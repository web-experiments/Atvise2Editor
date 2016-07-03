# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atvise2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(836, 698)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.ConnectCombo = QtWidgets.QComboBox(self.centralwidget)
        self.ConnectCombo.setEditable(True)
        self.ConnectCombo.setObjectName("ConnectCombo")
        self.gridLayout.addWidget(self.ConnectCombo, 0, 0, 1, 1)
        self.ConnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectButton.setObjectName("ConnectButton")
        self.gridLayout.addWidget(self.ConnectButton, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.Content = QtWidgets.QTextEdit(self.centralwidget)
        self.Content.setMinimumSize(QtCore.QSize(401, 546))
        self.Content.setLineWidth(2)
        self.Content.setOverwriteMode(False)
        self.Content.setObjectName("Content")
        self.gridLayout.addWidget(self.Content, 2, 0, 1, 2)
        self.Nodes = QtWidgets.QListWidget(self.centralwidget)
        self.Nodes.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Nodes.setLineWidth(2)
        self.Nodes.setObjectName("Nodes")
        self.gridLayout.addWidget(self.Nodes, 2, 2, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.CopyCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.CopyCheckbox.setObjectName("CopyCheckbox")
        self.gridLayout.addWidget(self.CopyCheckbox, 3, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 836, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuMain = QtWidgets.QMenu(self.menuBar)
        self.menuMain.setObjectName("menuMain")
        MainWindow.setMenuBar(self.menuBar)
        self.actionEinstellungen = QtWidgets.QAction(MainWindow)
        self.actionEinstellungen.setObjectName("actionEinstellungen")
        self.actionBeenden = QtWidgets.QAction(MainWindow)
        self.actionBeenden.setEnabled(True)
        self.actionBeenden.setObjectName("actionBeenden")
        self.menuMain.addAction(self.actionEinstellungen)
        self.menuMain.addAction(self.actionBeenden)
        self.menuBar.addAction(self.menuMain.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ConnectButton.setText(_translate("MainWindow", "Connect"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Vorschau</span></p></body></html>"))
        self.Content.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "In Editor öffnen"))
        self.CopyCheckbox.setText(_translate("MainWindow", "Kopie erstellen"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Verfügbare Displays</span></p></body></html>"))
        self.menuMain.setTitle(_translate("MainWindow", "Main"))
        self.actionEinstellungen.setText(_translate("MainWindow", "Einstellungen"))
        self.actionBeenden.setText(_translate("MainWindow", "Beenden"))





