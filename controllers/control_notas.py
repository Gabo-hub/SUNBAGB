from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Qt
from db.main_database import conectarse

class ControlNotas(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.manager = conectarse()
        # Nota: Aquí se cargaría una interfaz UI_Notas similar a las otras
        # Por ahora implementamos la lógica de negocio central
        
    def registrar_nota(self, id_estud, id_materia, id_lapso, calificacion):
        """Registra o actualiza una nota para un estudiante."""
        if not (0 <= calificacion <= 20):
            return False, "La calificación debe estar entre 0 y 20"
            
        query = """
            INSERT INTO public.notas (idestud, idmateria, idlapso, calificacion)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (idestud, idmateria, idlapso) 
            DO UPDATE SET calificacion = EXCLUDED.calificacion, fecha_registro = CURRENT_TIMESTAMP
        """
        # Nota: Para el ON CONFLICT, se requeriría un índice único en la DB
        # CREATE UNIQUE INDEX idx_notas_estud_materia_lapso ON public.notas(idestud, idmateria, idlapso);
        
        success = self.manager.ejecutar(query, (id_estud, id_materia, id_lapso, calificacion))
        return success, "Nota registrada exitosamente" if success else "Error al registrar nota"

    def consultar_notas_estudiante(self, id_estud):
        """Obtiene todas las notas de un estudiante con nombres de materia y lapso."""
        query = """
            SELECT m.nombre_materia, l.nombre_lapso, n.calificacion, n.fecha_registro
            FROM public.notas n
            JOIN public.materias m ON n.idmateria = m.idmateria
            JOIN public.lapsos l ON n.idlapso = l.idlapso
            WHERE n.idestud = %s
            ORDER BY l.idlapso, m.nombre_materia
        """
        return self.manager.consultar(query, (id_estud,), fetch_all=True)

    def obtener_promedio_estudiante(self, id_estud, id_lapso=None):
        """Calcula el promedio de un estudiante, opcionalmente por lapso."""
        query = "SELECT AVG(calificacion) FROM public.notas WHERE idestud = %s"
        params = [id_estud]
        
        if id_lapso:
            query += " AND idlapso = %s"
            params.append(id_lapso)
            
        result = self.manager.consultar(query, tuple(params))
        return float(result[0]) if result and result[0] is not None else 0.0
