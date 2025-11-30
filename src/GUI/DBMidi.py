# Copyright 2011-2015 Michael Thomas
#
# See www.whatang.org for more information.
#
# This file is part of DrumBurp.
#
# DrumBurp is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DrumBurp is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DrumBurp.  If not, see <http://www.gnu.org/licenses/>
'''
Created on 17 Sep 2011

@author: Mike Thomas

'''
import copy

HAS_MIDI = False
_MIDI_INITIALIZED = False
_PERCUSSION_CHANNEL = 0x09
_NOTE_ON = 0x90
_NOTE_OFF = 0x80
_CHOKE = 0xB0
_CHOKE_MSG = 120
_CHOKE_VELOCITY = 0
_PERCUSSION_NOTE_ON = _PERCUSSION_CHANNEL | _NOTE_ON
_PERCUSSION_NOTE_OFF = _PERCUSSION_CHANNEL | _NOTE_OFF
_PERCUSSION_CHOKE = _PERCUSSION_CHANNEL | _CHOKE
_BUFSIZE = 1024
_LATENCY = 1

_FREQ = 44100  # audio CD quality
_BITSIZE = -16  # unsigned 16 bit
_CHANNELS = 2  # 1 is mono, 2 is stereo
_NUMSAMPLES = 4096  # number of samples

FLAM_TIME_CONSTANT = 32
FLAM_VOLUME_CONSTANT = 2
DRAG_TIME_CONSTANT = 96

from PyQt5.QtCore import QThread
import atexit
import time
from io import BytesIO

try:
    import pygame
    import pygame.midi
    _HAS_PYGAME = True

    def getDefaultId():
        # Ensure pygame.midi is initialized
        try:
            if not pygame.midi.get_init():
                pygame.midi.init()
        except:
            return -1

        # Prefer TiMidity or FluidSynth over "Midi Through" ports
        # as Midi Through ports don't produce sound without routing
        preferred_names = [b'TiMidity', b'FluidSynth', b'Fluid', b'Synth']
        avoid_names = [b'Midi Through', b'VirMIDI']

        try:
            default_id = pygame.midi.get_default_output_id()
        except:
            return -1

        try:
            # Check if default is good (not a pass-through port)
            if default_id != -1:
                info = pygame.midi.get_device_info(default_id)
                if info:
                    name = info[1]
                    # If default is not a pass-through port, use it
                    if not any(avoid in name for avoid in avoid_names):
                        return default_id

            # Look for preferred synthesizer ports
            for device_id in range(pygame.midi.get_count()):
                info = pygame.midi.get_device_info(device_id)
                if info:
                    interface, name, is_input, is_output, opened = info
                    # Check if it's an output device
                    if is_output:
                        # Prefer synthesizer ports
                        if any(pref in name for pref in preferred_names):
                            return device_id

            # Look for any non-pass-through output
            for device_id in range(pygame.midi.get_count()):
                info = pygame.midi.get_device_info(device_id)
                if info:
                    interface, name, is_input, is_output, opened = info
                    if is_output and not any(avoid in name for avoid in avoid_names):
                        return device_id

            # Fall back to system default
            return default_id
        except:
            return -1

    def iterDeviceIds():
        return range(pygame.midi.get_count())

    def getDeviceInfo(deviceId):
        int_, name, isIn, isOut, isOpen = pygame.midi.get_device_info(deviceId)
        # Decode bytes to string for Python 3
        if isinstance(name, bytes):
            name = name.decode('utf-8', errors='replace')
        return name, isIn == 1, isOut == 1, isOpen == 1

    def cleanup():
        _PLAYER.cleanup()
        pygame.mixer.quit()
        pygame.midi.quit()
        pygame.quit()  # IGNORE:no-member

except ImportError:
    _HAS_PYGAME = False

    def getDefaultId():
        return -1

    def iterDeviceIds():
        return iter([])

    def getDeviceInfo(deviceId_):
        return None, False, False, False

    def cleanup():
        if _PLAYER is not None:
            _PLAYER.cleanup()


class MidiDevice(object):
    def __init__(self, deviceId):
        self.deviceId = deviceId
        self.name, in_, self._isOutput, self._isOpen = getDeviceInfo(deviceId)
        self._isValid = self.name is not None

    def isValid(self):
        return self._isValid

    def isOutput(self):
        return self._isOutput

    def isOpen(self):
        return getDeviceInfo(self.deviceId)[3]


_OUTPUT_DEVICES = []


def refreshOutputDevices():
    # No device selection needed with pygame.mixer.music
    pass


def iterMidiDevices():
    # No devices to select with pygame.mixer.music
    return iter([])


from PyQt5.QtCore import QTimer, pyqtSignal, QObject
from Data.DBConstants import MIDITICKSPERBEAT


class _midi(QObject):
    def __init__(self):
        super(_midi, self).__init__()
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self._onSongEnd)
        self._measureDetails = []
        self._measureTimer = QTimer()
        self._measureTimer.setSingleShot(True)
        self._measureTimer.timeout.connect(self._highlight)
        self._songStart = None
        self._mute = False
        self._musicPlaying = False
        self.kit = None

    def initialize(self):
        if not _MIDI_INITIALIZED:
            raise RuntimeError("MIDI not initialized yet!")
        # pygame.mixer.music is initialized globally, nothing to do here

    def setPort(self, port):
        # Port selection not needed for pygame.mixer.music
        pass

    def port(self):
        return -1

    def isGood(self):
        return _MIDI_INITIALIZED

    def setMute(self, onOff):
        self._mute = onOff

    def isMuted(self):
        return self._mute

    highlightMeasure = pyqtSignal(int, int)

    def playNote(self, drumIndex, head):
        if self.kit is None or self._mute:
            return
        headData = self.kit[drumIndex].headData(head)
        self.playHeadData(headData)

    def playHeadData(self, headData, when=None):
        # Stop any currently playing note
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

        # Generate a mini MIDI file with just this one note
        try:
            midi = BytesIO()
            self._exportSingleNote(headData, midi)
            midi.seek(0, 0)
            pygame.mixer.music.load(midi)
            pygame.mixer.music.play()
        except:
            # Silently ignore playback failures
            pass

    def _exportSingleNote(self, headData, handle):
        """Export a single note as a complete MIDI file for playback"""
        from Data.DBConstants import MIDITICKSPERBEAT

        # Write MIDI header
        handle.write(b"MThd\x00\x00\x00\x06\x00\x00\x00\x01")
        handle.write(bytes([(MIDITICKSPERBEAT >> 8) & 0xFF]))
        handle.write(bytes([(MIDITICKSPERBEAT >> 0) & 0xFF]))

        # Create MIDI events for the note (using proper variable-length delta times)
        midiData = []

        # Track start marker with text event
        midiData.extend([0, 0xff, 0x1, 0])

        # Set tempo to 120 BPM (500000 microseconds per beat)
        midiData.extend([0, 0xff, 0x51, 3, 0x07, 0xA1, 0x20])

        # Schedule the note(s) based on effect
        if headData.effect == "flam":
            # Grace note
            deltaTime = 0
            encodeSevenBitDelta(deltaTime, midiData)
            midiData.extend([_PERCUSSION_NOTE_ON, headData.midiNote,
                           int(headData.midiVolume / FLAM_VOLUME_CONSTANT)])
            # Main note shortly after
            deltaTime = int(MIDITICKSPERBEAT / FLAM_TIME_CONSTANT)
            encodeSevenBitDelta(deltaTime, midiData)
            midiData.extend([_PERCUSSION_NOTE_ON, headData.midiNote, headData.midiVolume])
        elif headData.effect == "drag":
            # First note
            encodeSevenBitDelta(0, midiData)
            midiData.extend([_PERCUSSION_NOTE_ON, headData.midiNote, headData.midiVolume])
            # Second note
            deltaTime = int(MIDITICKSPERBEAT / 10)
            encodeSevenBitDelta(deltaTime, midiData)
            midiData.extend([_PERCUSSION_NOTE_ON, headData.midiNote, headData.midiVolume])
        elif headData.effect == "choke":
            # Note on
            encodeSevenBitDelta(0, midiData)
            midiData.extend([_PERCUSSION_NOTE_ON, headData.midiNote, headData.midiVolume])
            # Choke shortly after
            deltaTime = int(MIDITICKSPERBEAT / 10)
            encodeSevenBitDelta(deltaTime, midiData)
            midiData.extend([_PERCUSSION_CHOKE, _CHOKE_MSG, _CHOKE_VELOCITY])
        else:
            # Simple note
            encodeSevenBitDelta(0, midiData)
            midiData.extend([_PERCUSSION_NOTE_ON, headData.midiNote, headData.midiVolume])

        # Wait a bit then end track (let note ring)
        encodeSevenBitDelta(MIDITICKSPERBEAT * 2, midiData)
        midiData.extend([0xFF, 0x2F, 0])

        # Write track header and data
        handle.write(b"MTrk")
        numBytes = len(midiData)
        lenBytes = [((numBytes >> i) & 0xff) for i in range(24, -8, -8)]
        for byte in lenBytes:
            handle.write(bytes([byte]))
        for byte in midiData:
            handle.write(bytes([int(byte) & 0xFF]))

    def playScore(self, score):
        measureList = list(score.iterMeasuresWithRepeats())
        self._playMIDINow(measureList, score)

    def _playMIDINow(self, measureList, score):
        if self.kit is None:
            return

        # Stop any currently playing music
        if self._musicPlaying:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            self._musicPlaying = False

        # Calculate measure timings for highlighting
        baseTime = 0
        bpm = score.scoreData.bpm
        swing = score.scoreData.swing
        msPerBeat = 60000.0 / bpm
        self._measureDetails = []
        lastMeasureIndex = None

        for measure, measureIndex in measureList:
            if lastMeasureIndex is None or measureIndex != lastMeasureIndex + 1:
                bpm = score.bpmAtMeasureByIndex(measureIndex)
            elif measure.newBpm > 0 and bpm != measure.newBpm:
                bpm = measure.newBpm
            if bpm == 0:
                bpm = 120
            lastMeasureIndex = measureIndex
            msPerBeat = 60000.0 / bpm
            times = list(measure.counter.iterTimesMs(msPerBeat, swing))
            baseTime += times[-1]
            self._measureDetails.append((measureIndex, baseTime))

        self._measureDetails.reverse()

        # Generate and play MIDI file
        try:
            midi = BytesIO()
            exportMidi(measureList, score, midi)
            midi.seek(0, 0)
            pygame.mixer.music.load(midi)
            pygame.mixer.music.play()
            self._songStart = time.perf_counter()
            self._musicPlaying = True
            self.timer.start(int(baseTime + 500))
            self._measureTimer.start(0)
        except:
            self.timer.timeout.emit()
            raise

    def loopBars(self, measureIterator, score, loopCount=100):
        measureList = [(measure, measureIndex) for
                       (measure, measureIndex, unused)
                       in measureIterator] * loopCount
        for index, (measure, measureIndex) in enumerate(measureList):
            if measure.simileDistance > 0:
                measure = score.getReferredMeasure(measureIndex)
                measureList[index] = (measure, measureIndex)
        self._playMIDINow(measureList, score)

    def _onSongEnd(self):
        """Called when song finishes playing naturally (timer expires)"""
        self._cleanupAfterPlayback()

    def _cleanupAfterPlayback(self):
        """Clean up after playback"""
        if self._musicPlaying:
            self._measureDetails = []
            self._measureTimer.stop()
            self.highlightMeasure.emit(-1, -1)
            pygame.mixer.music.stop()
            try:
                pygame.mixer.music.unload()
            except:
                pass
            self._musicPlaying = False

    def shutUp(self):
        # Always stop the timer to prevent it from firing later
        self.timer.stop()
        self._cleanupAfterPlayback()

    def cleanup(self):
        # Nothing to clean up - pygame.mixer.music is managed globally
        pass

    def _highlight(self):
        delay = -1
        measureIndex = None
        nextMeasure = -1
        while delay < 0 and self._measureDetails:
            measureIndex, measureEnd = self._measureDetails.pop()
            if self._measureDetails:
                nextMeasure = self._measureDetails[-1][0]
            delay = (measureEnd - 1000 * (time.perf_counter() - self._songStart))
        if measureIndex is not None:
            self.highlightMeasure.emit(measureIndex, nextMeasure)
        else:
            self.highlightMeasure.emit(-1, -1)
        if delay > 0:
            self._measureTimer.start(int(delay))


_PLAYER = _midi()
SONGEND_SIGNAL = _PLAYER.timer.timeout
HIGHLIGHT_SIGNAL = _PLAYER.highlightMeasure


def setKit(drumKit):
    _PLAYER.kit = drumKit


def playNote(drumIndex, head):
    _PLAYER.playNote(drumIndex, head)


def playHeadData(headData):
    _PLAYER.playHeadData(headData)


def playScore(score):
    _PLAYER.playScore(score)


def loopBars(measureIterator, score, loopCount=100):
    _PLAYER.loopBars(measureIterator, score, loopCount)


def shutUp():
    _PLAYER.shutUp()


def setMute(onOff):
    _PLAYER.setMute(onOff)


def isMuted():
    return _PLAYER.isMuted()


def encodeSevenBitDelta(delta, midiData):
    values = []
    lastByte = True
    # Convert to int for bitwise operations
    delta = int(delta)
    if delta <= 0:
        midiData.append(0)
        return
    while delta:
        thisValue = (delta & 0x7F)
        delta >>= 7
        if lastByte:
            lastByte = False
        else:
            thisValue |= 0x80
        values.append(thisValue)
    values.reverse()
    midiData.extend(values)


def _makeMidiStart(score):
    signature = "Created with DrumBurp"
    midiData = []
    midiData.extend([0, 0xff, 0x1, len(signature)])
    midiData.extend([ord(ch) for ch in signature])
    return midiData


def _writeMidiNotes(midiObjects, baseTime):
    lastNoteTime = 0
    midiData = []
    for midiEvent in midiObjects:
        deltaTime = midiEvent.time - lastNoteTime
        lastNoteTime = midiEvent.time
        encodeSevenBitDelta(deltaTime, midiData)
        midiData.extend(midiEvent.write())
    # Turn off drum notes
    deltaTime = baseTime - lastNoteTime
    # Insert a delay before the end of the track.
    encodeSevenBitDelta(deltaTime + 4 * MIDITICKSPERBEAT, midiData)
    midiData.extend([_PERCUSSION_NOTE_OFF, 38, 0])
    encodeSevenBitDelta(0, midiData)
    midiData.extend([0xFF, 0x2F, 0])
    return midiData


def _finishMidiData(midiData):
    numBytes = len(midiData)
    lenBytes = [((numBytes >> i) & 0xff) for i in range(24, -8, -8)]
    return lenBytes + midiData


class MidiObject(object):
    def __init__(self, eventTime):
        self.time = eventTime

    def __lt__(self, other):
        return self.time < other.time

    def write(self):
        raise NotImplementedError()


class MidiTempoChange(MidiObject):
    def __init__(self, eventTime, bpm):
        super(MidiTempoChange, self).__init__(eventTime)
        self.bpm = bpm

    def write(self):
        msPerBeat = int(60000000 / self.bpm)
        return [0xff, 0x51, 3, (msPerBeat >> 16) & 0xff,
                (msPerBeat >> 8) & 0xff, msPerBeat & 0xff]


class MidiNote(MidiObject):
    def __init__(self, noteTime, headData):
        super(MidiNote, self).__init__(noteTime)
        self.headData = headData

    def write(self):
        return [_PERCUSSION_NOTE_ON, self.headData.midiNote,
                self.headData.midiVolume]


class MidiChoke(MidiObject):
    def write(self):
        return [_PERCUSSION_CHOKE, _CHOKE_MSG, _CHOKE_VELOCITY]


def _calculateMidiTimes(measureIterator, score):
    notes = []
    baseTime = 1
    lastBpm = None
    lastMeasureIndex = None
    swing = score.scoreData.swing
    for measure, measureIndex in measureIterator:
        measureNotes = []
        times = list(measure.counter.iterMidiTicks(swing))
        if lastMeasureIndex is None or measureIndex != lastMeasureIndex + 1:
            bpm = score.bpmAtMeasureByIndex(measureIndex)
        elif measure.newBpm > 0 and bpm != measure.newBpm:
            bpm = measure.newBpm
        lastMeasureIndex = measureIndex
        if bpm == 0:
            bpm = 120
        if bpm != lastBpm:
            notes.append(MidiTempoChange(baseTime + times[0], bpm))
            lastBpm = bpm
        for notePos, head in measure:
            drumData = score.drumKit[notePos.drumIndex]
            headData = drumData.headData(head)
            if headData is not None:
                noteTime = baseTime + times[notePos.noteTime]
                divisionTicks = times[notePos.noteTime +
                                      1] - times[notePos.noteTime]
                if headData.effect == "flam":
                    headCopy = copy.copy(headData)
                    headCopy.midiVolume = headData.midiVolume / FLAM_VOLUME_CONSTANT
                    measureNotes.append(
                        MidiNote(noteTime - (MIDITICKSPERBEAT / FLAM_TIME_CONSTANT), headCopy))
                elif headData.effect == "drag":
                    measureNotes.append(
                        MidiNote(noteTime + divisionTicks / 2, headData))
                elif headData.effect == "choke":
                    measureNotes.append(
                        MidiChoke(noteTime + divisionTicks / 2))
                measureNotes.append(MidiNote(noteTime, headData))
        baseTime += times[-1]
        measureNotes.sort()
        notes.extend(measureNotes)
    return notes, baseTime


def exportMidi(measureIterator, score, handle):
    handle.write(b"MThd\x00\x00\x00\x06\x00\x00\x00\x01")
    handle.write(bytes([(MIDITICKSPERBEAT >> 8) & 0xFF]))
    handle.write(bytes([(MIDITICKSPERBEAT >> 0) & 0xFF]))
    notes, baseTime = _calculateMidiTimes(measureIterator, score)
    midiData = _makeMidiStart(score)
    midiData += _writeMidiNotes(notes, baseTime)
    midiData = _finishMidiData(midiData)
    handle.write(b"MTrk")
    for byte in midiData:
        handle.write(bytes([int(byte)]))


def selectMidiDevice(dev):
    # No device selection needed with pygame.mixer.music
    return True


def currentDevice():
    # No current device with pygame.mixer.music
    return None


def _initialize():
    global HAS_MIDI, _MIDI_INITIALIZED
    if _MIDI_INITIALIZED:
        return
    if _HAS_PYGAME:
        pygame.init()  # IGNORE:no-member
        pygame.midi.init()
        pygame.mixer.init(_FREQ, _BITSIZE, _CHANNELS, _NUMSAMPLES)
        pygame.mixer.music.set_volume(0.8)
    _MIDI_INITIALIZED = True
    _PLAYER.initialize()
    atexit.register(cleanup)
    HAS_MIDI = _HAS_PYGAME and _PLAYER.isGood()


class MidiInit(QThread):
    def run(self):  # IGNORE:no-self-use
        _initialize()


def main():
    _initialize()
    refreshOutputDevices()
    for device in iterMidiDevices():
        print(device.name)


if __name__ == "__main__":
    main()
