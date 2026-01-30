from assets.suplementos import Suplementos
from controllers.alerta import MensajeCaja
from db.main_database import *
from PySide6.QtCore import *
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from views.añadirdato import Ui_AnadirDatos


class IntroduccionDeDatos(QWidget, Ui_AnadirDatos):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        self.manager = conectarse() # DatabaseManager instance
        self.suplemento = Suplementos()

        # Cargar datos iniciales en ComboBoxes
        self._cargar_combos()

        # Etiquetas para cambio de color (modo claro/oscuro)
        self.txt_cambiarColor = [
            # Estudiantes
            self.ql_Ebasededatos, self.ql_Eingresarinfo, self.ql_EcedulaText, 
            self.ql_EnombreText, self.ql_EapellidoText, self.ql_EsexoText, 
            self.ql_EedadText, self.ql_EfnacimientoText, self.ql_ElnacimientoText, 
            self.ql_EestadoText, self.ql_EdireccionText, self.ql_EobservacionesText, 
            self.ql_ErepresentanteText, self.ql_EparentescoText, self.ql_EgradoseccionText,
            self.label_17, self.label_18, self.label_2,
            # Representantes
            self.ql_Rbasededatos, self.ql_Ringresarinfo, self.ql_RnombreText, 
            self.ql_RapellidoText, self.ql_RcedulaText, self.ql_RntelefonoText, 
            self.ql_RdireccionText, self.ql_RdirecciontrabText, self.ql_RobservacionesText, 
            self.ql_RestadolabText, self.ql_RtotalrepreText,
            self.label_16, self.label_15, self.label_19,
            # Profesores
            self.ql_Pbasededatos, self.ql_Pingresarinfo, self.ql_PnombreText, 
            self.ql_PapellidoText, self.ql_PcedulaText, self.ql_PsexoText, 
            self.ql_PfnacimientoText, self.ql_PanosserviText, self.ql_PcodcargoText, 
            self.ql_PcoddepenText, self.ql_PntelefonoText, self.ql_PgradodocText,
            self.label_13, self.label_14, self.label_20
        ]
        # Frames para cambio de fondo (modo claro/oscuro)
        self.bg_cambiarColor = [
            self.frame_10, self.frame_12, self.frame_5, self.frame_8, 
            self.frame, self.frame_6
        ]
        
        # Conectar botones
        self.bttn_Eguardar.clicked.connect(self.estudiantes_save)
        self.bttn_Rguardar.clicked.connect(self.representantes_save)
        self.bttn_Pguardar.clicked.connect(self.profesores_save)
        
        # Conectar botones de salida/limpiar (mejorar ergonomía)
        self.bttn_Psalir.clicked.connect(self.close)
        self.bttn_Esalir.clicked.connect(self.close)
        self.bttn_Rsalir.clicked.connect(self.close)

    def _cargar_combos(self):
        """Carga los comboboxes de forma segura usando UserData para los IDs."""
        tablas = {
            "representantes_v": self.comboBox,
            "public.estados": self.cbox_EestadoInfo,
            "public.parentesco": self.cbox_EparentescoInfo,
            "public.grados": self.cbox_Egradoseccion
        }
        
        for tabla, combo in tablas.items():
            combo.clear()
            # Si es representantes_v (vista), los campos son id y nombre
            query = f"SELECT * FROM {tabla}"
            if "estados" in tabla or "parentesco" in tabla:
                query += " ORDER BY 1 ASC"
            
            datos = self.manager.consultar(query, fetch_all=True) or []
            for item in datos:
                # item[0] es ID, item[1] es Nombre/Descripción
                combo.addItem(str(item[1]), item[0])

    def _convertir_fecha(self, fecha_str):
        """Convierte DD/MM/YYYY a YYYY-MM-DD para PostgreSQL."""
        try:
            partes = fecha_str.split("/")
            if len(partes) == 3:
                return f"{partes[2]}-{partes[1]}-{partes[0]}"
            return fecha_str # Devolver original si no tiene el formato esperado
        except Exception:
            return None

    # =========================================================================
    # ESTUDIANTES
    # =========================================================================
    def estudiantes_save(self):
        cedula = self.qlinee_EcedulaInfo.text().strip()
        if not cedula:
            return MensajeCaja(self, "ERROR", "La cédula es obligatoria", 1)

        fecha_db = self._convertir_fecha(self.qlinee_EfnacimientoInfo.text())
        
        # Recolectar datos
        datos = {
            "cedula": cedula,
            "psnombres": self.qlinee_EnombreInfo.text().upper(),
            "psapellidos": self.qlinee_EapellidosInfo.text().upper(),
            "sexo": self.qlinee_EsexoInfo.text(),
            "edad": self.qlinee_EedadInfo.text(),
            "fnacimiento": fecha_db,
            "lnacimiento": self.qlinee_ElnacimientoInfo.text(),
            "idestado": self.cbox_EestadoInfo.currentData(),
            "direccion": self.qlinee_EdireccionInfo.text(),
            "observaciones": self.qlinee_EobservacionesInfo.text(),
            "idrepresentante": self.comboBox.currentData(),
            "parentesco": self.cbox_EparentescoInfo.currentData(),
            "grado": self.cbox_Egradoseccion.currentData()
        }

        # Validar campos críticos
        if not all([datos["psnombres"], datos["psapellidos"], datos["idrepresentante"]]):
            return MensajeCaja(self, "ERROR", "Faltan campos obligatorios", 1)

        # Verificar si existe
        existe = self.manager.consultar("SELECT idestud FROM estudiantes WHERE cedula = %s", (cedula,))
        
        if not existe:
            query = """
                INSERT INTO estudiantes (cedula, psnombres, psapellidos, sexo, edad, fnacimiento, 
                                       lnacimiento, idestado, direccion, observaciones, 
                                       idrepresentante, parentesco, grado)
                VALUES (%(cedula)s, %(psnombres)s, %(psapellidos)s, %(sexo)s, %(edad)s, %(fnacimiento)s,
                        %(lnacimiento)s, %(idestado)s, %(direccion)s, %(observaciones)s, 
                        %(idrepresentante)s, %(parentesco)s, %(grado)s)
            """
            self.manager.ejecutar(query, datos)
            MensajeCaja(self, "ÉXITO", "Estudiante guardado correctamente", 1)
        else:
            query = """
                UPDATE estudiantes SET 
                    psnombres=%(psnombres)s, psapellidos=%(psapellidos)s, sexo=%(sexo)s, 
                    edad=%(edad)s, fnacimiento=%(fnacimiento)s, lnacimiento=%(lnacimiento)s, 
                    idestado=%(idestado)s, direccion=%(direccion)s, observaciones=%(observaciones)s, 
                    idrepresentante=%(idrepresentante)s, parentesco=%(parentesco)s, grado=%(grado)s
                WHERE cedula = %(cedula)s
            """
            self.manager.ejecutar(query, datos)
            MensajeCaja(self, "ÉXITO", "Estudiante actualizado correctamente", 1)

    # =========================================================================
    # REPRESENTANTES
    # =========================================================================
    def representantes_save(self):
        cedula = self.qlinee_RcedulaInfo.text().strip()
        if not cedula:
            return MensajeCaja(self, "ERROR", "La cédula es obligatoria", 1)

        datos = {
            "nrepresentante": self.qlinee_RnombreInfo.text().upper(),
            "arepresentante": self.qlinee_RapellidosInfo.text().upper(),
            "cedularepre": cedula,
            "ntelefonico": self.qlinee_RntelefonoInfo.text(),
            "ndireccion": self.qlinee_Rdireccioninfo.text(),
            "ndirecciontrabajo": self.qlinee_RdirecciontrabInfo.text(),
            "nobservaciones": self.qlinee_RobservacionesInfo.text(),
            "estadolaboral": self.qlinee_estadolabInfo.text(),
            "nrepresentados": int(self.qlinee_RtotalrepreInfo.text() or 0)
        }

        existe = self.manager.consultar("SELECT idrepresentante FROM representantes WHERE cedularepre = %s", (cedula,))
        
        if not existe:
            query = """
                INSERT INTO representantes (nrepresentante, arepresentante, cedularepre, ntelefonico, 
                                          ndireccion, ndirecciontrabajo, nobservaciones, estadolaboral, nrepresentados)
                VALUES (%(nrepresentante)s, %(arepresentante)s, %(cedularepre)s, %(ntelefonico)s, 
                        %(ndireccion)s, %(ndirecciontrabajo)s, %(nobservaciones)s, %(estadolaboral)s, %(nrepresentados)s)
            """
            self.manager.ejecutar(query, datos)
            MensajeCaja(self, "ÉXITO", "Representante guardado correctamente", 1)
        else:
            query = """
                UPDATE representantes SET 
                    nrepresentante=%(nrepresentante)s, arepresentante=%(arepresentante)s, 
                    ntelefonico=%(ntelefonico)s, ndireccion=%(ndireccion)s, 
                    ndirecciontrabajo=%(ndirecciontrabajo)s, nobservaciones=%(nobservaciones)s, 
                    estadolaboral=%(estadolaboral)s, nrepresentados=%(nrepresentados)s
                WHERE cedularepre = %(cedularepre)s
            """
            self.manager.ejecutar(query, datos)
            MensajeCaja(self, "ÉXITO", "Representante actualizado correctamente", 1)
        
        self._cargar_combos() # Actualizar lista de representantes para el combo de estudiantes

    # =========================================================================
    # PROFESORES
    # =========================================================================
    def profesores_save(self):
        cedula = self.qlinee_PcedulaInfo.text().strip()
        if not cedula:
            return MensajeCaja(self, "ERROR", "La cédula es obligatoria", 1)

        datos = {
            "pnombres": self.qlinee_PnombreInfo.text().upper(),
            "papellidos": self.qlinee_PapellidosInfo.text().upper(),
            "pcedula": cedula,
            "psexo": self.qlinee_PsexoInfo.text(),
            "fnacimiento": self.qlinee_PfnacimientoInfo.text(),
            "pañosservi": int(self.qlinee_PanosserviInfo.text() or 0),
            "pcodecargo": self.qlinee_PcodcargoInfo.text(),
            "pcodedepen": self.qlinee_PcoddepenInfo.text(),
            "ptelefono": self.qlinee_PntelefonoInfo.text(),
            "pgrado": self.qcbox_PgradodocInfo.currentText()
        }

        existe = self.manager.consultar("SELECT pides FROM profesores WHERE pcedula = %s", (cedula,))
        
        if not existe:
            query = """
                INSERT INTO profesores (pnombres, papellidos, pcedula, psexo, fnacimiento, 
                                      "pañosservi", pcodecargo, pcodedepen, ptelefono, pgrado)
                VALUES (%(pnombres)s, %(papellidos)s, %(pcedula)s, %(psexo)s, %(fnacimiento)s, 
                        %(pañosservi)s, %(pcodecargo)s, %(pcodedepen)s, %(ptelefono)s, %(pgrado)s)
            """
            self.manager.ejecutar(query, datos)
            MensajeCaja(self, "ÉXITO", "Docente guardado correctamente", 1)
        else:
            query = """
                UPDATE profesores SET 
                    pnombres=%(pnombres)s, papellidos=%(papellidos)s, psexo=%(psexo)s, 
                    fnacimiento=%(fnacimiento)s, "pañosservi"=%(pañosservi)s, 
                    pcodecargo=%(pcodecargo)s, pcodedepen=%(pcodedepen)s, 
                    ptelefono=%(ptelefono)s, pgrado=%(pgrado)s
                WHERE pcedula = %(pcedula)s
            """
            self.manager.ejecutar(query, datos)
            MensajeCaja(self, "ÉXITO", "Docente actualizado correctamente", 1)


