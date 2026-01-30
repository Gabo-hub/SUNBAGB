from assets.suplementos import Suplementos
from db.main_database import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QWidget
from views.main_representantes import Ui_Representantes


class Representantes(QWidget, Ui_Representantes):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

         # Variables
        self.suplemento = Suplementos()
        self.manager = conectarse()
        
        # Conectar botones originales
        self.bttnRsalir.clicked.connect(self.close)
        self.bttn_Rimprimir.clicked.connect(self.imprimir_funcion)
        self.bttn_Rbuscar.clicked.connect(self.search_info_representante)
        self.bttn_verrepresentantes.clicked.connect(self.verRepresentantes)
        
        # Conectar nuevos botones
        self.bttn_editar.clicked.connect(self.editarInfo)
        self.bttn_guardar.clicked.connect(self.guardarEdit)
        self.bttn_cancelar.clicked.connect(self.cancelarEdit)
        self.bttn_Rrefrescar.clicked.connect(lambda: (
            setattr(self, 'current_idrepre', None),
            self.qlw_REstudiantes.clear()
        ))
        
        # Ocultar botones de edición por defecto
        self.bttn_guardar.hide()
        self.ql_guardarText.hide()
        self.bttn_cancelar.hide()
        self.ql_cancelarText.hide()

        # Variables
        self.current_idrepre = None
        self.mapeo_informacion = {
            "nombres": self.qlinee_RnombresInfo,
            "apellidos": self.qlinee_RapellidosInfo,
            "cedula": self.qlinee_RcedulaInfo,
            "telefono": self.qlinee_RntelefonoInfo,
            "direccion": self.qpte_RdireccionInfo,
            "direccion_trabajo": self.qpte_RdirecciontrabajoInfo,
            "observaciones": self.qpte_RobservacionesInfo,
            "estado_laboral": self.qlinee_RestadolabInfo,
            "total_representados": self.qlinee_RtotalrepreInfo,
            "parentesco": self.qlinee_RparentescoInfo
        }

        # Etiquetas para cambio de color (utilizadas por PantallaPrint._aplicar_tema)
        self.txt_cambiarColor = [
            self.ql_RnombreSearch, self.ql_RcedulaSearch, self.ql_RbuscarbaseText,
            self.ql_RnombresText, self.ql_RapellidosText, self.ql_RcedulaText, 
            self.ql_RntelefonoText, self.ql_RdireccionText, self.ql_RtotalrepreText, 
            self.ql_RparentescoText, self.ql_RestadoLabText, self.ql_RdireccionTrabText,
            self.ql_RobservacionesText, self.textimprimir, self.textrefrescar, self.textsalir,
            self.bttn_verrepresentantes
        ]
        
        # Frames para cambio de fondo (modo claro/oscuro)
        self.bg_cambiarColor = [
            self.Headframe, self.FootFrame, self.frame, self.BodyFrame
        ]

    # Ventana de Ver todos los representantes
    def verRepresentantes(self):
        from controllers.control_ebusqueda import ControlBusqueda
        # mode="representantes" to avoid grade combo box or default behavior
        windows = ControlBusqueda(self, mode="representantes")
        if hasattr(self.parent(), '_aplicar_tema'):
            self.parent()._aplicar_tema(windows)
        
        # Setup table columns and data for Representatives
        # Column 0: CEDULA, Column 1: NOMBRE
        windows.conTabla("SELECT cedularepre, nrepresentante FROM representantes", "CEDULA", "NOMBRE")
        windows.alFinal.connect(self.funResultado)
        windows.show()

    # Funcion para obtener el resultado de la busqueda    
    def funResultado(self, xresultado):
        if xresultado != 0:
            # xresultado contains the ID/Cedula from column 0
            self.qlinee_RcedulaSearch.setText(str(xresultado))
            self.search_info_representante()

    # Funcion para obtener la informacion del representante
    def search_info_representante(self):
        query = ""
        params = ()
        
        nombre_search = self.qlinee_RnombreSearch.text().strip().upper()
        cedula_search = self.qlinee_RcedulaSearch.text().strip()

        # Query base (el original tenía una subconsulta compleja para parentesco)
        base_query = """
            SELECT idrepresentante, nrepresentante, arepresentante, cedularepre, ntelefonico, 
            ndireccion, ndirecciontrabajo, nobservaciones, estadolaboral, nrepresentados,
            (SELECT descripcion FROM parentesco 
             WHERE idparentesco = (SELECT parentesco FROM estudiantes WHERE idrepresentante = representantes.idrepresentante LIMIT 1))
            FROM public.representantes
        """

        if nombre_search:
            query = base_query + " WHERE nrepresentante || ' ' || arepresentante LIKE %s FETCH FIRST 1 ROW ONLY"
            params = (f"%{nombre_search}%",)
        elif cedula_search:
            query = base_query + " WHERE cedularepre = %s"
            params = (cedula_search,)

        if query:
            resultado = self.manager.consultar(query, params)
            if resultado:
                widgets_ordenados = list(self.mapeo_informacion.values())
                # El resultado trae idrepresentante at index 0, saltamos ese
                for i, valor in enumerate(resultado[1:]):
                    widget = widgets_ordenados[i]
                    val_str = str(valor) if valor is not None else ""
                    if hasattr(widget, 'setText'):
                        widget.setText(val_str)
                    elif hasattr(widget, 'setPlainText'):
                        widget.setPlainText(val_str)
                
                # Guardar el ID para edición
                self.current_idrepre = resultado[0]

                # --- NUEVA LÓGICA: Detalle de Representados ---
                self.qlw_REstudiantes.clear()
                query_estudiantes = "SELECT psnombres || ' ' || psapellidos FROM estudiantes WHERE idrepresentante = %s"
                estudiantes = self.manager.consultar(query_estudiantes, (self.current_idrepre,), fetch_all=True)
                
                if estudiantes:
                    for est in estudiantes:
                        self.qlw_REstudiantes.addItem(est[0])
                    # Actualizar contador automáticamente
                    self.qlinee_RtotalrepreInfo.setText(str(len(estudiantes)))
                else:
                    self.qlinee_RtotalrepreInfo.setText("0")
                # -----------------------------------------------
            else:
                self.ventanaError(nombre_search or cedula_search)
        else:
            self.ventanaError("Vacío")

    def editarInfo(self):
        # Obtener valores de la UI para validar si hay algo cargado
        valores = [widget.text() if hasattr(widget, 'text') else widget.toPlainText() 
                  for widget in self.mapeo_informacion.values()]
        
        if not any(valores):
            self.ventanaError("Ninguno")
            return

        # Habilitar edición (excepto el contador de representados)
        for key, widget in self.mapeo_informacion.items():
            if key == "total_representados":
                continue
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
        self.bttn_Rrefrescar.hide()
        self.textrefrescar.hide()
        self.bttn_Rimprimir.hide()
        self.textimprimir.hide()
        self.bttnRsalir.hide()
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
        self.bttn_Rrefrescar.show()
        self.textrefrescar.show()
        self.bttn_Rimprimir.show()
        self.textimprimir.show()
        self.bttnRsalir.show()
        self.textsalir.show()

        # Recargar datos del representante actual
        if self.current_idrepre:
            self.search_info_representante()
        else:
            self.qlw_REstudiantes.clear()

    def guardarEdit(self):
        if not self.current_idrepre:
            from controllers.alerta import MensajeCaja
            MensajeCaja(self, "ERROR", "No hay un representante seleccionado para editar", 1)
            return

        # Obtener valores del mapeo
        datos = {}
        for key, widget in self.mapeo_informacion.items():
            if hasattr(widget, 'text'):
                datos[key] = widget.text().strip()
            elif hasattr(widget, 'toPlainText'):
                datos[key] = widget.toPlainText().strip()

        try:
            # Query de actualización
            query = """
                UPDATE public.representantes SET
                nrepresentante = %s, arepresentante = %s, cedularepre = %s, 
                ntelefonico = %s, ndireccion = %s, ndirecciontrabajo = %s, 
                nobservaciones = %s, estadolaboral = %s, nrepresentados = %s
                WHERE idrepresentante = %s
            """
            params = (
                datos["nombres"], datos["apellidos"], datos["cedula"],
                datos["telefono"], datos["direccion"], datos["direccion_trabajo"],
                datos["observaciones"], datos["estado_laboral"], 
                int(datos["total_representados"] or 0), self.current_idrepre
            )
            
            if self.manager.ejecutar(query, params):
                from controllers.alerta import MensajeCaja
                MensajeCaja(self, "ÉXITO", "Información actualizada correctamente", 1)
                self.cancelarEdit()
            else:
                from controllers.alerta import MensajeCaja
                MensajeCaja(self, "ERROR", "No se pudo actualizar la información en la base de datos", 1)

        except Exception as e:
            print(f"Error en guardarEdit Representantes: {e}")
            from controllers.alerta import MensajeCaja
            MensajeCaja(self, "ERROR CRÍTICO", str(e), 1)

    # Funcion para mostrar el error
    def ventanaError(self, dato=""):
        from controllers.alerta import MensajeCaja
        self.ayuda = MensajeCaja(self,"ERROR DE VALIDACIÓN", 
                                 f"El representante '{dato}' no fue encontrado. Ingrese un dato válido", 1)

    # Funcion para imprimir
    def imprimir_funcion(self):
        from controllers.imprimir import Imprimir
        if not self.qlinee_RcedulaInfo.text():
            return

        portada = "U.E.N.B. ANTONIO GUZMÁN BLANCO"
        titulo = "INFORMACIÓN DEL REPRESENTANTE"
        imagenfoot = "./assets/icons/escuelaicon.jpg"
        footer = "PANTALLA DE IMPRESIÓN U.E.N.B ANTONIO GUZMAN BLANCO"

        # Obtener valores de la UI
        valores = [widget.text() if hasattr(widget, 'text') else widget.toPlainText() 
                  for widget in self.mapeo_informacion.values()]
        
        body = []
        labels = [
            "Nombres", "Apellidos", "Cédula", "Teléfono", "Dirección", 
            "D. Trabajo", "Observaciones", "Estado Lab.", "Representados", "Parentesco"
        ]
        
        # El orden en body debe coincidir con el reporte deseado (según original)
        # Basado en original: cedula, nombre, apellido, tlf, total, parentesco, estado_lab, direccion, dir_trab, observ
        orden_imprimir = [2, 0, 1, 3, 8, 9, 7, 4, 5, 6]
        for idx in orden_imprimir:
            body.append(labels[idx])
            body.append(valores[idx])

        Imprimir(self.suplemento.imprimir_profesores(portada, titulo, body, imagenfoot, footer))

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
