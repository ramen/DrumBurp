# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mike_2\Eclipse workspace\DrumBurp\src\GUI\newScoreDialog.ui'
#
# Created: Sat Oct 13 22:33:42 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_newScoreDialog(object):
    def setupUi(self, newScoreDialog):
        newScoreDialog.setObjectName(_fromUtf8("newScoreDialog"))
        newScoreDialog.resize(288, 298)
        newScoreDialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.verticalLayout = QtWidgets.QVBoxLayout(newScoreDialog)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtWidgets.QLabel(newScoreDialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.numMeasuresSpinBox = QtWidgets.QSpinBox(newScoreDialog)
        self.numMeasuresSpinBox.setMinimum(1)
        self.numMeasuresSpinBox.setMaximum(100000)
        self.numMeasuresSpinBox.setProperty("value", 32)
        self.numMeasuresSpinBox.setObjectName(_fromUtf8("numMeasuresSpinBox"))
        self.gridLayout.addWidget(self.numMeasuresSpinBox, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.measureTabs = measureTabs(newScoreDialog)
        self.measureTabs.setObjectName(_fromUtf8("measureTabs"))
        self.verticalLayout.addWidget(self.measureTabs)
        self.label_2 = QtWidgets.QLabel(newScoreDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.kitCombobox = QtWidgets.QComboBox(newScoreDialog)
        self.kitCombobox.setObjectName(_fromUtf8("kitCombobox"))
        self.verticalLayout.addWidget(self.kitCombobox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(newScoreDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label.setBuddy(self.numMeasuresSpinBox)
        self.label_2.setBuddy(self.kitCombobox)

        self.retranslateUi(newScoreDialog)
        self.buttonBox.accepted.connect(newScoreDialog.accept)
        self.buttonBox.rejected.connect(newScoreDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(newScoreDialog)
        newScoreDialog.setTabOrder(self.numMeasuresSpinBox, self.kitCombobox)
        newScoreDialog.setTabOrder(self.kitCombobox, self.buttonBox)

    def retranslateUi(self, newScoreDialog):
        newScoreDialog.setWindowTitle(QtWidgets.QApplication.translate("newScoreDialog", "New Score"))
        self.label.setToolTip(QtWidgets.QApplication.translate("newScoreDialog", "The number of measures in the new score"))
        self.label.setText(QtWidgets.QApplication.translate("newScoreDialog", "Number of measures"))
        self.numMeasuresSpinBox.setToolTip(QtWidgets.QApplication.translate("newScoreDialog", "The number of measures in the new score"))
        self.numMeasuresSpinBox.setStatusTip(QtWidgets.QApplication.translate("newScoreDialog", "The number of measures in the new score"))
        self.numMeasuresSpinBox.setSuffix(QtWidgets.QApplication.translate("newScoreDialog", " measures"))
        self.measureTabs.setToolTip(QtWidgets.QApplication.translate("newScoreDialog", "The default measure count for the new score"))
        self.label_2.setText(QtWidgets.QApplication.translate("newScoreDialog", "Drum kit"))

from Widgets.measureTabs_plugin import measureTabs
