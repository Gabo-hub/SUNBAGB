
from PySide6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt
from views.modal_notas import Ui_ModalNotas
from db.main_database import conectarse
from controllers.alerta import MensajeCaja

class ModalNotas(QDialog, Ui_ModalNotas):
    def __init__(self, parent=None, student_id=None, student_name=""):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        
        self.manager = conectarse()
        self.student_id = student_id
        self.label_estudiante_val.setText(student_name)
        
        # Conexiones
        self.bttn_guardar.clicked.connect(self.guardar_nota)
        self.bttn_cerrar.clicked.connect(self.close)
        
        if self.student_id:
            self.cargar_notas()
            
        # Cargar Grados desde BD
        self.cargar_grados()
        
        # Lista de widgets para aplicar tema si es necesario (compatible con main_windows)
        self.bg_cambiarColor = [self.frame_header, self.frame_info, self.frame_form, self.frame_footer]
        self.txt_cambiarColor = [
            self.label_titulo, self.label_estudiante, self.label_estudiante_val,
            self.label_anio, self.label_nota, self.label_obs
        ]
        
    def cargar_grados(self):
        try:
            self.cbox_grado.clear()
            # Asumiendo que manager es conectarse() -> DatabaseManager
            # Y que tiene consultar(query, fetch_all=True)
            # Ordenamos por idgrado para mantener 1er, 2do...
            query = "SELECT nomgrado FROM grados ORDER BY idgrado ASC"
            grados = self.manager.consultar(query, fetch_all=True)
            
            if grados:
                for (nombre,) in grados:
                    self.cbox_grado.addItem(nombre)
        except Exception as e:
            print(f"Error cargando grados: {e}")
            self.cbox_grado.addItem("Error cargando grados")

    def cargar_notas(self):
        self.table_notas.setRowCount(0)
        query = "SELECT año_escolar, grado, seccion, calificacion, observacion FROM notas_finales WHERE idestud = %s ORDER BY año_escolar DESC"
        notas = self.manager.consultar(query, (self.student_id,), fetch_all=True) or []
        
        for i, (anio, grado, seccion, nota, obs) in enumerate(notas):
            self.table_notas.insertRow(i)
            self.table_notas.setItem(i, 0, QTableWidgetItem(str(anio)))
            self.table_notas.setItem(i, 1, QTableWidgetItem(str(grado or "")))
            self.table_notas.setItem(i, 2, QTableWidgetItem(str(seccion or "")))
            self.table_notas.setItem(i, 3, QTableWidgetItem(str(nota)))
            self.table_notas.setItem(i, 4, QTableWidgetItem(str(obs or "")))
            
            self.table_notas.item(i, 0).setTextAlignment(Qt.AlignCenter)
            self.table_notas.item(i, 1).setTextAlignment(Qt.AlignCenter)
            self.table_notas.item(i, 2).setTextAlignment(Qt.AlignCenter)
            self.table_notas.item(i, 3).setTextAlignment(Qt.AlignCenter)

    def guardar_nota(self):
        anio = self.qlinee_anio.text().strip()
        grado_seccion_str = self.cbox_grado.currentText()
        
        # Separar Grado y Sección (Asumimos formato "X Grado Y")
        # El formato es "1er Grado A", split por último espacio
        parts = grado_seccion_str.rsplit(' ', 1)
        if len(parts) == 2:
            grado = parts[0]
            seccion = parts[1]
        else:
            # Fallback por si acaso
            grado = grado_seccion_str
            seccion = ""

        nota = self.cbox_nota.currentText()
        obs = self.qpte_obs.toPlainText().strip()
        
        if not anio:
            return MensajeCaja(self, "ERROR", "Debe ingresar el año escolar", 1)
            
        try:
            query = """
                INSERT INTO notas_finales (idestud, año_escolar, grado, seccion, calificacion, observacion, fecha_registro)
                VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP)
                ON CONFLICT (idestud, año_escolar) 
                DO UPDATE SET 
                    grado = EXCLUDED.grado,
                    seccion = EXCLUDED.seccion,
                    calificacion = EXCLUDED.calificacion, 
                    observacion = EXCLUDED.observacion,
                    fecha_registro = CURRENT_TIMESTAMP
            """
            params = (self.student_id, anio, grado, seccion, nota, obs)
            
            if self.manager.ejecutar(query, params):
                MensajeCaja(self, "ÉXITO", "Nota registrada correctamente", 1)
                self.cargar_notas()
                self.qlinee_anio.clear()
                self.qpte_obs.clear()
            else:
                MensajeCaja(self, "ERROR", "No se pudo registrar la nota", 1)
                
        except Exception as e:
            MensajeCaja(self, "ERROR", str(e), 1)
