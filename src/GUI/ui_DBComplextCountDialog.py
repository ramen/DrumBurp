# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mike_2\Eclipse workspace\DrumBurp\src\GUI\DBComplextCountDialog.ui'
#
# Created: Sat Mar 31 13:52:20 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_complexCountDialog(object):
    def setupUi(self, complexCountDialog):
        complexCountDialog.setObjectName(_fromUtf8("complexCountDialog"))
        complexCountDialog.resize(322, 251)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(complexCountDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.beatList = QtWidgets.QListWidget(complexCountDialog)
        self.beatList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.beatList.setProperty("showDropIndicator", False)
        self.beatList.setObjectName(_fromUtf8("beatList"))
        self.horizontalLayout_2.addWidget(self.beatList)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.addButton = QtWidgets.QPushButton(complexCountDialog)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.verticalLayout.addWidget(self.addButton)
        self.deleteButton = QtWidgets.QPushButton(complexCountDialog)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.verticalLayout.addWidget(self.deleteButton)
        self.label_2 = QtWidgets.QLabel(complexCountDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.countBox = QtWidgets.QComboBox(complexCountDialog)
        self.countBox.setObjectName(_fromUtf8("countBox"))
        self.verticalLayout.addWidget(self.countBox)
        self.label_3 = QtWidgets.QLabel(complexCountDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.numTicksSpinBox = QtWidgets.QSpinBox(complexCountDialog)
        self.numTicksSpinBox.setObjectName(_fromUtf8("numTicksSpinBox"))
        self.verticalLayout.addWidget(self.numTicksSpinBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(complexCountDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.previewText = QtWidgets.QLabel(self.groupBox)
        self.previewText.setAutoFillBackground(False)
        self.previewText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.previewText.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.previewText.setAlignment(QtCore.Qt.AlignCenter)
        self.previewText.setWordWrap(True)
        self.previewText.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.previewText.setObjectName(_fromUtf8("previewText"))
        self.horizontalLayout.addWidget(self.previewText)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(complexCountDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.Reset)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(complexCountDialog)
        self.buttonBox.accepted.connect(complexCountDialog.accept)
        self.buttonBox.rejected.connect(complexCountDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(complexCountDialog)

    def retranslateUi(self, complexCountDialog):
        complexCountDialog.setWindowTitle(QtWidgets.QApplication.translate("complexCountDialog", "Edit Complex Measure Count"))
        self.beatList.setToolTip(QtWidgets.QApplication.translate("complexCountDialog", "List of beats in the measure count"))
        self.addButton.setToolTip(QtWidgets.QApplication.translate("complexCountDialog", "Add a new beat at the end of this count"))
        self.addButton.setText(QtWidgets.QApplication.translate("complexCountDialog", "Add Beat"))
        self.deleteButton.setToolTip(QtWidgets.QApplication.translate("complexCountDialog", "Delete the currently selected count"))
        self.deleteButton.setText(QtWidgets.QApplication.translate("complexCountDialog", "Delete Beat"))
        self.label_2.setText(QtWidgets.QApplication.translate("complexCountDialog", "Count"))
        self.countBox.setToolTip(QtWidgets.QApplication.translate("complexCountDialog", "Count to use for the current beat"))
        self.label_3.setText(QtWidgets.QApplication.translate("complexCountDialog", "Ticks"))
        self.numTicksSpinBox.setToolTip(QtWidgets.QApplication.translate("complexCountDialog", "How many ticks of the count should the current beat use?"))
        self.groupBox.setToolTip(QtWidgets.QApplication.translate("complexCountDialog", "Preview of the measure count according to the current settings"))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("complexCountDialog", "Preview"))
        self.previewText.setText(QtWidgets.QApplication.translate("complexCountDialog", "TextLabel"))
        self.buttonBox.setToolTip(QtWidgets.QApplication.translate("complexCountDialog", "Reset the count to the original settings"))

