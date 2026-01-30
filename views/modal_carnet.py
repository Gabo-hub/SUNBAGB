from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QDialog, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget, QGroupBox, QSpinBox, QFormLayout)

class Ui_ModalCarnet(object):
    def setupUi(self, ModalCarnet):
        if not ModalCarnet.objectName():
            ModalCarnet.setObjectName(u"ModalCarnet")
        ModalCarnet.resize(800, 600)
        ModalCarnet.setStyleSheet(u"background-color: rgb(51, 54, 57); color: white;")
        
        self.verticalLayout = QVBoxLayout(ModalCarnet)
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        # Header
        self.frame_header = QFrame(ModalCarnet)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        self.label_titulo = QLabel(self.frame_header)
        self.label_titulo.setObjectName(u"label_titulo")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_titulo.setFont(font)
        self.horizontalLayout.addWidget(self.label_titulo)
        
        self.verticalLayout.addWidget(self.frame_header)
        
        # Main Content
        self.frame_content = QFrame(ModalCarnet)
        self.frame_content.setObjectName(u"frame_content")
        self.gridLayout = QGridLayout(self.frame_content)
        self.gridLayout.setObjectName(u"gridLayout")
        
        # Area Foto
        self.frame_foto = QFrame(self.frame_content)
        self.frame_foto.setObjectName(u"frame_foto")
        self.frame_foto.setFrameShape(QFrame.StyledPanel)
        self.verticalLayout_foto = QVBoxLayout(self.frame_foto)
        
        self.label_foto_titulo = QLabel(self.frame_foto)
        self.label_foto_titulo.setObjectName(u"label_foto_titulo")
        self.label_foto_titulo.setText("FOTO DEL ESTUDIANTE")
        self.verticalLayout_foto.addWidget(self.label_foto_titulo)
        
        self.lbl_foto_preview = QLabel(self.frame_foto)
        self.lbl_foto_preview.setObjectName(u"lbl_foto_preview")
        self.lbl_foto_preview.setMinimumSize(QSize(150, 150))
        self.lbl_foto_preview.setAlignment(Qt.AlignCenter)
        self.lbl_foto_preview.setStyleSheet("border: 1px solid white;")
        self.verticalLayout_foto.addWidget(self.lbl_foto_preview)
        
        self.bttn_cargar_foto = QPushButton(self.frame_foto)
        self.bttn_cargar_foto.setObjectName(u"bttn_cargar_foto")
        self.bttn_cargar_foto.setText("Cargar Foto")
        self.verticalLayout_foto.addWidget(self.bttn_cargar_foto)
        
        self.gridLayout.addWidget(self.frame_foto, 0, 0, 1, 1)
        
        # Area Carnet Preview
        self.frame_carnet = QFrame(self.frame_content)
        self.frame_carnet.setObjectName(u"frame_carnet")
        self.verticalLayout_carnet = QVBoxLayout(self.frame_carnet)
        
        self.label_carnet_titulo = QLabel(self.frame_carnet)
        self.label_carnet_titulo.setObjectName(u"label_carnet_titulo")
        self.label_carnet_titulo.setText("VISTA PREVIA CARNET")
        self.verticalLayout_carnet.addWidget(self.label_carnet_titulo)
        
        self.lbl_carnet_preview = QLabel(self.frame_carnet)
        self.lbl_carnet_preview.setObjectName(u"lbl_carnet_preview")
        self.lbl_carnet_preview.setMinimumSize(QSize(400, 250))
        self.lbl_carnet_preview.setAlignment(Qt.AlignCenter)
        self.lbl_carnet_preview.setStyleSheet("border: 1px solid white;")
        self.verticalLayout_carnet.addWidget(self.lbl_carnet_preview)
        
        self.gridLayout.addWidget(self.frame_carnet, 0, 1, 1, 1)

        # Calibration Controls
        self.group_calibration = QGroupBox(self.frame_content)
        self.group_calibration.setObjectName(u"group_calibration")
        self.group_calibration.setTitle("Calibración de Coordenadas (X, Y)")
        self.gridLayout_calib = QGridLayout(self.group_calibration)
        
        # Photo Coords
        self.lbl_calib_foto = QLabel("Foto (X, Y):", self.group_calibration)
        self.sb_foto_x = QSpinBox(self.group_calibration)
        self.sb_foto_x.setRange(0, 1000)
        self.sb_foto_x.setValue(59)
        self.sb_foto_y = QSpinBox(self.group_calibration)
        self.sb_foto_y.setRange(0, 1000)
        self.sb_foto_y.setValue(368)
        self.gridLayout_calib.addWidget(self.lbl_calib_foto, 0, 0)
        self.gridLayout_calib.addWidget(self.sb_foto_x, 0, 1)
        self.gridLayout_calib.addWidget(self.sb_foto_y, 0, 2)
        
        # Photo Size
        self.lbl_calib_foto_size = QLabel("Foto (W, H):", self.group_calibration)
        self.sb_foto_w = QSpinBox(self.group_calibration)
        self.sb_foto_w.setRange(10, 500)
        self.sb_foto_w.setValue(255) # Calc based on 21.5mm
        self.sb_foto_h = QSpinBox(self.group_calibration)
        self.sb_foto_h.setRange(10, 500)
        self.sb_foto_h.setValue(280) # Calc based on 23.6mm
        self.gridLayout_calib.addWidget(self.lbl_calib_foto_size, 0, 3)
        self.gridLayout_calib.addWidget(self.sb_foto_w, 0, 4)
        self.gridLayout_calib.addWidget(self.sb_foto_h, 0, 5)
        
        # Name Coords
        self.lbl_calib_nombre = QLabel("Nombre:", self.group_calibration)
        self.sb_nombre_x = QSpinBox(self.group_calibration)
        self.sb_nombre_x.setRange(0, 1000)
        self.sb_nombre_x.setValue(104)
        self.sb_nombre_y = QSpinBox(self.group_calibration)
        self.sb_nombre_y.setRange(0, 1000)
        self.sb_nombre_y.setValue(660)
        self.gridLayout_calib.addWidget(self.lbl_calib_nombre, 1, 0)
        self.gridLayout_calib.addWidget(self.sb_nombre_x, 1, 1)
        self.gridLayout_calib.addWidget(self.sb_nombre_y, 1, 2)

        # Cedula Coords
        self.lbl_calib_cedula = QLabel("Cédula:", self.group_calibration)
        self.sb_cedula_x = QSpinBox(self.group_calibration)
        self.sb_cedula_x.setRange(0, 1000)
        self.sb_cedula_x.setValue(104)
        self.sb_cedula_y = QSpinBox(self.group_calibration)
        self.sb_cedula_y.setRange(0, 1000)
        self.sb_cedula_y.setValue(700)
        self.gridLayout_calib.addWidget(self.lbl_calib_cedula, 2, 0)
        self.gridLayout_calib.addWidget(self.sb_cedula_x, 2, 1)
        self.gridLayout_calib.addWidget(self.sb_cedula_y, 2, 2)

        # Grade Coords
        self.lbl_calib_grado = QLabel("Grado:", self.group_calibration)
        self.sb_grado_x = QSpinBox(self.group_calibration)
        self.sb_grado_x.setRange(0, 1000)
        self.sb_grado_x.setValue(116)
        self.sb_grado_y = QSpinBox(self.group_calibration)
        self.sb_grado_y.setRange(0, 1000)
        self.sb_grado_y.setValue(740)
        self.gridLayout_calib.addWidget(self.lbl_calib_grado, 3, 0)
        self.gridLayout_calib.addWidget(self.sb_grado_x, 3, 1)
        self.gridLayout_calib.addWidget(self.sb_grado_y, 3, 2)

        self.gridLayout.addWidget(self.group_calibration, 1, 0, 1, 2)
        
        self.verticalLayout.addWidget(self.frame_content)
        
        # Footer
        self.frame_footer = QFrame(ModalCarnet)
        self.frame_footer.setObjectName(u"frame_footer")
        self.horizontalLayout_footer = QHBoxLayout(self.frame_footer)
        
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_footer.addItem(self.horizontalSpacer)
        
        self.bttn_imprimir = QPushButton(self.frame_footer)
        self.bttn_imprimir.setObjectName(u"bttn_imprimir")
        self.bttn_imprimir.setText("Imprimir Carnet")
        self.horizontalLayout_footer.addWidget(self.bttn_imprimir)
        
        self.bttn_pdf = QPushButton(self.frame_footer)
        self.bttn_pdf.setObjectName(u"bttn_pdf")
        self.bttn_pdf.setText("Guardar PDF")
        self.horizontalLayout_footer.addWidget(self.bttn_pdf)
        
        self.bttn_cerrar = QPushButton(self.frame_footer)
        self.bttn_cerrar.setObjectName(u"bttn_cerrar")
        self.bttn_cerrar.setText("Cerrar")
        self.horizontalLayout_footer.addWidget(self.bttn_cerrar)
        
        self.verticalLayout.addWidget(self.frame_footer)

        self.retranslateUi(ModalCarnet)
        QMetaObject.connectSlotsByName(ModalCarnet)

    def retranslateUi(self, ModalCarnet):
        ModalCarnet.setWindowTitle(QCoreApplication.translate("ModalCarnet", u"Generación de Carnet Estudiantil", None))
        self.label_titulo.setText(QCoreApplication.translate("ModalCarnet", u"GENERACIÓN DE CARNET", None))
