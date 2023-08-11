from assets.suplementos import Suplementos
from controllers.alerta import MensajeCaja
from db.main_database import *
from PySide2.QtCore import *
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget
from views.añadirdato import Ui_AnadirDatos


class IntroduccionDeDatos(QWidget, Ui_AnadirDatos):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        #################################### VARIABLES ####################################
        v_representantes = """SELECT * FROM representantes_v;"""
        v_estados = """SELECT * FROM public.estados ORDER BY idestados ASC;"""
        v_parentesco = """SELECT * FROM public.parentesco ORDER BY idparentesco ASC;"""
        v_grados = """SELECT idgrado, nomgrado FROM public.grados;"""

        self.conectar = conectarse()
        self.consulta_repre = consultarvista(self.conectar, v_representantes)
        self.consulta_estados = consultaestados(self.conectar, v_estados)
        self.consulta_grados = consultaestados(self.conectar, v_grados)
        self.consulta_parentesco = consultaparentesco(self.conectar, v_parentesco)
        
        self.bttn_Eguardar.clicked.connect(self.estudiantes_save)
        self.bttn_Rguardar.clicked.connect(self.representantes_save)
        self.bttn_Pguardar.clicked.connect(self.profesores_save)
        #################################### COMBO BOX #########################################
        print(self.consulta_repre)
        for x in self.consulta_repre:
            self.comboBox.addItem("")
            self.comboBox.setItemText(
                x[0] - 1, QCoreApplication.translate("AnadirDatos", str(x[1]), None))

        for x in self.consulta_estados:
            self.cbox_EestadoInfo.addItem("")
            self.cbox_EestadoInfo.setItemText(
                x[0] - 1, QCoreApplication.translate("AnadirDatos", str(x[1]), None))

        for x in self.consulta_parentesco:
            self.cbox_EparentescoInfo.addItem("")
            self.cbox_EparentescoInfo.setItemText(
                x[0] - 1, QCoreApplication.translate("AnadirDatos", str(x[1]), None))
        
        for x in self.consulta_grados:
            self.cbox_Egradoseccion.addItem("")
            self.cbox_Egradoseccion.setItemText(
                x[0] - 1, QCoreApplication.translate("AnadirDatos", str(x[1]), None))
            
    #FUNCIONES########################## ESTUDIANTES ####################################
    def estudiantes_save(self):

        fech = self.qlinee_EfnacimientoInfo.text()
        fech2 = fech.split("/")
        fechacambio = fech2[2]+"-"+fech2[1]+"-"+fech2[0]
        self.E_guardarinfo = ["qlinee_EcedulaInfo.text()", "qlinee_EnombreInfo.text().upper()", "qlinee_EapellidosInfo.text().upper()", "qlinee_EsexoInfo.text()", "qlinee_EedadInfo.text()",
                              f"{fechacambio}", "qlinee_ElnacimientoInfo.text()", "cbox_EestadoInfo.currentIndex() + 1", "qlinee_EdireccionInfo.text()", "qlinee_EobservacionesInfo.text()", "comboBox.currentIndex() + 1", "cbox_EparentescoInfo.currentIndex() + 1","cbox_Egradoseccion.currentIndex() + 1"]
        self.listaguardar = []

        if len(self.qlinee_EcedulaInfo.text()) == 0 or len(self.qlinee_ElnacimientoInfo.text()) == 0 or len(self.qlinee_EdireccionInfo.text()) == 0:
            return MensajeCaja(self, "ERROR INFORMACION INCOMPLETA", "POR FAVOR, RELLENE LOS CAMPOS VACIOS", 1)

        for i in self.E_guardarinfo:
            if i != fechacambio:
                self.cadena = "self."+i
                self.listaguardar.append(eval(self.cadena))
            else:
                self.listaguardar.append(str(fechacambio))

        self.holacomoestas = consultaidstud(
            self.conectar, f"""select exists(select 1 from public.estudiantes where cedula='{self.listaguardar[0]}')""")
        try:
            if self.holacomoestas[0][0] == False:
                MensajeCaja(self, "INFORMACION GUARDADA",
                            "La informacion ha sido guardada con exito", 1)

                xGuardarEstudiantes = f"""INSERT INTO public.estudiantes(cedula, psnombres, psapellidos, sexo, edad, fnacimiento,lnacimiento, idestado, direccion, observaciones, idrepresentante, parentesco, grado)
                VALUES ({self.listaguardar[0]},'{self.listaguardar[1]}', 
                '{self.listaguardar[2]}','{self.listaguardar[3]}','{self.listaguardar[4]}','{self.listaguardar[5]}','{self.listaguardar[6]}', {self.listaguardar[7]}, 
                '{self.listaguardar[8]}','{self.listaguardar[9]}', {self.listaguardar[10]}, {self.listaguardar[11]}, {self.listaguardar[12]});"""

                self.guardando = guardardb(self.conectar, xGuardarEstudiantes)
                self.conectar.connection.commit()

            else:
                MensajeCaja(self, "INFORMACION GUARDADA", "La informacion ha sido actualizada con exito ", 1)
                
                v_idstud = """SELECT idestud, cedula FROM public.estudiantes WHERE cedula='"""+self.listaguardar[0]+"'"
                self.consulta_idstud = actualizarinfo(self.conectar, v_idstud)
                
                xGuardarEstudiantes = f"""UPDATE public.estudiantes SET cedula={self.listaguardar[0]}, 
                psnombres='{self.listaguardar[1]}', psapellidos='{self.listaguardar[2]}', 
                sexo='{self.listaguardar[3]}', edad='{self.listaguardar[4]}', 
                fnacimiento='{self.listaguardar[5]}', lnacimiento='{self.listaguardar[6]}', 
                idestado={self.listaguardar[7]}, direccion='{self.listaguardar[8]}', 
                observaciones='{self.listaguardar[9]}', idrepresentante={self.listaguardar[10]}, 
                parentesco={self.listaguardar[11]}, grado={self.listaguardar[12]} WHERE estudiantes.idestud={self.consulta_idstud[0][0]};"""

                self.guardando = guardardb(self.conectar, xGuardarEstudiantes)
                self.conectar.connection.commit()
        except NameError:
            print(NameError)
    #FUNCIONES########################## REPRESENTANTES ####################################
    def representantes_save(self):
        self.E_guardarinfo = ['qlinee_RnombreInfo.text().upper()','qlinee_RapellidosInfo.text().upper()','qlinee_RcedulaInfo.text()','qlinee_RntelefonoInfo.text()','qlinee_Rdireccioninfo.text()','qlinee_RdirecciontrabInfo.text()','qlinee_RobservacionesInfo.text()','qlinee_estadolabInfo.text()','qlinee_RtotalrepreInfo.text()']
        self.listaguardar = []

        if len(self.qlinee_RcedulaInfo.text()) == 0 or len(self.qlinee_Rdireccioninfo.text()) == 0 or len(self.ql_RdirecciontrabText.text()) == 0:
            return MensajeCaja(self, "ERROR INFORMACION INCOMPLETA", "POR FAVOR, RELLENE LOS CAMPOS VACIOS", 1)

        for i in self.E_guardarinfo:
                self.cadena = "self."+i
                self.listaguardar.append(eval(self.cadena))

        self.holacomoestas = consultaidstud(
            self.conectar, f"""select exists(select 1 from public.representantes where cedularepre='{self.listaguardar[2]}')""")
        
        try:
            if self.holacomoestas[0][0] == False:
                MensajeCaja(self, "INFORMACION GUARDADA",
                            "La informacion ha sido guardada con exito", 1)

                xGuardarEstudiantes = f"""INSERT INTO public.representantes(
	            nrepresentante, arepresentante, cedularepre, ntelefonico, ndireccion, ndirecciontrabajo, nobservaciones, estadolaboral, nrepresentados)
	            VALUES ('{self.listaguardar[0]}','{self.listaguardar[1]}', 
                '{self.listaguardar[2]}','{self.listaguardar[3]}','{self.listaguardar[4]}','{self.listaguardar[5]}','{self.listaguardar[6]}', '{self.listaguardar[7]}', 
                {int(self.listaguardar[8])});"""

                self.guardando = guardardb(self.conectar, xGuardarEstudiantes)
                self.conectar.connection.commit()
            else:
                MensajeCaja(self, "INFORMACION GUARDADA", "La informacion ha sido actualizada con exito ", 1)
                
                v_idrepre = """SELECT idrepresentante, cedularepre FROM public.representantes WHERE cedularepre='"""+self.listaguardar[2]+"'"
                self.consulta_idrepre = actualizarinfo(self.conectar, v_idrepre)
                
                xGuardarEstudiantes = f"""UPDATE public.representantes
	            SET nrepresentante='{self.listaguardar[0]}', arepresentante='{self.listaguardar[1]}',
                cedularepre='{self.listaguardar[2]}', ntelefonico='{self.listaguardar[3]}', ndireccion='{self.listaguardar[4]}', 
                ndirecciontrabajo='{self.listaguardar[5]}', nobservaciones='{self.listaguardar[6]}', 
                estadolaboral='{self.listaguardar[7]}', nrepresentados={int(self.listaguardar[8])}
	            WHERE representantes.idrepresentante={self.consulta_idrepre[0][0]};"""

                self.guardando = guardardb(self.conectar, xGuardarEstudiantes)
                self.conectar.connection.commit()
        except NameError:
            print(NameError)
    #FUNCIONES########################## PROFESORES ####################################
    def profesores_save(self):
        self.E_guardarinfo = ["qlinee_PnombreInfo.text().upper()","qlinee_PapellidosInfo.text().upper()","qlinee_PcedulaInfo.text()","qlinee_PsexoInfo.text()","qlinee_PfnacimientoInfo.text()","qlinee_PanosserviInfo.text()","qlinee_PcodcargoInfo.text()","qlinee_PcoddepenInfo.text()","qlinee_PntelefonoInfo.text()","qcbox_PgradodocInfo.currentText()"]
        self.listaguardar = []

        if len(self.qlinee_PcedulaInfo.text()) == 0 or len(self.qlinee_PcodcargoInfo.text()) == 0 or len(self.qlinee_PnombreInfo.text()) == 0:
            return MensajeCaja(self, "ERROR INFORMACION INCOMPLETA", "POR FAVOR, RELLENE LOS CAMPOS VACIOS", 1)

        for i in self.E_guardarinfo:
                self.cadena = "self."+i
                self.listaguardar.append(eval(self.cadena))

        self.holacomoestas = consultaidstud(
            self.conectar, f"""select exists(select 1 from public.profesores where pcedula='{self.listaguardar[2]}')""")
        
        try:
            if self.holacomoestas[0][0] == False:
                MensajeCaja(self, "INFORMACION GUARDADA",
                            "La informacion ha sido guardada con exito", 1)

                xGuardarEstudiantes = f"""INSERT INTO public.profesores(
	            pnombres, papellidos, pcedula, psexo, fnacimiento, "pañosservi", pcodecargo, pcodedepen, ptelefono, pgrado)
	            VALUES ('{self.listaguardar[0]}', '{self.listaguardar[1]}', {self.listaguardar[2]}, 
                        '{self.listaguardar[3]}', '{self.listaguardar[4]}', {self.listaguardar[5]},
                        '{self.listaguardar[6]}', '{self.listaguardar[7]}', '{self.listaguardar[8]}', '{self.listaguardar[9]}');"""

                self.guardando = guardardb(self.conectar, xGuardarEstudiantes)
                self.conectar.connection.commit()

            else:
                MensajeCaja(self, "INFORMACION GUARDADA", "La informacion ha sido actualizada con exito ", 1)
                
                v_idprofe = """SELECT pides, pcedula FROM public.profesores WHERE pcedula='"""+self.listaguardar[2]+"'"
                self.consulta_idprofe = actualizarinfo(self.conectar, v_idprofe)
                
                xGuardarEstudiantes = f"""UPDATE public.profesores SET pnombres='{self.listaguardar[0]}', 
                papellidos='{self.listaguardar[1]}', pcedula={self.listaguardar[2]}, psexo='{self.listaguardar[3]}', 
                fnacimiento='{self.listaguardar[4]}', "pañosservi"={self.listaguardar[5]}, 
                pcodecargo='{self.listaguardar[6]}', pcodedepen='{self.listaguardar[7]}', 
                ptelefono='{self.listaguardar[8]}', pgrado='{self.listaguardar[9]}'
	            WHERE profesores.pides={self.consulta_idprofe[0][0]};"""

                self.guardando = guardardb(self.conectar, xGuardarEstudiantes)
                self.conectar.connection.commit()
        except NameError:
            print(NameError)           


