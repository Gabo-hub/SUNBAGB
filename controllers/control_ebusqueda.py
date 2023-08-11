from views.ebusqueda import Ui_eBusqueda
from PySide2.QtWidgets import QDialog,QTableWidgetItem
from PySide2.QtGui import *
from PySide2.QtCore import *
from db.main_database import *


class ControlBusqueda(QDialog, Ui_eBusqueda):
    # Definir la señal que se dispara al finalizar la selección
    alFinal = Signal(int)

    def __init__(self,parent=None):
        # INVOCA AL CONSTRUCTOR DE LA CLASE PADRE
        super().__init__(parent)
        self.setupUi(self)
        # DEFINE ALGUNOS ATRIBUTOS PARA EL NUEVO OBJETO
        self.setWindowFlag(Qt.Window)
        icon = QIcon()
        icon.addFile(u":/logo_ipasme/icons/IPASME-logo-DABC2AE9B1-seeklogo.com.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.resultado=0
        # CARGAR VALORES AL OBJETO QTABLETWIDGET DESDE LA BASE DE DATOS
                # VALIDACION DE DATOS
        self.Validador = QRegExpValidator(QRegExp("[1-9]\\d{0,10}"),self)
        self.txtNumeracion.setValidator(self.Validador)
        self.Validador = QRegExpValidator(QRegExp("[A-Za-z áéíóú]*"),self)
        self.txtCategoria.setValidator(self.Validador)
        
        # CARGAR LOS GRADOS EN EL COMBO BOX
        
        v_grados = """SELECT idgrado, nomgrado FROM public.grados;"""
        self.conectar = conectarse()
        self.consulta_grados = consultaestados(self.conectar, v_grados)
        
        self.cbox_grado.addItem("")
        self.cbox_grado.setItemText(0, QCoreApplication.translate("AnadirDatos", "VISTA GENERAL", None))
        for x in self.consulta_grados:
            self.cbox_grado.addItem("")
            self.cbox_grado.setItemText(
                x[0], QCoreApplication.translate("AnadirDatos", str(x[1]), None))
        
        # ACTIVAR EL EVENTO DE CAMBIO DE TEXTO EN EL LINEEDIT IDENTIFICADOR
        self.cbox_grado.currentIndexChanged.connect(self.ubicar)
        self.txtNumeracion.textChanged.connect(self.filtrar)
        self.txtNumeracion.returnPressed.connect(self.tblBusqueda.setFocus)
        self.txtCategoria.textChanged.connect(self.filtrar)
        self.txtCategoria.returnPressed.connect(self.tblBusqueda.setFocus)
        self.btnSalir.clicked.connect(self.close)
        self.tblBusqueda.doubleClicked.connect(self.seleccionar)
        self.tblBusqueda.activated.connect(self.seleccionar) 
        self.finished.connect(self.finalizar)

        self.show()
        
    def ubicar(self):
        self.seleccion = self.cbox_grado.currentIndex()
        if self.seleccion == 0:
            self.tblBusqueda.clearContents()
            self.conTabla("SELECT cedula,psnombres FROM estudiantes", "CEDULA", "NOMBRE")
        else:
            self.tblBusqueda.clearContents()
            self.conTabla(f"SELECT cedula,psnombres FROM estudiantes WHERE grado={self.seleccion}", "CEDULA", "NOMBRE")
# Define la cadena para cargar los datos en la Clase
    def conTabla(self,xtabla,xColumna1,xColumna2):
        self.listaDatos=xtabla
        self.conector = conectarse()
        self.cargarinfo = cargarestudiantes(self.conector, self.listaDatos)
        if self.cargarinfo == None: 
            return
        self.listadoC= dict(self.cargarinfo)
        self.lblColumna1.setText(" "+xColumna1+" ")
        self.lblColumna2.setText(" "+xColumna2+" ")
        self.tblBusqueda.horizontalHeaderItem(0).setText(" "+xColumna1+" ")
        self.tblBusqueda.horizontalHeaderItem(1).setText(" "+xColumna2+" ")
        
        # Devuelve los valores de la consulta en listas separadas
        self.claves=list(self.listadoC.keys())
        self.valores = list(self.listadoC.values())
        self.combinar= [(str(self.claves[i]), self.valores[i]) for i in range(0, len(self.claves))] 

        # Colocamos los datos en la tabla    
        for i in range(len(self.claves)):
            self.claves[i]=str(self.claves[i])
            self.tblBusqueda.setItem(i,0,QTableWidgetItem(self.claves[i]))
            self.tblBusqueda.setItem(i,1,QTableWidgetItem(self.valores[i]))
            self.txtNumeracion.setFocus()
        
        
    # Funcion que emite el valor final de la selección
    def finalizar(self):
        #x=(self.tblBusqueda.item(self.tblBusqueda.currentRow(),0).text())
        #self.alFinal.emit(x)    
        try:
            x=int((self.tblBusqueda.item(self.tblBusqueda.currentRow(),0).text()))
            #print (x)
            self.alFinal.emit(x)  
        except:
            self.alFinal.emit(0)  
        #return x

    def filtrar(self):
        filtro=[]
        self.xcolumn=0
        if self.txtNumeracion.hasFocus():    #COLOCA UNA CONDICION  QUE SIRVA
           self.xcolumn=0
        elif self.txtCategoria.hasFocus():
            self.xcolumn=1
        # Definir que columna de verifica 
        if self.xcolumn==0:
            self.txtCategoria.setText("")
            for i in range(len(self.combinar)):
                if self.txtNumeracion.text() in self.combinar[i][self.xcolumn]:
                    filtro.append(self.combinar[i])
        else:
            self.txtNumeracion.setText("")
            self.txtCategoria.setText(self.txtCategoria.text().upper())
            for i in range(len(self.combinar)):
                if self.txtCategoria.text().upper() in self.combinar[i][self.xcolumn]:
                    filtro.append(self.combinar[i])
        self.tblBusqueda.clearContents()
        for i in range(len(filtro)):
            self.tblBusqueda.setItem(i,0,QTableWidgetItem(filtro[i][0]))
            self.tblBusqueda.setItem(i,1,QTableWidgetItem(filtro[i][1]))
        
    def seleccionar(self):
        self.resultado = (self.tblBusqueda.item(self.tblBusqueda.currentRow(),0).text())
        self.close()
    
