from calendar import c
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from datetime import datetime
from PySide2.QtPrintSupport import *

from controllers.control_ebusqueda import ControlBusqueda
from views.main_estudiantes import Ui_Estudiantes
from db.main_database import *
from assets.suplementos import Suplementos


class Estudiantes(QWidget, Ui_Estudiantes):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        # Manipulación del evento click del botones
        self.xtexto = self.bttn_Ebuscar.clicked.connect(self.search_new_file_table)  # BOTON DE BUSQUEDA
        self.conector = conectarse()
        self.bttn_Erimprimir.clicked.connect(self.imprimir_funcion)  # Imprimir boton
        self.bttn_Esalir.clicked.connect(self.close)  # Salir boton
        self.bttn_verestudiantes.clicked.connect(self.verEstudiantes)

        # Listas
        self.txt_cambiarColor = ["ql_EcedulaText", "ql_EnombresText", "ql_EapellidosText", "ql_EsexoText", "ql_EedadText", "ql_EfnacimientoText", "ql_EestadosText",
            "ql_ElnacimientoText", "ql_ErepresentanteText", "ql_EparentescoText", "ql_EntelefonicoText", "ql_EdireccionText", "ql_EtobservacionText", "ql_EgradoseccionText"]
        self.objetosImprimir = ["qlinee_EcedulaInfo.text()", "qlinee_EnombresInfo.text()", "qlinee_EapellidosInfo.text()", "qlinee_EsexoInfo.text()", "qlinee_EedadInfo.text()", "qlinee_EfnacimientoInfo.text()", "qlinee_EestadoInfo.text()",
                                                         "qlinee_ElnacimientoInfo.text()", "qlinee_ErepresentanteInfo.text()", "qlinee_EparentescoInfo.text()", "qlinee_EntelefonicoInfo.text()", "qpte_EdireccionInfo.toPlainText()", "qpte_EobservacionesInfo.toPlainText()", "ql_EgradoseccionInfo.text()"]
        self.setearInformacion = ["qlinee_EcedulaInfo.setText(", "qlinee_EnombresInfo.setText(", "qlinee_EapellidosInfo.setText(", "qlinee_EsexoInfo.setText(", "qlinee_EedadInfo.setText(", "qlinee_EfnacimientoInfo.setText(", "qlinee_ElnacimientoInfo.setText(",
                                                              "qlinee_EestadoInfo.setText(", "qpte_EdireccionInfo.setPlainText(", "qpte_EobservacionesInfo.setPlainText(", "qlinee_ErepresentanteInfo.setText(", "qlinee_EntelefonicoInfo.setText(", "qlinee_EparentescoInfo.setText(", "ql_EgradoseccionInfo.setText("]


    # Ventana de Error de Busqueda
    def ventanaError(self):
        from controllers.alerta import MensajeCaja
        self.ayuda = MensajeCaja(self, "ERROR DE VALIDACI\u00d3N",
                                 f"El dato ingresado {xbusqueda} no fue encontrado. Ingrese un dato v\u00e1lido", 1)
    
    # Ventana de Ver todos los estudiantes    
    def verEstudiantes(self):
        from controllers.control_ebusqueda import ControlBusqueda
        windows = ControlBusqueda(self)
        windows.conTabla("SELECT cedula,psnombres FROM estudiantes", "CEDULA", "NOMBRE")
        windows.alFinal.connect(self.funResultado)
        
    def funResultado(self,xresultado):
        if xresultado!=0:
            self.qlinee_EcedulaSearch.setText(str(xresultado))
            self.search_new_file_table()
        else:
            pass
    
    # Funcion para Imprimir datos de busqueda
    def imprimir_funcion(self):
        from controllers.imprimir import Imprimir
        self.listaimprimir = []
        if len(self.qlinee_EcedulaInfo.text()) != 0:
            for i in self.objetosImprimir:
                self.xcadena = "self."+i
                self.listaimprimir.append(eval(self.xcadena))
                self.StrA = "".join(self.listaimprimir)
            self.portada = "U.E.N.B. ANTONIO GUZMÁN BLANCO"
            self.titulo = "INFORMACIÓN DEL ESTUDIANTE"
            self.imagenfoot = "./assets/icons/escuelaicon.jpg"
            self.footer = "PANTALLA DE IMPRESIÓN U.E.N.B ANTONIO GUZMAN BLANCO"
            self.body = [self.ql_EcedulaText.text(), self.listaimprimir[0], self.ql_EnombresText.text(), self.listaimprimir[1], self.ql_EapellidosText.text(), self.listaimprimir[2], self.ql_EsexoText.text(), self.listaimprimir[3], self.ql_EedadText.text(), self.listaimprimir[4], self.ql_EfnacimientoText.text(), self.listaimprimir[5], self.ql_EestadosText.text(), self.listaimprimir[6], self.ql_ElnacimientoText.text(
            ), self.listaimprimir[7], self.ql_ErepresentanteText.text(), self.listaimprimir[8], self.ql_EparentescoText.text(), self.listaimprimir[9], self.ql_EntelefonicoText.text(), self.listaimprimir[10], self.ql_EgradoseccionText.text(), self.listaimprimir[13], self.ql_EdireccionText.text(), self.listaimprimir[11], self.ql_EtobservacionText.text(), self.listaimprimir[12]]
            Imprimir(self.suplemento.imprimir_estudiantes(
                self.portada, self.titulo, self.body, self.imagenfoot, self.footer))
        else:
            return

    # Funcion para la Busqueda de datos
    def search_new_file_table(self):

        xcadena= ''
        global xbusqueda
        xbusqueda = "0"

        if len(self.qlinee_EnombreSearch.text()) != 0:

            xbusqueda = self.qlinee_EnombreSearch.text()
            xcadena = """SELECT idestud, cedula, psnombres, psapellidos, sexo, edad, fnacimiento, lnacimiento,
            (SELECT nombre FROM estados Where estados.idestados=estudiantes.idestado), direccion, observaciones,
            (SELECT nrepresentante ||' '|| arepresentante AS nrepresentante FROM representantes WHERE representantes.idrepresentante=estudiantes.idrepresentante),
            (SELECT ntelefonico FROM representantes WHERE representantes.idrepresentante=estudiantes.idrepresentante),
            (SELECT descripcion FROM parentesco WHERE parentesco.idparentesco=estudiantes.parentesco), (SELECT nomgrado FROM grados WHERE idgrado=grado)
			FROM public.estudiantes WHERE estudiantes.psnombres||' '||estudiantes.psapellidos LIKE '%"""+str(xbusqueda)+"%' FETCH FIRST 1 ROW ONLY"

        elif len(self.qlinee_EcedulaSearch.text()) != 0:

            xbusqueda = self.qlinee_EcedulaSearch.text()
            xcadena = """SELECT idestud, cedula, psnombres, psapellidos, sexo, edad, fnacimiento, lnacimiento,
            ( SELECT nombre FROM estados Where estados.idestados=estudiantes.idestado), direccion, observaciones,
            (SELECT nrepresentante ||' '|| arepresentante AS nrepresentante FROM representantes
            WHERE representantes.idrepresentante=estudiantes.idrepresentante),
            (SELECT ntelefonico FROM representantes WHERE representantes.idrepresentante=estudiantes.idrepresentante),
            (SELECT descripcion FROM parentesco WHERE parentesco.idparentesco=estudiantes.parentesco), (SELECT nomgrado FROM grados WHERE idgrado=grado) FROM public.estudiantes WHERE cedula='"""+str(xbusqueda)+"'"
        
        if xcadena != "":
            self.resultado = consultardb(self.conector, xcadena)
            if self.resultado != None:
                for i in range(len(self.resultado)-1):
                    self.prueba2 = "self." + \
                        self.setearInformacion[i]+"str(self.resultado[i+1]))"
                    eval(self.prueba2)
                fecha = self.resultado[6].strftime("%d %m %Y")
                self.qlinee_EfnacimientoInfo.setText(fecha)
            else:
                self.ventanaError()
        else:
            self.ventanaError()
