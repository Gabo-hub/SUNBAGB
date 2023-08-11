from db.main_database import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from views.main_windows import Ui_Principal

class PantallaPrint(QMainWindow, Ui_Principal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Variables
        self.fondotexto = ""

        # Manipulación de los eventos click de los Botones
        self.bestudiantes_3.clicked.connect(self.estudiantespantalla)
        self.bprofesores_3.clicked.connect(self.profesorespantalla)
        self.brepresentantes_3.clicked.connect(self.representantespantalla)
        self.pushButton_4.clicked.connect(self.close)
        self.checkBox.clicked.connect(self.modoclaro)
        self.actionRegistro_de_La_Data.triggered.connect(self.añadirdatos)
        
    #Funciones para Los Botones de la pantalla principal
    def añadirdatos(self):
        from controllers.añadirdato import IntroduccionDeDatos
        windows = IntroduccionDeDatos(self)
        windows.show()
    
    def estudiantespantalla(self):
        from controllers.main_estudiantes import Estudiantes
        windows = Estudiantes(self)
        a = QApplication.desktop();
        windows.move((a.width() - windows.width())/ 2, (a.height() - windows.height()) /8);

        
        if not self.checkBox.isChecked():
            windows.setStyleSheet(u"background-color: rgb(51, 54, 57);")
            self.fondotexto = "255, 255, 255"           
        else:
            windows.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.fondotexto = "51, 54, 57"
        for i in windows.txt_cambiarColor:
                #windows.textcedula.setStyleSheet(u"color: rgb("+self.fondotexto+");")
                cadena = "windows."+i+".setStyleSheet(u'color: rgb("+str(self.fondotexto)+");')"
                eval(cadena)        
        windows.show()

    def profesorespantalla(self):
        from controllers.main_profesores import Profesores
        windows = Profesores(self)

        if not self.checkBox.isChecked():
            windows.setStyleSheet(u"background-color: rgb(51, 54, 57);")
            self.fondotexto = "255, 255, 255"           
        else:
            windows.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.fondotexto = "51, 54, 57"
        for i in windows.txt_cambiarColor:
                #windows.textcedula.setStyleSheet(u"color: rgb("+self.fondotexto+");")
                cadena = "windows."+i+".setStyleSheet(u'color: rgb("+str(self.fondotexto)+");')"
                eval(cadena)
        windows.show()

    def representantespantalla(self):
        from controllers.main_representantes import Representantes
        windows1 = Representantes(self)
        #windows1.setGeometry((xancho-830)/2,(yalto-960)/8,830,960)
        a = QApplication.desktop();
        windows1.move((a.width() - windows1.width())/ 2, (a.height() - windows1.height()) /8);

        
        
        
        if not self.checkBox.isChecked():
            windows1.setStyleSheet(u"background-color: rgb(51, 54, 57);")
            self.fondotexto = "255, 255, 255"           
        else:
            windows1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.fondotexto = "51, 54, 57"
        for i in windows1.objetos:
                #windows.textcedula.setStyleSheet(u"color: rgb("+self.fondotexto+");")
                cadena = "windows1."+i+".setStyleSheet(u'color: rgb("+str(self.fondotexto)+");')"
                eval(cadena)
        windows1.show()

    def modoclaro(self):
        if self.checkBox.isChecked():
            #Activar modo Blanco
            self.setStyleSheet(u"background-color: rgb(255, 255, 255);")
            self.label_6.setStyleSheet(u"color: rgb(51, 54, 57);")
            self.label_7.setStyleSheet(u"color: rgb(51, 54, 57);")
            self.labelestudiantes_3.setStyleSheet(u"color: rgb(51, 54, 57);")
            

            self.fondotexto = "51, 54, 57"
        else:
            #Volver al negro
            self.setStyleSheet(u"background-color: rgb(51, 54, 57);")
            self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
            self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
            self.labelestudiantes_3.setStyleSheet(u"color: rgb(255, 255, 255);")

            self.fondotexto = "255, 255, 255"
