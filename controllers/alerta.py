from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import *
from PySide6.QtCore import *

msg = QMessageBox()

def MensajeCaja(self,titulo,texto,tipo): 
    self.tipo=tipo
    self.msg = QMessageBox(self)
    icon = QIcon()
    icon.addFile(u"./assets/icons/Webp.net-resizeimage.png", QSize(), QIcon.Normal, QIcon.Off)
    self.msg.setWindowTitle(titulo)
    self.msg.setText(texto)
    self.msg.setStyleSheet(u"background-color: rgb(85, 90, 95); color: rgb(255, 255, 255);")
    
    if self.tipo == 1:
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.setIcon(QMessageBox.Information) 
    elif self.tipo == 2:
        self.msg.setIcon(QMessageBox.Question)  
        self.msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

    self.msg.setWindowIcon(icon)
    #self.msg.setStyleSheet("background-color: rgb(223, 223, 223);")
    #self.msg.setStyleSheet("background-color: rgb(240, 240, 240); \n QMessageBox{\n color:rgb(255, 255, 255); \n background-color: rgb(71, 93, 144);}")
    
    respuestaMensaje=self.msg.exec_()

    if respuestaMensaje==QMessageBox.Yes:
        return 1  
    else:
        return 2