# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mike_2\Eclipse workspace\DrumBurp\src\GUI\asciiDialog.ui'
#
# Created: Sat Mar 31 13:52:19 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_asciiDialog(object):
    def setupUi(self, asciiDialog):
        asciiDialog.setObjectName(_fromUtf8("asciiDialog"))
        asciiDialog.resize(487, 169)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(asciiDialog.sizePolicy().hasHeightForWidth())
        asciiDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(asciiDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.filenameButton = QtWidgets.QPushButton(asciiDialog)
        self.filenameButton.setObjectName(_fromUtf8("filenameButton"))
        self.horizontalLayout.addWidget(self.filenameButton)
        self.filenameLabel = QtWidgets.QLabel(asciiDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filenameLabel.sizePolicy().hasHeightForWidth())
        self.filenameLabel.setSizePolicy(sizePolicy)
        self.filenameLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.filenameLabel.setObjectName(_fromUtf8("filenameLabel"))
        self.horizontalLayout.addWidget(self.filenameLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.metadataCheck = QtWidgets.QCheckBox(asciiDialog)
        self.metadataCheck.setChecked(True)
        self.metadataCheck.setObjectName(_fromUtf8("metadataCheck"))
        self.gridLayout.addWidget(self.metadataCheck, 0, 0, 1, 1)
        self.underlineCheck = QtWidgets.QCheckBox(asciiDialog)
        self.underlineCheck.setChecked(True)
        self.underlineCheck.setObjectName(_fromUtf8("underlineCheck"))
        self.gridLayout.addWidget(self.underlineCheck, 0, 1, 1, 1)
        self.kitKeyCheck = QtWidgets.QCheckBox(asciiDialog)
        self.kitKeyCheck.setChecked(True)
        self.kitKeyCheck.setObjectName(_fromUtf8("kitKeyCheck"))
        self.gridLayout.addWidget(self.kitKeyCheck, 2, 0, 1, 1)
        self.omitEmptyCheck = QtWidgets.QCheckBox(asciiDialog)
        self.omitEmptyCheck.setChecked(True)
        self.omitEmptyCheck.setObjectName(_fromUtf8("omitEmptyCheck"))
        self.gridLayout.addWidget(self.omitEmptyCheck, 3, 0, 1, 1)
        self.printCountsCheck = QtWidgets.QCheckBox(asciiDialog)
        self.printCountsCheck.setChecked(True)
        self.printCountsCheck.setObjectName(_fromUtf8("printCountsCheck"))
        self.gridLayout.addWidget(self.printCountsCheck, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.emptyLineAfterSectionCheck = QtWidgets.QCheckBox(asciiDialog)
        self.emptyLineAfterSectionCheck.setChecked(True)
        self.emptyLineAfterSectionCheck.setObjectName(_fromUtf8("emptyLineAfterSectionCheck"))
        self.gridLayout.addWidget(self.emptyLineAfterSectionCheck, 3, 1, 1, 1)
        self.emptyLineBeforeSectionCheck = QtWidgets.QCheckBox(asciiDialog)
        self.emptyLineBeforeSectionCheck.setChecked(True)
        self.emptyLineBeforeSectionCheck.setObjectName(_fromUtf8("emptyLineBeforeSectionCheck"))
        self.gridLayout.addWidget(self.emptyLineBeforeSectionCheck, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(asciiDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(asciiDialog)
        self.buttonBox.accepted.connect(asciiDialog.accept)
        self.buttonBox.rejected.connect(asciiDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(asciiDialog)

    def retranslateUi(self, asciiDialog):
        asciiDialog.setWindowTitle(QtWidgets.QApplication.translate("asciiDialog", "Export ASCII file"))
        self.filenameButton.setToolTip(QtWidgets.QApplication.translate("asciiDialog", "Click to select a new filename"))
        self.filenameButton.setText(QtWidgets.QApplication.translate("asciiDialog", "Filename:"))
        self.filenameLabel.setToolTip(QtWidgets.QApplication.translate("asciiDialog", "The filename to export this score to"))
        self.filenameLabel.setText(QtWidgets.QApplication.translate("asciiDialog", "Filename"))
        self.metadataCheck.setToolTip(QtWidgets.QApplication.translate("asciiDialog", "Export the song information"))
        self.metadataCheck.setText(QtWidgets.QApplication.translate("asciiDialog", "Song info (Title, artist, etc.)"))
        self.underlineCheck.setToolTip(QtWidgets.QApplication.translate("asciiDialog", "Underline each section title"))
        self.underlineCheck.setText(QtWidgets.QApplication.translate("asciiDialog", "Underline section titles with ~ characters"))
        self.kitKeyCheck.setToolTip(QtWidgets.QApplication.translate("asciiDialog", "Export the drum kit key"))
        self.kitKeyCheck.setText(QtWidgets.QApplication.translate("asciiDialog", "Drum kit key"))
        self.omitEmptyCheck.setToolTip(QtWidgets.QApplication.translate("asciiDialog", "Empty lines for unlocked drums are not written to the ASCII tab"))
        self.omitEmptyCheck.setText(QtWidgets.QApplication.translate("asciiDialog", "Omit empty lines for unlocked drums"))
        self.printCountsCheck.setToolTip(QtWidgets.QApplication.translate("asciiDialog", "Export the beat count underneath each measure"))
        self.printCountsCheck.setText(QtWidgets.QApplication.translate("asciiDialog", "Beat count"))
        self.emptyLineAfterSectionCheck.setToolTip(QtWidgets.QApplication.translate("asciiDialog", "Include a blank line after each section title"))
        self.emptyLineAfterSectionCheck.setText(QtWidgets.QApplication.translate("asciiDialog", "Empty line after section title"))
        self.emptyLineBeforeSectionCheck.setToolTip(QtWidgets.QApplication.translate("asciiDialog", "Include a blank line before each section title"))
        self.emptyLineBeforeSectionCheck.setText(QtWidgets.QApplication.translate("asciiDialog", "Empty line before section title"))

