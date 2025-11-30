# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Mike_2\Eclipse workspace\DrumBurp\src\GUI\defaultKitManager.ui'
#
# Created: Sat Oct 13 16:38:05 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DefaulKitManager(object):
    def setupUi(self, DefaulKitManager):
        DefaulKitManager.setObjectName(_fromUtf8("DefaulKitManager"))
        DefaulKitManager.resize(353, 311)
        self.horizontalLayout = QtWidgets.QHBoxLayout(DefaulKitManager)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.defaultKitList = QtWidgets.QListWidget(DefaulKitManager)
        self.defaultKitList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.defaultKitList.setProperty("showDropIndicator", False)
        self.defaultKitList.setObjectName(_fromUtf8("defaultKitList"))
        self.horizontalLayout.addWidget(self.defaultKitList)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.saveButton = QtWidgets.QPushButton(DefaulKitManager)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.verticalLayout.addWidget(self.saveButton)
        self.overwriteButton = QtWidgets.QPushButton(DefaulKitManager)
        self.overwriteButton.setObjectName(_fromUtf8("overwriteButton"))
        self.verticalLayout.addWidget(self.overwriteButton)
        self.deleteButton = QtWidgets.QPushButton(DefaulKitManager)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.verticalLayout.addWidget(self.deleteButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.openButton = QtWidgets.QPushButton(DefaulKitManager)
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.verticalLayout.addWidget(self.openButton)
        self.cancelButton = QtWidgets.QPushButton(DefaulKitManager)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.verticalLayout.addWidget(self.cancelButton)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(DefaulKitManager)
        self.cancelButton.clicked.connect(DefaulKitManager.reject)
        self.openButton.clicked.connect(DefaulKitManager.accept)
        self.defaultKitList.itemDoubleClicked.connect(DefaulKitManager.accept)
        QtCore.QMetaObject.connectSlotsByName(DefaulKitManager)
        DefaulKitManager.setTabOrder(self.defaultKitList, self.saveButton)
        DefaulKitManager.setTabOrder(self.saveButton, self.overwriteButton)
        DefaulKitManager.setTabOrder(self.overwriteButton, self.deleteButton)
        DefaulKitManager.setTabOrder(self.deleteButton, self.openButton)
        DefaulKitManager.setTabOrder(self.openButton, self.cancelButton)

    def retranslateUi(self, DefaulKitManager):
        DefaulKitManager.setWindowTitle(QtWidgets.QApplication.translate("DefaulKitManager", "Default Kit Manager"))
        self.defaultKitList.setToolTip(QtWidgets.QApplication.translate("DefaulKitManager", "Available default kits"))
        self.defaultKitList.setWhatsThis(QtWidgets.QApplication.translate("DefaulKitManager", "<html><head/><body><p><span style=\" font-weight:600;\">Default kit list</span></p><p><br/></p><p>Kits listed here can be loaded into the kit editor by double-clicking, or selecting them and clicking the <span style=\" font-style:italic;\">Open</span> button.</p><p><br/></p><p>Kits listed in <span style=\" font-style:italic;\">italics</span> are built into DrumBurp and cannot be overwritten, deleted or renamed.</p></body></html>", None))
        self.saveButton.setToolTip(QtWidgets.QApplication.translate("DefaulKitManager", "Save the current kit as a new default"))
        self.saveButton.setWhatsThis(QtWidgets.QApplication.translate("DefaulKitManager", "<html><head/><body><p><span style=\" font-weight:600;\">Save a new default kit</span></p><p><br/></p><p>Save the kit currently loaded in the kit editor as a new default. You will be asked a name to save it under, then it will appear in this dialog whenever you run DrumBurp in the future.</p></body></html>", None))
        self.saveButton.setText(QtWidgets.QApplication.translate("DefaulKitManager", "Save New"))
        self.overwriteButton.setToolTip(QtWidgets.QApplication.translate("DefaulKitManager", "Overwrite this default kit"))
        self.overwriteButton.setWhatsThis(QtWidgets.QApplication.translate("DefaulKitManager", "<html><head/><body><p><span style=\" font-weight:600;\">Overwrite this default kit</span></p><p><br/></p><p>The currently selected default kit will be overwritten with the kit currently loaded into the kit editor.</p></body></html>", None))
        self.overwriteButton.setText(QtWidgets.QApplication.translate("DefaulKitManager", "Overwrite"))
        self.deleteButton.setToolTip(QtWidgets.QApplication.translate("DefaulKitManager", "Delete this default kit"))
        self.deleteButton.setWhatsThis(QtWidgets.QApplication.translate("DefaulKitManager", "<html><head/><body><p><span style=\" font-weight:600;\">Delete this default kit</span></p><p><br/></p><p>Delete this default kit from the default kit list. DrumBurp builtin default kits cannot be deleted.</p></body></html>", None))
        self.deleteButton.setText(QtWidgets.QApplication.translate("DefaulKitManager", "Delete"))
        self.openButton.setToolTip(QtWidgets.QApplication.translate("DefaulKitManager", "Load this default kit"))
        self.openButton.setWhatsThis(QtWidgets.QApplication.translate("DefaulKitManager", "<html><head/><body><p><span style=\" font-weight:600;\">Load default kit</span></p><p><br/></p><p>Load the currently selected default kit into the kit editor.</p></body></html>", None))
        self.openButton.setText(QtWidgets.QApplication.translate("DefaulKitManager", "Load"))
        self.cancelButton.setToolTip(QtWidgets.QApplication.translate("DefaulKitManager", "Cancel this dialog"))
        self.cancelButton.setText(QtWidgets.QApplication.translate("DefaulKitManager", "Cancel"))

