# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulator.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
################################################################################################
#User code
from PyQt5.QtCore import Qt
from assembler import Assembler
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(993, 649)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.browsAssembly = QtWidgets.QPushButton(self.centralwidget)
        self.browsAssembly.setGeometry(QtCore.QRect(360, 10, 51, 31))
        self.browsAssembly.setObjectName("browsAssembly")
        self.duration = QtWidgets.QSpinBox(self.centralwidget)
        self.duration.setGeometry(QtCore.QRect(730, 560, 80, 30))
        self.duration.setMinimum(1)
        self.duration.setMaximum(10000)
        self.duration.setSingleStep(10)
        self.duration.setProperty("value", 100)
        self.duration.setObjectName("duration")

        #UserCode
        font = QtGui.QFont()
        font.setPointSize(10)
        self.duration.setFont(font)


        self.assemblyEditor = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.assemblyEditor.setGeometry(QtCore.QRect(30, 50, 380, 350))
        self.assemblyEditor.setAcceptDrops(False)
        self.assemblyEditor.setObjectName("assemblyEditor")
        self.assembleButton = QtWidgets.QPushButton(self.centralwidget)
        self.assembleButton.setGeometry(QtCore.QRect(420, 210, 151, 61))
        self.assembleButton.setObjectName("assembleButton")
        
        #UserCode
        font = QtGui.QFont()
        font.setPointSize(13)
        self.assembleButton.setFont(font)


        #UserCode
        font = QtGui.QFont()
        font.setPointSize(13)
        self.assemblyEditor.setFont(font)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(730, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.simulateButton = QtWidgets.QPushButton(self.centralwidget)
        self.simulateButton.setGeometry(QtCore.QRect(620, 560, 93, 28))
        self.simulateButton.setObjectName("simulateButton")

        #UserCode
        font = QtGui.QFont()
        font.setPointSize(11)
        self.simulateButton.setFont(font)


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(730, 540, 80, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.machineCode = QtWidgets.QTextBrowser(self.centralwidget)
        self.machineCode.setGeometry(QtCore.QRect(590, 50, 380, 350))
        self.machineCode.setObjectName("machineCode")

        font = QtGui.QFont()
        font.setPointSize(13)
        self.machineCode.setFont(font)


        self.browsProjects = QtWidgets.QPushButton(self.centralwidget)
        self.browsProjects.setGeometry(QtCore.QRect(50, 510, 41, 31))
        self.browsProjects.setObjectName("browsProjects")
        self.libraryName = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.libraryName.setGeometry(QtCore.QRect(200, 550, 140, 40))
        self.libraryName.setAcceptDrops(False)
        self.libraryName.setObjectName("libraryName")
        self.moduleName = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.moduleName.setGeometry(QtCore.QRect(350, 550, 140, 40))
        self.moduleName.setAcceptDrops(False)
        self.moduleName.setObjectName("moduleName")

        #UserCode
        font = QtGui.QFont()
        font.setPointSize(13)
        self.moduleName.setFont(font)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(99, 510, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(200, 510, 140, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(350, 510, 140, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.projectName = QtWidgets.QTextBrowser(self.centralwidget)
        self.projectName.setGeometry(QtCore.QRect(50, 550, 140, 40))
        self.projectName.setObjectName("projectName")
        #UserCode
        font = QtGui.QFont()
        font.setPointSize(13)
        self.projectName.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ################################################################################################
        #User code
        self.browsAssembly.clicked.connect(self.browsAssemblyClicked)
        self.assembleButton.clicked.connect(self.assembleClicked)
        self.simulateButton.clicked.connect(self.simulateClicked)
        self.browsProjects.clicked.connect(self.browsProjectsClicked)

        self.projectPath = ""
        self.assemblyFilePath = ""
        self.binaryFilePath = ""

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simulator"))
        self.label.setText(_translate("MainWindow", "Assembly"))
        self.browsAssembly.setText(_translate("MainWindow", "Brows"))
        self.assembleButton.setText(_translate("MainWindow", "Assemble >>"))
        self.label_2.setText(_translate("MainWindow", "MachineCode"))
        self.simulateButton.setText(_translate("MainWindow", "Simulate"))
        self.label_3.setText(_translate("MainWindow", "Duration Us"))
        self.browsProjects.setText(_translate("MainWindow", "Brows"))
        self.label_4.setText(_translate("MainWindow", "project"))
        self.label_5.setText(_translate("MainWindow", "Library"))
        self.label_6.setText(_translate("MainWindow", "Module"))
        self.libraryName.setPlainText(_translate("MainWindow", "work"))

        #UserCode
        font = QtGui.QFont()
        font.setPointSize(13)
        self.libraryName.setFont(font)

################################################################################################
#User code
    
    def browsAssemblyClicked(self):
        text = ""
        self.assemblyFilePath, _ = QtWidgets.QFileDialog.getOpenFileName(MainWindow, 'Open File')
        print(self.assemblyFilePath)
        if self.assemblyFilePath: 
            with open(self.assemblyFilePath, 'r') as file:
                text = file.read()
            self.assemblyEditor.setPlainText(text)

        self.binaryFilePath = self.assemblyFilePath[:self.assemblyFilePath.rfind('/') +1] + "binaryInstructions.txt"

    def assembleClicked(self):
        if not self.assemblyFilePath:
            self.assemblyFilePath = os.path.dirname(os.path.abspath(__file__)) + "\\assembly.asm"
            self.binaryFilePath = self.assemblyFilePath[:self.assemblyFilePath.rfind('/') +1] + "binaryInstructions.txt"
            
        
        with open(self.assemblyFilePath, 'w') as asmFile:
            asmFile.write(self.assemblyEditor.toPlainText())

        errorFlag = False
        try:
            Assembler(self.assemblyFilePath,  self.binaryFilePath)
        except:
            errorFlag = True
            print("Syntax error")

        with open (self.binaryFilePath, 'r') as binaryFile:
            self.machineCode.setPlainText(binaryFile.read())
            
        if errorFlag is True:
            count = 0
            with open (self.binaryFilePath, 'r') as binaryFile: 
                for line in binaryFile:
                    count += 1
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("Syntax error at {}".format(int(count /4 +1)))
            error_dialog.exec_()
            # self.assemblyEditor.setPlainText(self.assemblyEditor.toPlainText() +
            #                     "\nSyntax error at {}".format(int(count /4 +1)))




    def browsProjectsClicked(self):
        qfd = QtWidgets.QFileDialog()
        self.projectPath, _ = QtWidgets.QFileDialog.getOpenFileName(qfd, "Brows projects", os.path.dirname(os.path.abspath(__file__)), "Modelsim(*.mpf)")

        name = self.projectPath[self.projectPath.rfind('/') +1: self.projectPath.rfind('.')]
        
        self.projectName.setPlainText(name)
        

    def simulateClicked(self):
        QtWidgets.QApplication.setOverrideCursor(Qt.WaitCursor)

        # library = 'work'
        # moduleName = 'FullAdderTest'
        # vsim -do "project open  D:/Education/University/3rdCSE/CO/Projects/MIPS/Mips/MipsProcessor.mpf; project compileall; vsim Education.FullAdderTest; run; vsim Education.MuxTwoToOneTest; run 5; quit -f" -c
        simulateCommand = 'vsim -do "project open {project}; project compileall; vsim {library}.{module}; run {duration}; quit -f" -c'.format(
            project=self.projectPath, library=self.libraryName.toPlainText(),
            module=self.moduleName.toPlainText(), duration=self.duration.value())
        os.system(simulateCommand)
        
        QtWidgets.QApplication.restoreOverrideCursor()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())