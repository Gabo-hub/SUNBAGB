from db.main_database import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from views.main_windows import Ui_Principal

class PantallaPrint(QMainWindow, Ui_Principal):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Manipulación de los eventos click de los Botones
        self.bestudiantes_3.clicked.connect(self.estudiantespantalla)
        self.bprofesores_3.clicked.connect(self.profesorespantalla)
        self.brepresentantes_3.clicked.connect(self.representantespantalla)
        self.brepresentantes_3.clicked.connect(self.representantespantalla)
        # self.bnotas.clicked.connect(self.notaspantalla) # Deprecated
        self.pushButton_4.clicked.connect(self.close)
        self.checkBox.clicked.connect(self.modoclaro)
        self.actionRegistro_de_La_Data.triggered.connect(self.añadirdatos)


        
    def añadirdatos(self):
        from controllers.añadirdato import IntroduccionDeDatos
        windows = IntroduccionDeDatos(self)
        self._aplicar_tema(windows)
        windows.show()
    
    def _aplicar_tema(self, windows):
        """Aplica el tema actual a una ventana secundaria."""
        is_light = self.checkBox.isChecked()
        bg_col = "rgb(255, 255, 255)" if is_light else "rgb(51, 54, 57)"
        txt_col = "rgb(51, 54, 57)" if is_light else "rgb(255, 255, 255)"
        
        # Definir colores base
        bg_frame = "rgb(245, 245, 245)" if is_light else "rgb(85, 90, 95)"
        grid_col = "rgb(200, 200, 200)" if is_light else "rgb(60, 60, 60)"
        
        # Estilo global para la ventana y menús/combos
        windows.setStyleSheet(f"""
            QWidget {{
                background-color: {bg_col};
                color: {txt_col};
            }}
            QMenu {{
                background-color: {bg_col};
                color: {txt_col};
                border: 1px solid {grid_col};
            }}
            QMenu::item::selected {{
                background-color: {bg_frame};
                color: {txt_col};
            }}
            QComboBox {{
                background-color: {bg_col};
                color: {txt_col};
                border: 1px solid {grid_col};
            }}
            QComboBox QAbstractItemView {{
                background-color: {bg_col};
                color: {txt_col};
                selection-background-color: {bg_frame};
                selection-color: {txt_col};
            }}
        """)
        
        # bg_cambiarColor contiene widgets que deben cambiar su fondo
        if hasattr(windows, 'bg_cambiarColor'):
            for widget in windows.bg_cambiarColor:
                if isinstance(widget, QWidget):
                    # Preservar estilos complejos si es frPieBotonSalir
                    if widget.objectName() == "frPieBotonSalir":
                        btn_bg = "rgb(71, 93, 144)"
                        widget.setStyleSheet(f"""
                            QFrame {{ background-color: {bg_frame}; }}
                            QPushButton {{ color: white; background-color: {btn_bg}; border-radius: 5px; padding: 5px; }}
                            QPushButton:hover {{ background-color: rgb(89, 118, 181); }}
                        """)
                    elif widget.objectName() == "headframe":
                         widget.setStyleSheet(f"background-color: {bg_frame}; border-radius: 10px;")
                    elif widget.objectName() == "footerframe":
                         widget.setStyleSheet(f"background-color: {bg_frame}; border-radius: 5px;")
                    else:
                        widget.setStyleSheet(f"background-color: {bg_frame}; border: none;")

        # Soporte para QTableWidget
        if hasattr(windows, 'tblBusqueda') or hasattr(windows, 'table_horario'):
            
            style_table = f"""
                QTableWidget {{ 
                    background-color: {bg_col}; 
                    color: {txt_col};
                    gridline-color: {grid_col};
                }}
                QHeaderView::section {{
                    background-color: rgb(24, 42, 127);
                    color: white;
                    padding: 4px;
                }}
            """
            
            if hasattr(windows, 'tblBusqueda'):
                windows.tblBusqueda.setStyleSheet(style_table)

        if hasattr(windows, 'tblAnadirDatos'):
            # Colores para QTabWidget (Tabs)
            tab_bg_sel = bg_col
            tab_txt_sel = txt_col
            
            if is_light:
                tab_bg_unsel = "rgb(220, 220, 220)"
                tab_txt_unsel = "rgb(80, 80, 80)"
                border_col = "rgb(200, 200, 200)"
            else:
                tab_bg_unsel = "rgb(70, 70, 70)"
                tab_txt_unsel = "rgb(200, 200, 200)"
                border_col = "rgb(100, 100, 100)"

            windows.tblAnadirDatos.setStyleSheet(f"""
                QTabWidget::pane {{ 
                    border: 1px solid {border_col};
                    background-color: {tab_bg_sel}; 
                }}
                QTabBar::tab {{
                    background: {tab_bg_unsel};
                    color: {tab_txt_unsel};
                    padding: 8px 20px;
                    border: 1px solid {border_col};
                    border-bottom: none;
                    border-top-left-radius: 4px;
                    border-top-right-radius: 4px;
                    margin-right: 2px;
                }}
                QTabBar::tab:selected {{
                    background: {tab_bg_sel};
                    color: {tab_txt_sel};
                    border-bottom: 2px solid {tab_bg_sel}; /* Blends with pane */
                }}
                QTabBar::tab:hover {{
                    background-color: {tab_bg_sel};
                    color: {tab_txt_sel};
                }}
            """)

        # txt_cambiarColor ahora contiene objetos QWidget reales
        if hasattr(windows, 'txt_cambiarColor'):
            for widget in windows.txt_cambiarColor:
                if isinstance(widget, QWidget):
                    widget.setStyleSheet(f"color: {txt_col}; background: transparent;")
                else: # Fallback
                    try:
                        obj = getattr(windows, widget)
                        obj.setStyleSheet(f"color: {txt_col}; background: transparent;")
                    except Exception:
                        pass

    def estudiantespantalla(self):
        from controllers.main_estudiantes import Estudiantes
        windows = Estudiantes(self)
        screen = QGuiApplication.primaryScreen().availableGeometry()
        windows.move((screen.width() - windows.width()) / 2, (screen.height() - windows.height()) / 8)
        
        self._aplicar_tema(windows)
        windows.show()

    def profesorespantalla(self):
        from controllers.main_profesores import Profesores
        windows = Profesores(self)
        self._aplicar_tema(windows)
        windows.show()

    def representantespantalla(self):
        from controllers.main_representantes import Representantes
        windows1 = Representantes(self)
        screen = QGuiApplication.primaryScreen().availableGeometry()
        windows1.move((screen.width() - windows1.width()) / 2, (screen.height() - windows1.height()) / 8)
        
        self._aplicar_tema(windows1)
        windows1.show()

    # def notaspantalla(self):
    #     from controllers.main_notas import MainNotas
    #     windows = MainNotas(self)
    #     self._aplicar_tema(windows)
    #     windows.show()

    def modoclaro(self):
        is_light = self.checkBox.isChecked()
        bg_col = "rgb(255, 255, 255)" if is_light else "rgb(51, 54, 57)"
        txt_col = "rgb(51, 54, 57)" if is_light else "rgb(255, 255, 255)"
        
        if hasattr(self, 'label'):
            self.label.setStyleSheet(f"color: {txt_col};")
        if hasattr(self, 'checkBox'):
            self.checkBox.setStyleSheet(f"color: {txt_col};")
        if hasattr(self, 'pushButton_4'):
            self.pushButton_4.setStyleSheet(f"color: {txt_col};")
        bg_frame = "rgb(245, 245, 245)" if is_light else "rgb(85, 90, 95)"
        if hasattr(self, 'frame'):
            self.frame.setStyleSheet(f"background-color: {bg_frame}; border: none;")
        if hasattr(self, 'frame_2'):
            self.frame_2.setStyleSheet(f"background-color: {bg_frame}; border: none;")

        self.setStyleSheet(f"background-color: {bg_col};")
        self.label_6.setStyleSheet(f"color: {txt_col};")
        self.label_7.setStyleSheet(f"color: {txt_col};")
        self.labelestudiantes_3.setStyleSheet(f"color: {txt_col};")
        if hasattr(self, 'label_notas'):
            self.label_notas.setStyleSheet(f"color: {txt_col};")


