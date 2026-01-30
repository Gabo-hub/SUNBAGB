from assets.suplementos import Suplementos
from db.main_database import *
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from views.main_profesores import Ui_Profesores


class Profesores(QWidget, Ui_Profesores):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        # Manipulación del evento click de los botones
        self.bttn_busqueda.clicked.connect(self.search_file_profesores) #BOTON DE BUSQUEDA
        self.bttn_verprofesores.clicked.connect(self.verProfesores) # BOTON VER LISTA
        self.bttn_editar.clicked.connect(self.editarInfo)
        self.manager = conectarse()
        self.bttn_imprimir.clicked.connect(self.imprimir_funcion)

        # Cargar datos en ComboBox
        self.cargar_combos()

        # Conectar nuevos botones
        self.bttn_guardar.clicked.connect(self.guardarEdit)
        self.bttn_cancelar.clicked.connect(self.cancelarEdit)
        self.bttn_refrescar.clicked.connect(lambda: self.cbox_gradodocInfo.setCurrentIndex(-1))
        
        # Ocultar botones de edición por defecto
        self.bttn_guardar.hide()
        self.ql_guardarText.hide()
        self.bttn_cancelar.hide()
        self.ql_cancelarText.hide()

        # Variables
        self.current_idprof = None
        self.suplemento = Suplementos()
        
        # Mapeo de campos para evitar eval()
        self.mapeo_informacion = {
            "nombres": self.qlinee_nombreInfo,
            "apellidos": self.qlinee_apellidoInfo,
            "cedula": self.qlinee_cedulaInfo,
            "sexo": self.qlinee_sexoInfo,
            "fnacimiento": self.qlinee_fnacimientoinfo,
            "anos_servicio": self.qlinee_anosServiciosText,
            "cod_cargo": self.qlinee_codcargoInfo,
            "cod_depen": self.qlinee_coddepenInfo,
            "telefono": self.qlinee_telefonoInfo,
            "grado": self.cbox_gradodocInfo
        }

        self.txt_cambiarColor = [
            self.ql_nombreText, self.ql_apellidoText, self.ql_cedulaText, self.ql_sexoText,
            self.ql_fnacimientoText, self.ql_telefonoText, self.ql_gradodocText, 
            self.ql_anosServiciosText, self.ql_codcargoText, self.ql_codigodepenText, self.lbel_nombreSearch,
            self.ql_buscarText, self.lbel_cedulaSearch, self.textimprimir, self.textrefrescar, self.textsalir,
            self.bttn_verprofesores
        ]

        # Frames para cambio de fondo (modo claro/oscuro)
        self.bg_cambiarColor = [
            self.Headframe, self.FootFrame, self.frame, self.BodyFrame
        ]

    # Ventana de Ver todos los profesores    
    def verProfesores(self):
        from controllers.control_ebusqueda import ControlBusqueda
        # mode="profesores" to avoid grade combo box
        windows = ControlBusqueda(self, mode="profesores")
        if hasattr(self.parent(), '_aplicar_tema'):
            self.parent()._aplicar_tema(windows)
        
        # Setup table columns and data for Professors
        # Column 0: CEDULA, Column 1: NOMBRE
        windows.conTabla("SELECT pcedula, pnombres FROM profesores", "CEDULA", "NOMBRE")
        windows.alFinal.connect(self.funResultado)
        windows.show()
        
    def funResultado(self, xresultado):
        if xresultado != 0:
            # xresultado contains the ID/Cedula from column 0
            self.qlinee_cedulaSearch.setText(str(xresultado))
            self.search_file_profesores()

    # Ventana de Error de Busqueda
    def ventanaError(self, dato=""):
        from controllers.alerta import MensajeCaja
        self.ayuda = MensajeCaja(self, "ERROR DE VALIDACIÓN", 
                                 f"El docente '{dato}' no fue encontrado. Ingrese un dato válido", 1)
    
    def editarError(self, dato=""):
        from controllers.alerta import MensajeCaja
        self.ayuda = MensajeCaja(self, "ERROR DE VALIDACIÓN", 
                                 f"Para editar la información del docente, debe de seleccionar uno", 1)
        
    # Funcion para Imprimir datos de busqueda
    def imprimir_funcion(self):
        from controllers.imprimir import Imprimir
        if not self.qlinee_cedulaInfo.text():
            return

        portada = "U.E.N.B. ANTONIO GUZMÁN BLANCO"
        titulo = "INFORMACIÓN DEL DOCENTE"
        imagenfoot = "./assets/icons/escuelaicon.jpg"
        footer = "PANTALLA DE IMPRESIÓN U.E.N.B ANTONIO GUZMAN BLANCO"

        # Obtener valores de la UI
        valores = []
        for widget in self.mapeo_informacion.values():
            if hasattr(widget, 'text'):
                valores.append(widget.text())
            elif hasattr(widget, 'currentText'):
                valores.append(widget.currentText())
            else:
                valores.append("")
        
        body = []
        labels = [
            "Cédula", "Nombres", "Apellidos", "Sexo", "F. Nacimiento", 
            "Teléfono", "Grado", "Años Servicio", "Cod. Cargo", "Cod. Depen"
        ]
        
        # El orden en body debe coincidir con el reporte deseado
        # Basado en el original: cedula, nombre, apellido, sexo, fnacimiento, tlf, grado, anos, cargo, depen
        # Mapeamos según el orden de labels
        orden_imprimir = [2, 0, 1, 3, 4, 8, 9, 5, 6, 7]
        for idx in orden_imprimir:
            body.append(labels[idx] if idx < len(labels) else "Info")
            body.append(valores[idx])

        Imprimir(self.suplemento.imprimir_profesores(portada, titulo, body, imagenfoot, footer))

    # Funcion para la Busqueda de datos
    def search_file_profesores(self):
        query = ""
        params = ()
        
        nombre_search = self.qlinee_nombreSearch.text().strip().upper()
        cedula_search = self.qlinee_cedulaSearch.text().strip()

        base_query = """
            SELECT pides, pnombres, papellidos, pcedula, psexo, fnacimiento, "pañosservi", 
                   pcodecargo, pcodedepen, ptelefono, pgrado
            FROM public.profesores
        """

        if nombre_search:
            query = base_query + " WHERE pnombres || ' ' || papellidos LIKE %s FETCH FIRST 1 ROW ONLY"
            params = (f"%{nombre_search}%",)
        elif cedula_search:
            query = base_query + " WHERE pcedula = %s"
            params = (cedula_search,)

        if query:
            resultado = self.manager.consultar(query, params)
            if resultado:
                widgets_ordenados = list(self.mapeo_informacion.values())
                # El resultado trae pides at index 0, saltamos ese
                for i, valor in enumerate(resultado[1:]):
                    widget = widgets_ordenados[i]
                    val_str = str(valor) if valor is not None else ""
                    if hasattr(widget, 'setText'):
                        widget.setText(val_str)
                    elif hasattr(widget, 'setCurrentText'):
                        widget.setCurrentText(val_str)
                
                # Guardar el ID para edición
                self.current_idprof = resultado[0]
            else:
                self.ventanaError(nombre_search or cedula_search)
        else:
            self.ventanaError("Vacío")

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
        
        for i in valores:
            if i == "":
                self.editarError()
                return

        for widget in self.mapeo_informacion.values():
            if hasattr(widget, 'setReadOnly'):
                widget.setReadOnly(False)
            elif hasattr(widget, 'setEnabled'):
                widget.setEnabled(True)

        # Cambiar visibilidad de botones
        self.bttn_guardar.show()
        self.ql_guardarText.show()
        self.bttn_cancelar.show()
        self.ql_cancelarText.show()

        self.bttn_editar.hide()
        self.label.hide()
        self.bttn_refrescar.hide()
        self.textrefrescar.hide()
        self.bttn_imprimir.hide()
        self.textimprimir.hide()
        self.bttn_salir.hide()
        self.textsalir.hide()

    def cancelarEdit(self):
        # Deshabilitar edición
        for widget in self.mapeo_informacion.values():
            if hasattr(widget, 'setReadOnly'):
                widget.setReadOnly(True)
            elif hasattr(widget, 'setEnabled'):
                widget.setEnabled(False)

        # Restaurar visibilidad de botones
        self.bttn_guardar.hide()
        self.ql_guardarText.hide()
        self.bttn_cancelar.hide()
        self.ql_cancelarText.hide()

        self.bttn_editar.show()
        self.label.show()
        self.bttn_refrescar.show()
        self.textrefrescar.show()
        self.bttn_imprimir.show()
        self.textimprimir.show()
        self.bttn_salir.show()
        self.textsalir.show()

        # Recargar datos del profesor actual
        if self.current_idprof:
            self.search_file_profesores()

    def guardarEdit(self):
        if not self.current_idprof:
            from controllers.alerta import MensajeCaja
            MensajeCaja(self, "ERROR", "No hay un docente seleccionado para editar", 1)
            return

        # Obtener valores del mapeo
        datos = {}
        for key, widget in self.mapeo_informacion.items():
            if hasattr(widget, 'text'):
                datos[key] = widget.text().strip()
            elif hasattr(widget, 'currentText'):
                datos[key] = widget.currentText().strip()
            elif hasattr(widget, 'toPlainText'):
                datos[key] = widget.toPlainText().strip()

        try:
            # Query de actualización
            query = """
                UPDATE public.profesores SET
                pnombres = %s, papellidos = %s, pcedula = %s, psexo = %s, 
                fnacimiento = %s, "pañosservi" = %s, pcodecargo = %s, 
                pcodedepen = %s, ptelefono = %s, pgrado = %s
                WHERE pides = %s
            """
            params = (
                datos["nombres"], datos["apellidos"], datos["cedula"], datos["sexo"],
                datos["fnacimiento"], int(datos["anos_servicio"] or 0),
                datos["cod_cargo"], datos["cod_depen"], datos["telefono"],
                datos["grado"], self.current_idprof
            )
            
            if self.manager.ejecutar(query, params):
                from controllers.alerta import MensajeCaja
                MensajeCaja(self, "ÉXITO", "Información actualizada correctamente", 1)
                self.cancelarEdit()
            else:
                from controllers.alerta import MensajeCaja
                MensajeCaja(self, "ERROR", "No se pudo actualizar la información en la base de datos", 1)

        except Exception as e:
            print(f"Error en guardarEdit Profesores: {e}")
            from controllers.alerta import MensajeCaja
            MensajeCaja(self, "ERROR CRÍTICO", str(e), 1)

    def cargar_combos(self):
        try:
            # Grados
            # Usamos fetch_all=True para obtener todos los registros
            res_grados = self.manager.consultar("SELECT idgrado, nomgrado FROM grados ORDER BY idgrado ASC", fetch_all=True)
            if res_grados:
                self.cbox_gradodocInfo.clear()
                for item in res_grados:
                    self.cbox_gradodocInfo.addItem(str(item[1]), item[0])
                
            self.cbox_gradodocInfo.setEnabled(False)
        except Exception as e:
            print(f"Error cargando combos en Profesores: {e}")
