import calendar
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from datetime import datetime
from PySide6.QtPrintSupport import *

from controllers.control_ebusqueda import ControlBusqueda
from views.main_estudiantes import Ui_Estudiantes
from db.main_database import *
from assets.suplementos import Suplementos


class Estudiantes(QWidget, Ui_Estudiantes):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        self.bttn_guardar.hide()
        self.bttn_cancelar.hide()
        self.ql_cancelarText.hide()
        self.ql_guardarText.hide()


        # Manipulación del evento click de los botones
        self.bttn_Ebuscar.clicked.connect(self.search_new_file_table)  # BOTON DE BUSQUEDA
        self.manager = conectarse() # Ahora es un DatabaseManager
        self.bttn_Erimprimir.clicked.connect(self.imprimir_funcion)  # Imprimir boton
        self.bttn_Esalir.clicked.connect(self.close)  # Salir boton
        self.bttn_verestudiantes.clicked.connect(self.verEstudiantes)
        self.bttn_editar.clicked.connect(self.editarInfo)
        self.bttn_guardar.clicked.connect(self.guardarEdit)
        self.bttn_cancelar.clicked.connect(self.cancelarEdit)
        self.bttn_Erefrescar.clicked.connect(lambda: self.cbox_EestadoInfo.setCurrentIndex(-1))
        self.bttn_Erefrescar.clicked.connect(lambda: self.cbox_EestadoInfo.setCurrentIndex(-1))
        self.bttn_Erefrescar.clicked.connect(lambda: self.cbox_Egradoseccion.setCurrentIndex(-1))
        self.bttn_notas.clicked.connect(self.abrir_modal_notas)
        self.bttn_carnet.clicked.connect(self.abrir_modal_carnet)

        # Cargar datos en ComboBox
        self.cargar_combos()

        # Mapeo de campos para evitar eval()
        self.mapeo_informacion = {
            "cedula": self.qlinee_EcedulaInfo,
            "nombres": self.qlinee_EnombresInfo,
            "apellidos": self.qlinee_EapellidosInfo,
            "sexo": self.qlinee_EsexoInfo,
            "edad": self.qlinee_EedadInfo,
            "fnacimiento": self.qlinee_EfnacimientoInfo,
            "lnacimiento": self.qlinee_ElnacimientoInfo,
            "estado": self.cbox_EestadoInfo,
            "direccion": self.qpte_EdireccionInfo,
            "observaciones": self.qpte_EobservacionesInfo,
            "representante": self.qlinee_ErepresentanteInfo,
            "telefono": self.qlinee_EntelefonicoInfo,
            "parentesco": self.qlinee_EparentescoInfo,
            "grado": self.cbox_Egradoseccion
        }

        # Etiquetas para cambio de color (modo claro/oscuro)
        self.txt_cambiarColor = [
            self.ql_EcedulaText, self.ql_EnombresText, self.ql_EapellidosText, self.ql_EsexoText, 
            self.ql_EedadText, self.ql_EfnacimientoText, self.ql_EestadosText, self.ql_ElnacimientoText, 
            self.ql_ErepresentanteText, self.ql_EparentescoText, self.ql_EntelefonicoText, 
            self.ql_EdireccionText, self.ql_EtobservacionText, self.ql_EgradoseccionText, self.ql_EsalirText, self.ql_EimprimirText, self.ql_ErefrescarText,
            self.ql_EbuscarbaseText, self.ql_EnombreSearch, self.ql_EcedulaSearch, self.bttn_verestudiantes, self.ql_notasText, self.label, self.ql_carnetText
        ]
        # Frames para cambio de fondo (modo claro/oscuro)
        self.bg_cambiarColor = [
            self.headframe, self.footerframe
        ]

    # Ventana de Error de Busqueda
    def ventanaError(self, dato=""):
        from controllers.alerta import MensajeCaja
        self.ayuda = MensajeCaja(self, "ERROR DE VALIDACIÓN",
                                 f"El dato '{dato}' no fue encontrado. Ingrese un dato válido", 1)

    def editarError(self, dato=""):
        from controllers.alerta import MensajeCaja
        self.ayuda = MensajeCaja(self, "ERROR DE VALIDACIÓN", 
                                 f"Para editar la información del estudiante, debe de seleccionar uno", 1)
    
    # Ventana de Ver todos los estudiantes    
    def verEstudiantes(self):
        from controllers.control_ebusqueda import ControlBusqueda
        windows = ControlBusqueda(self)
        if hasattr(self.parent(), '_aplicar_tema'):
            self.parent()._aplicar_tema(windows)
        windows.conTabla("SELECT cedula, psnombres FROM estudiantes", "CEDULA", "NOMBRE")
        windows.alFinal.connect(self.funResultado)
        windows.show()
        
    def funResultado(self, xresultado):
        if xresultado != 0:
            self.qlinee_EcedulaSearch.setText(str(xresultado))
            self.search_new_file_table()
    
    # Funcion para Imprimir datos de busqueda
    def imprimir_funcion(self):
        from controllers.imprimir import Imprimir
        if not self.qlinee_EcedulaInfo.text():
            return

        portada = "U.E.N.B. ANTONIO GUZMÁN BLANCO"
        titulo = "INFORMACIÓN DEL ESTUDIANTE"
        imagenfoot = "./assets/icons/escuelaicon.jpg"
        footer = "PANTALLA DE IMPRESIÓN U.E.N.B ANTONIO GUZMAN BLANCO"

        # Obtener valores de la UI
        valores = [widget.text() if hasattr(widget, 'text') else widget.toPlainText() 
                  for widget in self.mapeo_informacion.values()]
        
        body = []
        labels = [
            "Cédula", "Nombres", "Apellidos", "Sexo", "Edad", "F. Nacimiento", 
            "L. Nacimiento", "Estado", "Dirección", "Observaciones", 
            "Representante", "Teléfono", "Parentesco", "Grado"
        ]
        
        for i, label in enumerate(labels):
            body.append(label)
            body.append(valores[i])

        # Usar suplementos para generar el reporte
        from assets.suplementos import Suplementos
        suplemento = Suplementos()
        Imprimir(suplemento.imprimir_estudiantes(portada, titulo, body, imagenfoot, footer))

    # Funcion para la Busqueda de datos
    def search_new_file_table(self):
        query = ""
        params = ()

        nombre_search = self.qlinee_EnombreSearch.text().strip()
        cedula_search = self.qlinee_EcedulaSearch.text().strip()

        base_query = """
            SELECT idestud, cedula, psnombres, psapellidos, sexo, edad, fnacimiento, lnacimiento,
            (SELECT nombre FROM estados WHERE estados.idestados = estudiantes.idestado),
            direccion, observaciones,
            (SELECT nrepresentante || ' ' || arepresentante FROM representantes WHERE representantes.idrepresentante = estudiantes.idrepresentante),
            (SELECT ntelefonico FROM representantes WHERE representantes.idrepresentante = estudiantes.idrepresentante),
            (SELECT descripcion FROM parentesco WHERE parentesco.idparentesco = estudiantes.parentesco),
            (SELECT nomgrado FROM grados WHERE idgrado = grado)
            FROM public.estudiantes
        """

        if nombre_search:
            query = base_query + " WHERE psnombres || ' ' || psapellidos ILIKE %s FETCH FIRST 1 ROW ONLY"
            params = (f"%{nombre_search}%",)
        elif cedula_search:
            query = base_query + " WHERE cedula = %s"
            params = (cedula_search,)

        if query:
            resultado = self.manager.consultar(query, params)
            print(resultado)
            if resultado:
                self.current_idestud = resultado[0]
                # Mapeo de resultados a widgets
                widgets_ordenados = list(self.mapeo_informacion.values())
                # El resultado trae idestud at index 0, saltamos ese
                for i, valor in enumerate(resultado[1:]):
                    widget = widgets_ordenados[i]
                    val_str = str(valor) if valor is not None else ""
                    
                    if i == 5 and valor: # Fecha de nacimiento (index 6 en query, index 5 aqui)
                        val_str = valor.strftime("%d/%m/%Y")
                    
                    if hasattr(widget, 'setText'):
                        widget.setText(val_str)
                    elif hasattr(widget, 'setPlainText'):
                        widget.setPlainText(val_str)
                    elif hasattr(widget, 'setCurrentText'):
                        widget.setCurrentText(val_str)
            else:
                self.ventanaError(nombre_search or cedula_search)
        else:
            self.ventanaError("Vacío")

    def cancelarEdit(self):

        for widget in self.mapeo_informacion.values():
            if hasattr(widget, 'setReadOnly'):
                widget.setReadOnly(True)
            elif hasattr(widget, 'setEnabled'):
                widget.setEnabled(False)

        self.search_new_file_table()
        
        self.bttn_editar.show()
        self.label.show()
        self.bttn_Erefrescar.show()
        self.ql_ErefrescarText.show()
        self.bttn_Erimprimir.show()
        self.ql_EimprimirText.show()
        self.bttn_Esalir.show()
        self.ql_EsalirText.show()
        
        self.bttn_cancelar.hide()
        self.ql_cancelarText.hide()
        self.bttn_guardar.hide()
        self.ql_guardarText.hide()

    def editarInfo(self):
        # Obtener valores de la UI de forma robusta
        valores = []
        for widget in self.mapeo_informacion.values():
            if hasattr(widget, 'text'):
                valores.append(widget.text())
            elif hasattr(widget, 'currentText'):
                valores.append(widget.currentText())
            elif hasattr(widget, 'toPlainText'):
                valores.append(widget.toPlainText())
            else:
                valores.append("")
        
        if valores[0] == "" and valores[1] == "":
            self.editarError()
            return

        try:
            for widget in self.mapeo_informacion.values():
                if hasattr(widget, 'setReadOnly'):
                    widget.setReadOnly(False)
                elif hasattr(widget, 'setEnabled'):
                    widget.setEnabled(True)

            self.bttn_guardar.show()
            self.bttn_cancelar.show()
            self.ql_cancelarText.show()
            self.ql_guardarText.show()

            self.bttn_notas.hide()
            self.ql_notasText.hide()
            self.bttn_editar.hide()
            self.label.hide()
            self.bttn_Erefrescar.hide()
            self.ql_ErefrescarText.hide()
            self.bttn_Erimprimir.hide()
            self.ql_EimprimirText.hide()
            self.bttn_Esalir.hide()
            self.ql_EsalirText.hide()
        except Exception as e:
            print(e)

    def guardarEdit(self):
        from datetime import datetime
        if not hasattr(self, 'current_idestud') or not self.current_idestud:
            from controllers.alerta import MensajeCaja
            MensajeCaja(self, "ERROR", "No hay un estudiante seleccionado para editar", 1)
            return

        # Obtener valores del mapeo
        datos = {}
        for key, widget in self.mapeo_informacion.items():
            if hasattr(widget, 'text'):
                datos[key] = widget.text().strip()
            elif hasattr(widget, 'toPlainText'):
                datos[key] = widget.toPlainText().strip()
            elif hasattr(widget, 'currentText'):
                datos[key] = widget.currentText().strip()

        try:
            # Convertir fecha si existe
            fecha_nac = None
            if datos.get("fnacimiento"):
                try:
                    fecha_nac = datetime.strptime(datos["fnacimiento"], "%d/%m/%Y").date()
                except ValueError:
                    # Si falla, intentamos pasar el string tal cual o None
                    fecha_nac = None

            # Query de actualización
            query = """
                UPDATE public.estudiantes SET
                cedula = %s, psnombres = %s, psapellidos = %s, sexo = %s, edad = %s, 
                fnacimiento = %s, lnacimiento = %s,
                idestado = (SELECT idestados FROM estados WHERE nombre = %s),
                direccion = %s, observaciones = %s,
                parentesco = (SELECT idparentesco FROM parentesco WHERE descripcion = %s),
                grado = (SELECT idgrado FROM grados WHERE nomgrado = %s)
                WHERE idestud = %s
            """
            params = (
                datos["cedula"], datos["nombres"], datos["apellidos"], datos["sexo"], datos["edad"],
                fecha_nac, datos["lnacimiento"], datos["estado"],
                datos["direccion"], datos["observaciones"],
                datos["parentesco"], datos["grado"],
                self.current_idestud
            )
            
            if self.manager.ejecutar(query, params):
                from controllers.alerta import MensajeCaja
                MensajeCaja(self, "ÉXITO", "Información actualizada correctamente", 1)
                self.cancelarEdit()
            else:
                from controllers.alerta import MensajeCaja
                MensajeCaja(self, "ERROR", "No se pudo actualizar la información en la base de datos", 1)

        except Exception as e:
            print(f"Error en guardarEdit: {e}")
            from controllers.alerta import MensajeCaja
            MensajeCaja(self, "ERROR CRÍTICO", str(e), 1)

    def cargar_combos(self):
        try:
            # Estados
            # Usamos fetch_all=True para obtener todos los registros
            res_estados = self.manager.consultar("SELECT idestados, nombre FROM estados ORDER BY nombre ASC", fetch_all=True)
            if res_estados:
                self.cbox_EestadoInfo.clear()
                for item in res_estados:
                    self.cbox_EestadoInfo.addItem(str(item[1]), item[0])
                
            # Grados
            res_grados = self.manager.consultar("SELECT idgrado, nomgrado FROM grados ORDER BY idgrado ASC", fetch_all=True)
            if res_grados:
                self.cbox_Egradoseccion.clear()
                for item in res_grados:
                    self.cbox_Egradoseccion.addItem(str(item[1]), item[0])
                
            self.cbox_EestadoInfo.setEnabled(False)
            self.cbox_Egradoseccion.setEnabled(False)
        except Exception as e:
            print(f"Error cargando combos en Estudiantes: {e}")

    def abrir_modal_notas(self):
        if not hasattr(self, 'current_idestud') or not self.current_idestud:
            from controllers.alerta import MensajeCaja
            MensajeCaja(self, "ADVERTENCIA", "Seleccione un estudiante primero", 1)
            return

        from controllers.modal_notas import ModalNotas
        # Construir nombre completo
        nombre_completo = f"{self.qlinee_EnombresInfo.text()} {self.qlinee_EapellidosInfo.text()}"
        
        modal = ModalNotas(self, self.current_idestud, nombre_completo)
        
        # Aplicar tema si es posible
        if hasattr(self.parent(), '_aplicar_tema'):
             self.parent()._aplicar_tema(modal)
             
        modal.exec()

    def abrir_modal_carnet(self):
        if not hasattr(self, 'current_idestud') or not self.current_idestud:
            from controllers.alerta import MensajeCaja
            MensajeCaja(self, "ADVERTENCIA", "Seleccione un estudiante primero", 1)
            return

        from controllers.modal_carnet import ModalCarnet
        
        datos_estudiante = {
            "cedula": self.qlinee_EcedulaInfo.text(),
            "nombres": self.qlinee_EnombresInfo.text(),
            "apellidos": self.qlinee_EapellidosInfo.text(),
            "grado": self.cbox_Egradoseccion.currentText(),
            "idestud": self.current_idestud
        }
        
        modal = ModalCarnet(self, datos_estudiante)
        
        if hasattr(self.parent(), '_aplicar_tema'):
             self.parent()._aplicar_tema(modal)
             
        modal.exec()
