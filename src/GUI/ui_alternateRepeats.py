# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mike_2\Eclipse workspace\DrumBurp\src\GUI\alternateRepeats.ui'
#
# Created: Sat Mar 31 13:52:18 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AlternateDialog(object):
    def setupUi(self, AlternateDialog):
        AlternateDialog.setObjectName(_fromUtf8("AlternateDialog"))
        AlternateDialog.resize(502, 214)
        self.verticalLayout = QtWidgets.QVBoxLayout(AlternateDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtWidgets.QLabel(AlternateDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.addButton = QtWidgets.QPushButton(AlternateDialog)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.horizontalLayout.addWidget(self.addButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.repeatsFrame = QtWidgets.QScrollArea(AlternateDialog)
        self.repeatsFrame.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.repeatsFrame.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.repeatsFrame.setWidgetResizable(True)
        self.repeatsFrame.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.repeatsFrame.setObjectName(_fromUtf8("repeatsFrame"))
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 465, 134))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(9, 0, -1, 0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.repeatsLayout = QtWidgets.QVBoxLayout()
        self.repeatsLayout.setSpacing(0)
        self.repeatsLayout.setObjectName(_fromUtf8("repeatsLayout"))
        self.verticalLayout_2.addLayout(self.repeatsLayout)
        self.stretchyLayout = QtWidgets.QVBoxLayout()
        self.stretchyLayout.setObjectName(_fromUtf8("stretchyLayout"))
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.stretchyLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.stretchyLayout)
        self.repeatsFrame.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.repeatsFrame)
        self.buttonBox = QtWidgets.QDialogButtonBox(AlternateDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AlternateDialog)
        self.buttonBox.accepted.connect(AlternateDialog.accept)
        self.buttonBox.rejected.connect(AlternateDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AlternateDialog)

    def retranslateUi(self, AlternateDialog):
        AlternateDialog.setWindowTitle(QtWidgets.QApplication.translate("AlternateDialog", "Alternate Repeats"))
        self.label.setText(QtWidgets.QApplication.translate("AlternateDialog", "Enter alternate repeat information:"))
        self.addButton.setToolTip(QtWidgets.QApplication.translate("AlternateDialog", "Add a new repeat"))
        self.addButton.setText(QtWidgets.QApplication.translate("AlternateDialog", "Add"))

