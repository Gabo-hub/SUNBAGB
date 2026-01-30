
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ModalNotas(object):
    def setupUi(self, ModalNotas):
        if not ModalNotas.objectName():
            ModalNotas.setObjectName(u"ModalNotas")
        ModalNotas.resize(700, 500)
        ModalNotas.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        
        self.verticalLayout = QVBoxLayout(ModalNotas)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        # Header
        self.frame_header = QFrame(ModalNotas)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        self.label_titulo = QLabel(self.frame_header)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.horizontalLayout.addWidget(self.label_titulo)
        self.verticalLayout.addWidget(self.frame_header)
        
        # Info Estudiante
        self.frame_info = QFrame(ModalNotas)
        self.frame_info.setObjectName(u"frame_info")
        self.gridLayout_info = QGridLayout(self.frame_info)
        self.gridLayout_info.setObjectName(u"gridLayout_info")
        
        self.label_estudiante = QLabel(self.frame_info)
        self.label_estudiante.setObjectName(u"label_estudiante")
        font_bold = QFont()
        font_bold.setBold(True)
        self.label_estudiante.setFont(font_bold)
        self.gridLayout_info.addWidget(self.label_estudiante, 0, 0, 1, 1)
        
        self.label_estudiante_val = QLabel(self.frame_info)
        self.label_estudiante_val.setObjectName(u"label_estudiante_val")
        self.gridLayout_info.addWidget(self.label_estudiante_val, 0, 1, 1, 1)
        
        self.verticalLayout.addWidget(self.frame_info)

        # Formulario
        self.frame_form = QFrame(ModalNotas)
        self.frame_form.setObjectName(u"frame_form")
        self.gridLayout_form = QGridLayout(self.frame_form)
        self.gridLayout_form.setObjectName(u"gridLayout_form")
        
        self.label_anio = QLabel(self.frame_form)
        self.label_anio.setObjectName(u"label_anio")
        self.gridLayout_form.addWidget(self.label_anio, 0, 0, 1, 1)
        
        self.qlinee_anio = QLineEdit(self.frame_form)
        self.qlinee_anio.setObjectName(u"qlinee_anio")
        self.qlinee_anio.setPlaceholderText("Ej: 2024-2025")
        self.gridLayout_form.addWidget(self.qlinee_anio, 0, 1, 1, 1)

        self.label_grado = QLabel(self.frame_form)
        self.label_grado.setObjectName(u"label_grado")
        self.gridLayout_form.addWidget(self.label_grado, 0, 2, 1, 1)

        self.cbox_grado = QComboBox(self.frame_form)
        self.cbox_grado.setObjectName(u"cbox_grado")
        
        self.gridLayout_form.addWidget(self.cbox_grado, 0, 3, 1, 1)

        self.label_nota = QLabel(self.frame_form)
        self.label_nota.setObjectName(u"label_nota")
        self.gridLayout_form.addWidget(self.label_nota, 1, 0, 1, 1)
        
        self.cbox_nota = QComboBox(self.frame_form)
        self.cbox_nota.setObjectName(u"cbox_nota")
        self.cbox_nota.addItems(["A", "B", "C", "D", "E"])
        self.gridLayout_form.addWidget(self.cbox_nota, 1, 1, 1, 1)
        
        self.label_obs = QLabel(self.frame_form)
        self.label_obs.setObjectName(u"label_obs")
        self.gridLayout_form.addWidget(self.label_obs, 2, 0, 1, 1)
        
        self.qpte_obs = QPlainTextEdit(self.frame_form)
        self.qpte_obs.setObjectName(u"qpte_obs")
        self.qpte_obs.setMaximumHeight(60)
        self.gridLayout_form.addWidget(self.qpte_obs, 2, 1, 1, 3)
        
        self.bttn_guardar = QPushButton(self.frame_form)
        self.bttn_guardar.setObjectName(u"bttn_guardar")
        self.bttn_guardar.setMinimumHeight(30)
        self.bttn_guardar.setStyleSheet(u"background-color: rgb(85, 170, 255); color: white; font-weight: bold; border-radius: 5px;")
        self.gridLayout_form.addWidget(self.bttn_guardar, 3, 0, 1, 4)
        
        self.verticalLayout.addWidget(self.frame_form)

        # Tabla
        self.table_notas = QTableWidget(ModalNotas)
        if (self.table_notas.columnCount() < 5):
            self.table_notas.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_notas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_notas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_notas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_notas.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_notas.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table_notas.setObjectName(u"table_notas")
        self.table_notas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table_notas.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.table_notas.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.table_notas.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.table_notas.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        
        self.verticalLayout.addWidget(self.table_notas)

        # Footer
        self.frame_footer = QFrame(ModalNotas)
        self.frame_footer.setObjectName(u"frame_footer")
        self.horizontalLayout_footer = QHBoxLayout(self.frame_footer)
        self.horizontalLayout_footer.setObjectName(u"horizontalLayout_footer")
        
        self.bttn_cerrar = QPushButton(self.frame_footer)
        self.bttn_cerrar.setObjectName(u"bttn_cerrar")
        self.bttn_cerrar.setMinimumHeight(30)
        self.bttn_cerrar.setStyleSheet(u"background-color: rgb(255, 85, 85); color: white; border-radius: 5px;")
        self.horizontalLayout_footer.addWidget(self.bttn_cerrar)
        
        self.verticalLayout.addWidget(self.frame_footer)

        self.retranslateUi(ModalNotas)
        QMetaObject.connectSlotsByName(ModalNotas)

    def retranslateUi(self, ModalNotas):
        ModalNotas.setWindowTitle(QCoreApplication.translate("ModalNotas", u"Historial de Notas", None))
        self.label_titulo.setText(QCoreApplication.translate("ModalNotas", u"HISTORIAL ACADÉMICO", None))
        self.label_estudiante.setText(QCoreApplication.translate("ModalNotas", u"Estudiante:", None))
        self.label_estudiante_val.setText(QCoreApplication.translate("ModalNotas", u"-", None))
        
        self.label_anio.setText(QCoreApplication.translate("ModalNotas", u"Año Escolar:", None))
        self.label_grado.setText(QCoreApplication.translate("ModalNotas", u"Grado y Sección:", None))
        self.label_nota.setText(QCoreApplication.translate("ModalNotas", u"Nota Final:", None))
        self.label_obs.setText(QCoreApplication.translate("ModalNotas", u"Observación:", None))
        self.bttn_guardar.setText(QCoreApplication.translate("ModalNotas", u"REGISTRAR NOTA", None))
        
        ___qtablewidgetitem = self.table_notas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ModalNotas", u"Año Escolar", None));
        ___qtablewidgetitem1 = self.table_notas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ModalNotas", u"Grado", None));
        ___qtablewidgetitem2 = self.table_notas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ModalNotas", u"Sección", None));
        ___qtablewidgetitem3 = self.table_notas.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ModalNotas", u"Nota", None));
        ___qtablewidgetitem4 = self.table_notas.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ModalNotas", u"Observación", None));
        
        self.bttn_cerrar.setText(QCoreApplication.translate("ModalNotas", u"CERRAR", None))
