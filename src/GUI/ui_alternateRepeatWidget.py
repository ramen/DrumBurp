# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mike_2\Eclipse workspace\DrumBurp\src\GUI\alternateRepeatWidget.ui'
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

class Ui_AlternateWidget(object):
    def setupUi(self, AlternateWidget):
        AlternateWidget.setObjectName(_fromUtf8("AlternateWidget"))
        AlternateWidget.resize(273, 24)
        self.horizontalLayout = QtWidgets.QHBoxLayout(AlternateWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.startBox = QtWidgets.QSpinBox(AlternateWidget)
        self.startBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.startBox.setMinimum(1)
        self.startBox.setMaximum(100000000)
        self.startBox.setObjectName(_fromUtf8("startBox"))
        self.horizontalLayout.addWidget(self.startBox)
        self.endBox = QtWidgets.QSpinBox(AlternateWidget)
        self.endBox.setEnabled(True)
        self.endBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.endBox.setReadOnly(False)
        self.endBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.endBox.setMinimum(1)
        self.endBox.setMaximum(10000000)
        self.endBox.setObjectName(_fromUtf8("endBox"))
        self.horizontalLayout.addWidget(self.endBox)
        self.rangeCheck = QtWidgets.QCheckBox(AlternateWidget)
        self.rangeCheck.setChecked(True)
        self.rangeCheck.setObjectName(_fromUtf8("rangeCheck"))
        self.horizontalLayout.addWidget(self.rangeCheck)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.deleteButton = QtWidgets.QPushButton(AlternateWidget)
        self.deleteButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/Icons/process-stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon)
        self.deleteButton.setFlat(True)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout.addWidget(self.deleteButton)

        self.retranslateUi(AlternateWidget)
        self.rangeCheck.toggled.connect(self.endBox.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(AlternateWidget)

    def retranslateUi(self, AlternateWidget):
        AlternateWidget.setWindowTitle(QtWidgets.QApplication.translate("AlternateWidget", "Form"))
        self.startBox.setToolTip(QtWidgets.QApplication.translate("AlternateWidget", "Repeat number"))
        self.endBox.setToolTip(QtWidgets.QApplication.translate("AlternateWidget", "Repeat number range end"))
        self.rangeCheck.setToolTip(QtWidgets.QApplication.translate("AlternateWidget", "Range of repeat numbers?"))
        self.rangeCheck.setText(QtWidgets.QApplication.translate("AlternateWidget", "Range?"))
        self.deleteButton.setToolTip(QtWidgets.QApplication.translate("AlternateWidget", "Delete this repeat"))

from GUI import DrumBurp_rc
