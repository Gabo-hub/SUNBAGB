from assets.suplementos import Suplementos
from db.main_database import *
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget
from views.main_profesores import Ui_Profesores


class Profesores(QWidget, Ui_Profesores):


    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        # Manipulación del evento click del botones
        self.xtexto = self.bttn_busqueda.clicked.connect(self.search_file_profesores) #BOTON DE BUSQUEDA
        self.conector = conectarse()
        self.bttn_imprimir.clicked.connect(self.imprimir_funcion)

        #Variables
        self.suplemento = Suplementos()
        self.txt_cambiarColor = ["ql_nombreText","ql_apellidoText","ql_cedulaText","ql_sexoText","ql_fnacimientoText","ql_telefonoText","ql_gradodocText","ql_anosServiciosText","ql_codcargoText","ql_codigodepenText"]
        self.objimprimir = ["qlinee_cedulaInfo.text()","qlinee_nombreInfo.text()","qlinee_apellidoInfo.text()","qlinee_sexoInfo.text()","qlinee_fnacimientoinfo.text()","qlinee_telefonoInfo.text()","qlinee_gradodocInfo.text()","qlinee_anosServiciosText.text()","qlinee_codcargoInfo.text()","qlinee_coddepenInfo.text()"]
        self.setearInformacion = ["self.qlinee_nombreInfo.setText(","self.qlinee_apellidoInfo.setText(","self.qlinee_cedulaInfo.setText(","self.qlinee_sexoInfo.setText(","self.qlinee_fnacimientoinfo.setText(","self.qlinee_anosServiciosText.setText(","self.qlinee_codcargoInfo.setText(","self.qlinee_coddepenInfo.setText(","self.qlinee_telefonoInfo.setText(","self.qlinee_gradodocInfo.setText("]

    
    #Ventana de Error de Busqueda
    def ventanaError(self):
        from controllers.alerta import MensajeCaja
        self.ayuda = MensajeCaja(self, "ERROR DE VALIDACI\u00d3N", f"El dato ingresado {xbusqueda} no fue encontrado. Ingrese un dato v\u00e1lido", 1)
        
    #Funcion para Imprimir datos de busqueda
    def imprimir_funcion(self):
        from controllers.imprimir import Imprimir
        
        self.listaimprimir = []
        if len(self.qlinee_cedulaInfo.text()) != 0:
            for i in self.objimprimir:
                self.cadena = "self."+i
                self.listaimprimir.append(eval(self.cadena))
                self.StrA = "".join(self.listaimprimir)

            self.portada = "U.E.N.B. ANTONIO GUZMÁN BLANCO"
            self.titulo = "INFORMACIÓN DEL DOCENTE"
            self.imagenfoot = "./assets/icons/escuelaicon.jpg"
            self.footer = "PANTALLA DE IMPRESIÓN U.E.N.B ANTONIO GUZMAN BLANCO"
            self.body = [self.ql_cedulaText.text(),self.listaimprimir[0],self.ql_nombreText.text(),self.listaimprimir[1],self.ql_apellidoText.text(),self.listaimprimir[2],self.ql_sexoText.text(),self.listaimprimir[3],self.ql_fnacimientoText.text(),self.listaimprimir[4],self.ql_telefonoText.text(),self.listaimprimir[5],self.ql_gradodocText.text(),self.listaimprimir[6],self.ql_anosServiciosText.text(),self.listaimprimir[7],self.ql_codcargoText.text(),self.listaimprimir[8],self.ql_codigodepenText.text(),self.listaimprimir[9]]
            Imprimir(self.suplemento.imprimir_profesores(self.portada, self.titulo, self.body, self.imagenfoot, self.footer))
        else:
            return

    #Funcion para la Busqueda de datos
    def search_file_profesores(self):
        xcadena=""
        global xbusqueda
        xbusqueda="0"
        if len(self.qlinee_nombreSearch.text()) != 0:
            xbusqueda = self.qlinee_nombreSearch.text().upper()
            xcadena= """SELECT pides, pnombres, papellidos, pcedula, psexo, fnacimiento, "pañosservi", pcodecargo, pcodedepen, ptelefono, pgrado
	                    FROM public.profesores WHERE pnombres||' '||papellidos LIKE '%"""+str(xbusqueda)+"%' FETCH FIRST 1 ROW ONLY"
        elif len(self.qlinee_cedulaSearch.text()) != 0:
            xbusqueda = self.qlinee_cedulaSearch.text()
            xcadena= """SELECT pides, pnombres, papellidos, pcedula, psexo, fnacimiento, "pañosservi", pcodecargo, pcodedepen, ptelefono, pgrado
	                    FROM public.profesores WHERE pcedula="""+str(xbusqueda)
        if xcadena != "":
            self.resultado = consultardb(self.conector, xcadena) 

            if self.resultado != None:
                for i in range(len(self.resultado)-1):
                    self.prueba2 = self.setearInformacion[i]+"str(self.resultado[i+1]))"
                    eval(self.prueba2)
            else:
                self.ventanaError()
        else:
            self.ventanaError()
