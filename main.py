import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
import sys
sys.path.insert(0, "..")
import xml.etree.ElementTree as ET
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.styles import get_style_by_name
from pygments.formatters import HtmlFormatter
import subprocess
from xml.dom import minidom
from Config import ConfigReader,ConfigWriter
from opcua.crypto import uacrypto
import time



try:
    from IPython import embed
except ImportError:
    import code

    def embed():
        vars = globals()
        vars.update(locals())
        shell = code.InteractiveConsole(vars)
        shell.interact()


from opcua import Client
from opcua import ua

from Atvise import Ui_MainWindow



class ViewFormatter():
    def format(self,value):
            script = self.getScript(value)
            if script:
                HtmlFormatter(style='paraiso-dark').style
                lexer = get_lexer_by_name("javascript", stripall=True)
                formatter = HtmlFormatter(linenos=True,noclasses=True, cssclass="source")
                result = highlight(script, lexer, formatter)
                return result
            else:
                result = script;
                return result;

    def getScript(self,value):
        root = ET.fromstring(value)
        for node in root.iter('{http://www.w3.org/2000/svg}script'):
            return node.text


class OPCUAConnector():
    def __init__(self):
        self.client = ""
        self.displays = []
        self.connectionstatus = False

    def setAddress(self,adress):
        self.client = Client(adress)


    def connect(self):
            self.displays = []
            if self.connectionstatus == False:
                self.client.connect()
                prog.ConnectButton.setText("Disconnect")
                prog.ConnectCombo.setEnabled(False)
                self.connectionstatus = True
            else:
                self.close()
                self.connectionstatus = False



    def close(self):
            prog.ConnectCombo.setEnabled(True)
            prog.Nodes.clear()
            prog.Content.clear()
            prog.ConnectButton.setText("Connect")
            prog.pushButton.setEnabled(False)


    def browse(self,start,filtertype):
        address = start
        filter = filtertype
        root = self.client.get_node(start).get_children()
        if len(root) > 0:
            for idx in root:

                if (self.client.get_node(idx).get_type_definition() == filtertype):
                    self.displays.append(self.client.get_node(idx).nodeid.to_string())
                self.browse(idx,filter)

    def getDisplays(self):
        return self.displays

    def getValue(self,item):
        value = self.client.get_node(item).get_value().Value
        return value;


    def writeValue(self,item,value):
        th = self.client.get_node(item)
        root = ET.fromstring(self.getValue(item))
        for node in root.iter('{http://www.w3.org/2000/svg}script'):
            node.text = '<![CDATA[' + value + ']]>';

        #  node.text = '<![CDATA['.encode() + value + ']]>';
        ET.register_namespace("", "http://www.w3.org/2000/svg")
        ET.register_namespace("atv","http://webmi.atvise.com/2007/svgext")
        ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")
        root_string = ET.tostring(root,encoding="UTF-8",method="html")

        test=  minidom.parseString(ET.tostring(root,encoding="UTF-8")).toprettyxml()

        try:
            tet = th.get_attribute(13)
            #th.set_writable(True)
            val = str(test).replace("&lt;", "<")
            val2 = val.replace("&gt;", ">")
            val3 = val2.replace("&quot;",'"');
            length = int(len(val3)-1)
            tet.Value.Value.Value = val3
            th.set_value(tet)


        except:
            print("Unexpected error:", sys.exc_info())


class MyFirstGuiProgram(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)

    def addListtoView(self,list):
        for i in list:
          self.Nodes.addItem(QListWidgetItem(str(i)))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QMainWindow()
    ViewFormat = ViewFormatter()
    prog = MyFirstGuiProgram(dialog)
    At = OPCUAConnector();
    test = []
    value = ""
    selectNode = ""
    configreader = ConfigReader()
    configwriter = ConfigWriter()
    prog.pushButton.setEnabled(False)

    def showValue(index):
        global value
        global selectNode
        selectNode = prog.Nodes.model().itemData(index)[0]
        value = At.getValue(prog.Nodes.model().itemData(index)[0])
        if ViewFormat.format(value):
            prog.pushButton.setEnabled(True)
            prog.Content.setHtml(ViewFormat.format(value))
        else:
            prog.pushButton.setEnabled(False)
            prog.Content.setText("Kein Scriptcode vorhanden")


    def connectatvise():
        global test
        test = []
        At.setAddress(prog.ConnectCombo.currentText())
        configwriter.writeLastConnection(prog.ConnectCombo.currentText())
        At.connect()
        if At.connectionstatus == True:
            At.browse("ns=1;s=AGENT", "VariableTypes.ATVISE.Display")
            test = At.getDisplays()
            prog.addListtoView(test)
            prog.Content.setReadOnly(True)
            try:
                prog.Nodes.clicked.connect(showValue)
            except:
                print("Unexpected error:", sys.exc_info()[0])

    def openFile():
        file = open("temp.js","w")
        file.write(ViewFormat.getScript(value))
        if(prog.CopyCheckbox.isChecked()):
            file_backup = open("backups/" + selectNode  + "-" + time.strftime("%y%m%d%H%M") + ".js","w")
            file_backup.write(ViewFormat.getScript(value))
        file.close()
        jsfile = "temp.js"
        editorPath = r''+configreader.getEditorPath()+''
        process = subprocess.Popen("%s %s" % (editorPath,jsfile))
        dialog.showMinimized()

        stdoutdata, stderrdata = process.communicate()
        if process.returncode == 0:
            dialog.showNormal()
            file = open("temp.js","r")
            content = file.read()
            At.writeValue(selectNode,content)
            file.close();


    prog.ConnectCombo.addItems(configreader.getLastConnection())
    prog.ConnectButton.clicked.connect(connectatvise)

    prog.pushButton.clicked.connect(openFile)
    dialog.setWindowIcon(QtGui.QIcon('icon.png'))
    dialog.show()
    sys.exit(app.exec_())

