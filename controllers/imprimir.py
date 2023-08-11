from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtPrintSupport import *
from PySide2.QtWidgets import QWidget
from views.imprimirpage import Ui_Form
from views.main_estudiantes import Ui_Estudiantes


class Imprimir(QWidget, Ui_Form, Ui_Estudiantes):    
    def __init__(self, textoimprimir):
        super().__init__() 
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.paraimprimir.setHtml(textoimprimir)

        self.printer = QPrinter(QPrinter.HighResolution)
        self.prueba = QPrintPreviewWidget(self.printer, self)
        self.prueba.setZoomMode(QPrintPreviewWidget.ZoomMode.FitInView)
        self.previewDialog = QPrintPreviewDialog(self.printer, self)
        self.previewDialog.paintRequested.connect(self.print_preview)
        self.previewDialog.setWindowTitle("Ventana de Impresión")
        #self.previewDialog.setOrientation()
        self.previewDialog.exec_()
 
    def print_preview(self, printer):
        self.paraimprimir.print_(printer)
    