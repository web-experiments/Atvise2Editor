# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Atvise.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Avise2Editor")
        MainWindow.resize(830, 661)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.URL = QtWidgets.QLineEdit(self.centralwidget)
        self.URL.setObjectName("URL")
        self.gridLayout.addWidget(self.URL, 2, 1, 1, 1)
        self.ConnectButton = QtWidgets.QPushButton(self.centralwidget)
        self.ConnectButton.setObjectName("ConnectButton")
        self.gridLayout.addWidget(self.ConnectButton, 2, 0, 1, 1)
        self.Content = QtWidgets.QTextEdit(self.centralwidget)
        self.Content.setOverwriteMode(False)
        self.Content.setObjectName("Content")
        self.gridLayout.addWidget(self.Content, 1, 0, 1, 2)
        self.Nodes = QtWidgets.QListWidget(self.centralwidget)
        self.Nodes.setObjectName("Nodes")
        self.gridLayout.addWidget(self.Nodes, 1, 2, 2, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Atvise2Editor"))
        self.ConnectButton.setText(_translate("MainWindow", "Connect"))
        self.Content.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "In Editor öffnen"))
        self.label.setText(_translate("MainWindow", "Verfügbare Displays"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

