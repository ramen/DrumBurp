# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mike_2\Eclipse workspace\DrumBurp\src\GUI\insertMeasuresDialog.ui'
#
# Created: Sat Mar 31 13:52:23 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_InsertMeasuresDialog(object):
    def setupUi(self, InsertMeasuresDialog):
        InsertMeasuresDialog.setObjectName(_fromUtf8("InsertMeasuresDialog"))
        InsertMeasuresDialog.resize(288, 281)
        self.verticalLayout = QtWidgets.QVBoxLayout(InsertMeasuresDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtWidgets.QLabel(InsertMeasuresDialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.numMeasuresSpinBox = QtWidgets.QSpinBox(InsertMeasuresDialog)
        self.numMeasuresSpinBox.setSuffix(_fromUtf8(""))
        self.numMeasuresSpinBox.setMinimum(1)
        self.numMeasuresSpinBox.setMaximum(1000)
        self.numMeasuresSpinBox.setProperty("value", 1)
        self.numMeasuresSpinBox.setObjectName(_fromUtf8("numMeasuresSpinBox"))
        self.gridLayout.addWidget(self.numMeasuresSpinBox, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtWidgets.QLabel(InsertMeasuresDialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.beforeButton = QtWidgets.QRadioButton(InsertMeasuresDialog)
        self.beforeButton.setChecked(True)
        self.beforeButton.setObjectName(_fromUtf8("beforeButton"))
        self.horizontalLayout.addWidget(self.beforeButton)
        self.afterButton = QtWidgets.QRadioButton(InsertMeasuresDialog)
        self.afterButton.setObjectName(_fromUtf8("afterButton"))
        self.horizontalLayout.addWidget(self.afterButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.measureTabs = measureTabs(InsertMeasuresDialog)
        self.measureTabs.setObjectName(_fromUtf8("measureTabs"))
        self.verticalLayout.addWidget(self.measureTabs)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.buttonBox = QtWidgets.QDialogButtonBox(InsertMeasuresDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.numMeasuresSpinBox)
        self.label_3.setBuddy(self.beforeButton)

        self.retranslateUi(InsertMeasuresDialog)
        self.buttonBox.accepted.connect(InsertMeasuresDialog.accept)
        self.buttonBox.rejected.connect(InsertMeasuresDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InsertMeasuresDialog)

    def retranslateUi(self, InsertMeasuresDialog):
        InsertMeasuresDialog.setWindowTitle(QtWidgets.QApplication.translate("InsertMeasuresDialog", "Insert Measures"))
        self.label.setToolTip(QtWidgets.QApplication.translate("InsertMeasuresDialog", "Number of measures to insert"))
        self.label.setText(QtWidgets.QApplication.translate("InsertMeasuresDialog", "Number of measures"))
        self.numMeasuresSpinBox.setToolTip(QtWidgets.QApplication.translate("InsertMeasuresDialog", "Number of measures to insert"))
        self.label_3.setText(QtWidgets.QApplication.translate("InsertMeasuresDialog", "Insert Measures..."))
        self.beforeButton.setToolTip(QtWidgets.QApplication.translate("InsertMeasuresDialog", "Insert new measures before the current measure"))
        self.beforeButton.setText(QtWidgets.QApplication.translate("InsertMeasuresDialog", "Before"))
        self.afterButton.setToolTip(QtWidgets.QApplication.translate("InsertMeasuresDialog", "Insert new measures after the current measure"))
        self.afterButton.setText(QtWidgets.QApplication.translate("InsertMeasuresDialog", "After"))
        self.measureTabs.setToolTip(QtWidgets.QApplication.translate("InsertMeasuresDialog", "Select the count to use for the new measures"))

from Widgets.measureTabs_plugin import measureTabs
