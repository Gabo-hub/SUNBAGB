from assets.suplementos import Suplementos
from db.main_database import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import QWidget
from views.main_representantes import Ui_Representantes


class Representantes(QWidget, Ui_Representantes):


    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

         #Variables
        self.suplemento = Suplementos()
        self.xtexto = self.bttn_Rbuscar.clicked.connect(self.search_info_representante) #BOTON DE BUSQUEDA
        self.conector = conectarse()
        
        # Creación de lista para cambiar de color los objestos de la vista Representante
        self.objetos = ["ql_RnombresText","ql_RapellidosText","ql_RcedulaText","ql_RntelefonoText","ql_RdireccionText","ql_RtotalrepreText","ql_RparentescoText","ql_RestadoLabText","ql_RdireccionTrabText","ql_RobservacionesText"]
        self.objimprimir = ["qlinee_RcedulaInfo.text()","qlinee_RnombresInfo.text()","qlinee_RapellidosInfo.text()","qlinee_RntelefonoInfo.text()","qlinee_RtotalrepreInfo.text()","qlinee_RparentescoInfo.text()","qlinee_RestadolabInfo.text()","qpte_RdireccionInfo.toPlainText()","qpte_RdirecciontrabajoInfo.toPlainText()","qpte_RobservacionesInfo.toPlainText()"]
        self.setearInformacion = ["self.qlinee_RnombresInfo.setText(","self.qlinee_RapellidosInfo.setText(","self.qlinee_RcedulaInfo.setText(","self.qlinee_RntelefonoInfo.setText(","self.qpte_RdireccionInfo.setPlainText(","self.qpte_RdirecciontrabajoInfo.setPlainText(","self.qpte_RobservacionesInfo.setPlainText(","self.qlinee_RestadolabInfo.setText(","self.qlinee_RtotalrepreInfo.setText(","self.qlinee_RparentescoInfo.setText("]

        #Eventos botones
        self.bttnRsalir.clicked.connect(self.close) #Boton de Salir
        self.bttn_Rimprimir.clicked.connect(self.imprimir_funcion) #Boton de Imprimir

    def search_info_representante(self):
        xcadena=""
        global xbusqueda
        xbusqueda="0"
        if len(self.qlinee_RnombreSearch.text()) != 0:
            xbusqueda = self.qlinee_RnombreSearch.text().upper()
            xcadena = """SELECT idrepresentante, nrepresentante, arepresentante, cedularepre, ntelefonico, 
		ndireccion, ndirecciontrabajo, nobservaciones, estadolaboral,nrepresentados,
		(SELECT descripcion FROM parentesco WHERE parentesco.idparentesco=(SELECT parentesco FROM estudiantes WHERE estudiantes.idestud=idrepresentante))
		FROM public.representantes WHERE representantes.nrepresentante||' '||representantes.arepresentante LIKE '%"""+str(xbusqueda)+"%' FETCH FIRST 1 ROW ONLY"
        
        elif len(self.qlinee_RcedulaSearch.text()) != 0:
            xbusqueda = self.qlinee_RcedulaSearch.text()
            xcadena = """SELECT idrepresentante, nrepresentante, arepresentante, cedularepre, ntelefonico, 
		ndireccion, ndirecciontrabajo, nobservaciones, estadolaboral,nrepresentados,
		(SELECT descripcion FROM parentesco WHERE parentesco.idparentesco=(SELECT parentesco FROM estudiantes WHERE estudiantes.idestud=idrepresentante))
		FROM public.representantes WHERE cedularepre='"""+str(xbusqueda)+"'"
        
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

    def ventanaError(self):
        from controllers.alerta import MensajeCaja
        self.ayuda = MensajeCaja(self,"ERROR DE VALIDACIÓN",f"El dato ingresado {xbusqueda} no fue encontrado. Ingrese un dato válido",1)

    def imprimir_funcion(self):
        from controllers.imprimir import Imprimir
        
        self.listaimprimir = []
        if len(self.qlinee_RcedulaInfo.displayText()) != 0:
            for i in self.objimprimir:
                self.cadena = "self."+i
                self.listaimprimir.append(eval(self.cadena))
                self.StrA = "".join(self.listaimprimir)

            self.portada = "U.E.N.B. ANTONIO GUZMÁN BLANCO"
            self.titulo = "INFORMACIÓN DEL REPRESENTANTE"
            self.imagenfoot = "./assets/icons/escuelaicon.jpg"
            self.footer = "PANTALLA DE IMPRESIÓN U.E.N.B ANTONIO GUZMAN BLANCO"
            self.body = [self.ql_RcedulaText.text(),self.listaimprimir[0],self.ql_RnombresText.text(),self.listaimprimir[1],self.ql_RapellidosText.text(),self.listaimprimir[2],self.ql_RntelefonoText.text(),self.listaimprimir[3],self.ql_RtotalrepreText.text(),self.listaimprimir[4],self.ql_RparentescoText.text(),self.listaimprimir[5],self.ql_RestadoLabText.text(),self.listaimprimir[6],self.ql_RdireccionText.text(),self.listaimprimir[7],self.ql_RdireccionTrabText.text(),self.listaimprimir[8],self.ql_RobservacionesText.text(),self.listaimprimir[9]]
            Imprimir(self.suplemento.imprimir_profesores(self.portada, self.titulo, self.body, self.imagenfoot, self.footer))
        else:
            return
            #.format(
            #     self.textcedula.text(), self.listaimprimir[2],
            #     self.textnombre.text(), self.listaimprimir[0],
            #     self.textapellido.text(), self.listaimprimir[1],
            #     self.texttelefono.text(), self.listaimprimir[3],
            #     self.textodireccion.text(), self.listaimprimir[4],
            #     self.textotalrepre.text(), self.listaimprimir[5],
            #     self.textparentesco.text(), self.listaimprimir[6],
            #     self.textestadoLab.text(), self.listaimprimir[7],
            #     self.textdirecciontrabajo.text(), self.listaimprimir[8],
            #     self.textobservaciones.text(), self.listaimprimir[9]
            # )
