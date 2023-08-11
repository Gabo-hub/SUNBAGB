# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'añadirdato.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import views.resource_rc

class Ui_AnadirDatos(object):
    def setupUi(self, AnadirDatos):
        if not AnadirDatos.objectName():
            AnadirDatos.setObjectName(u"AnadirDatos")
        AnadirDatos.resize(789, 541)
        AnadirDatos.setStyleSheet(u"background-color: rgb(51, 54, 57);")
        self.gridLayout_3 = QGridLayout(AnadirDatos)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(AnadirDatos)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setFamily(u"Poppins")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.qw_Estudiantes = QWidget()
        self.qw_Estudiantes.setObjectName(u"qw_Estudiantes")
        self.qw_Estudiantes.setCursor(QCursor(Qt.ArrowCursor))
        self.qw_Estudiantes.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.qw_Estudiantes)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_12 = QFrame(self.qw_Estudiantes)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"background-color: rgb(85, 90, 95);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_12)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.label_18 = QLabel(self.frame_12)
        self.label_18.setObjectName(u"label_18")
        font1 = QFont()
        font1.setFamily(u"Poppins")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_12.addWidget(self.label_18, 1, 1, 1, 1)

        self.bttn_Elimpiar = QPushButton(self.frame_12)
        self.bttn_Elimpiar.setObjectName(u"bttn_Elimpiar")
        self.bttn_Elimpiar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bttn_Elimpiar.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #757a80;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{		\n"
"		color: rgb(255, 255, 255);\n"
"	 	background-color:#333639;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Botones salida/clear_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bttn_Elimpiar.setIcon(icon)
        self.bttn_Elimpiar.setIconSize(QSize(50, 50))
        self.bttn_Elimpiar.setFlat(True)

        self.gridLayout_12.addWidget(self.bttn_Elimpiar, 0, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(275, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.bttn_Eguardar = QPushButton(self.frame_12)
        self.bttn_Eguardar.setObjectName(u"bttn_Eguardar")
        self.bttn_Eguardar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bttn_Eguardar.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #757a80;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{		\n"
"		color: rgb(255, 255, 255);\n"
"	 	background-color:#333639;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Botones salida/save-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bttn_Eguardar.setIcon(icon1)
        self.bttn_Eguardar.setIconSize(QSize(50, 50))
        self.bttn_Eguardar.setFlat(True)

        self.gridLayout_12.addWidget(self.bttn_Eguardar, 0, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(274, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_6, 0, 5, 1, 1)

        self.label_2 = QLabel(self.frame_12)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_12.addWidget(self.label_2, 1, 3, 1, 1)

        self.label_17 = QLabel(self.frame_12)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_12.addWidget(self.label_17, 1, 2, 1, 1)

        self.bttn_Salir = QPushButton(self.frame_12)
        self.bttn_Salir.setObjectName(u"bttn_Salir")
        self.bttn_Salir.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #757a80;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{		\n"
"		color: rgb(255, 255, 255);\n"
"	 	background-color:#333639;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Botones salida/salir_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bttn_Salir.setIcon(icon2)
        self.bttn_Salir.setIconSize(QSize(50, 50))
        self.bttn_Salir.setFlat(True)

        self.gridLayout_12.addWidget(self.bttn_Salir, 0, 3, 1, 1)


        self.gridLayout_4.addWidget(self.frame_12, 3, 0, 1, 1)

        self.line_9 = QFrame(self.qw_Estudiantes)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_9, 2, 0, 1, 1)

        self.frame_10 = QFrame(self.qw_Estudiantes)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgb(85, 90, 95);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ql_Ebasededatos = QLabel(self.frame_10)
        self.ql_Ebasededatos.setObjectName(u"ql_Ebasededatos")
        font2 = QFont()
        font2.setFamily(u"Poppins")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.ql_Ebasededatos.setFont(font2)
        self.ql_Ebasededatos.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.ql_Ebasededatos)

        self.ql_Eingresarinfo = QLabel(self.frame_10)
        self.ql_Eingresarinfo.setObjectName(u"ql_Eingresarinfo")
        self.ql_Eingresarinfo.setFont(font2)
        self.ql_Eingresarinfo.setStyleSheet(u"color: rgb(85, 170, 255);")

        self.verticalLayout_5.addWidget(self.ql_Eingresarinfo)


        self.gridLayout_4.addWidget(self.frame_10, 0, 0, 1, 1)

        self.frame_11 = QFrame(self.qw_Estudiantes)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.line_7 = QFrame(self.frame_11)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_7, 7, 2, 7, 2)

        self.qlinee_EapellidosInfo = QLineEdit(self.frame_11)
        self.qlinee_EapellidosInfo.setObjectName(u"qlinee_EapellidosInfo")
        self.qlinee_EapellidosInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.qlinee_EapellidosInfo, 8, 1, 1, 1)

        self.ql_EnombreText = QLabel(self.frame_11)
        self.ql_EnombreText.setObjectName(u"ql_EnombreText")
        self.ql_EnombreText.setFont(font1)
        self.ql_EnombreText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_EnombreText, 7, 0, 1, 1)

        self.qlinee_EnombreInfo = QLineEdit(self.frame_11)
        self.qlinee_EnombreInfo.setObjectName(u"qlinee_EnombreInfo")
        self.qlinee_EnombreInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.qlinee_EnombreInfo, 7, 1, 1, 1)

        self.qlinee_EcedulaInfo = QLineEdit(self.frame_11)
        self.qlinee_EcedulaInfo.setObjectName(u"qlinee_EcedulaInfo")
        self.qlinee_EcedulaInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")
        self.qlinee_EcedulaInfo.setMaxLength(8)

        self.gridLayout_9.addWidget(self.qlinee_EcedulaInfo, 4, 1, 3, 1)

        self.ql_EapellidoText = QLabel(self.frame_11)
        self.ql_EapellidoText.setObjectName(u"ql_EapellidoText")
        self.ql_EapellidoText.setFont(font1)
        self.ql_EapellidoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_EapellidoText, 8, 0, 1, 1)

        self.qlinee_EedadInfo = QLineEdit(self.frame_11)
        self.qlinee_EedadInfo.setObjectName(u"qlinee_EedadInfo")
        self.qlinee_EedadInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.qlinee_EedadInfo, 10, 1, 1, 1)

        self.line_8 = QFrame(self.frame_11)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_9.addWidget(self.line_8, 0, 0, 1, 6)

        self.qlinee_EsexoInfo = QLineEdit(self.frame_11)
        self.qlinee_EsexoInfo.setObjectName(u"qlinee_EsexoInfo")
        self.qlinee_EsexoInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.qlinee_EsexoInfo, 9, 1, 1, 1)

        self.ql_EsexoText = QLabel(self.frame_11)
        self.ql_EsexoText.setObjectName(u"ql_EsexoText")
        self.ql_EsexoText.setFont(font1)
        self.ql_EsexoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_EsexoText, 9, 0, 1, 1)

        self.ql_EcedulaText = QLabel(self.frame_11)
        self.ql_EcedulaText.setObjectName(u"ql_EcedulaText")
        self.ql_EcedulaText.setFont(font1)
        self.ql_EcedulaText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_EcedulaText, 3, 0, 4, 1)

        self.ql_EedadText = QLabel(self.frame_11)
        self.ql_EedadText.setObjectName(u"ql_EedadText")
        self.ql_EedadText.setFont(font1)
        self.ql_EedadText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_EedadText, 10, 0, 1, 1)

        self.ql_EfnacimientoText = QLabel(self.frame_11)
        self.ql_EfnacimientoText.setObjectName(u"ql_EfnacimientoText")
        self.ql_EfnacimientoText.setFont(font1)
        self.ql_EfnacimientoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_EfnacimientoText, 11, 0, 1, 1)

        self.qlinee_EfnacimientoInfo = QLineEdit(self.frame_11)
        self.qlinee_EfnacimientoInfo.setObjectName(u"qlinee_EfnacimientoInfo")
        self.qlinee_EfnacimientoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.qlinee_EfnacimientoInfo, 11, 1, 1, 1)

        self.ql_ElnacimientoText = QLabel(self.frame_11)
        self.ql_ElnacimientoText.setObjectName(u"ql_ElnacimientoText")
        self.ql_ElnacimientoText.setFont(font1)
        self.ql_ElnacimientoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_ElnacimientoText, 13, 0, 1, 1)

        self.qlinee_ElnacimientoInfo = QLineEdit(self.frame_11)
        self.qlinee_ElnacimientoInfo.setObjectName(u"qlinee_ElnacimientoInfo")
        self.qlinee_ElnacimientoInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.qlinee_ElnacimientoInfo, 13, 1, 1, 1)

        self.ql_EestadoText = QLabel(self.frame_11)
        self.ql_EestadoText.setObjectName(u"ql_EestadoText")
        self.ql_EestadoText.setFont(font1)
        self.ql_EestadoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_EestadoText, 4, 4, 1, 1)

        self.cbox_EestadoInfo = QComboBox(self.frame_11)
        self.cbox_EestadoInfo.setObjectName(u"cbox_EestadoInfo")
        self.cbox_EestadoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.cbox_EestadoInfo, 4, 5, 1, 1)

        self.ql_EdireccionText = QLabel(self.frame_11)
        self.ql_EdireccionText.setObjectName(u"ql_EdireccionText")
        self.ql_EdireccionText.setFont(font1)
        self.ql_EdireccionText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_EdireccionText, 7, 4, 1, 1)

        self.qlinee_EdireccionInfo = QLineEdit(self.frame_11)
        self.qlinee_EdireccionInfo.setObjectName(u"qlinee_EdireccionInfo")
        self.qlinee_EdireccionInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.qlinee_EdireccionInfo, 7, 5, 1, 1)

        self.ql_EobservacionesText = QLabel(self.frame_11)
        self.ql_EobservacionesText.setObjectName(u"ql_EobservacionesText")
        self.ql_EobservacionesText.setFont(font1)
        self.ql_EobservacionesText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_EobservacionesText, 8, 4, 1, 1)

        self.qlinee_EobservacionesInfo = QLineEdit(self.frame_11)
        self.qlinee_EobservacionesInfo.setObjectName(u"qlinee_EobservacionesInfo")
        self.qlinee_EobservacionesInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.qlinee_EobservacionesInfo, 8, 5, 1, 1)

        self.ql_ErepresentanteText = QLabel(self.frame_11)
        self.ql_ErepresentanteText.setObjectName(u"ql_ErepresentanteText")
        font3 = QFont()
        font3.setFamily(u"Poppins SemiBold")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.ql_ErepresentanteText.setFont(font3)
        self.ql_ErepresentanteText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_ErepresentanteText, 9, 4, 1, 1)

        self.comboBox = QComboBox(self.frame_11)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.comboBox, 9, 5, 1, 1)

        self.ql_EparentescoText = QLabel(self.frame_11)
        self.ql_EparentescoText.setObjectName(u"ql_EparentescoText")
        self.ql_EparentescoText.setFont(font3)
        self.ql_EparentescoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_EparentescoText, 10, 4, 1, 1)

        self.cbox_EparentescoInfo = QComboBox(self.frame_11)
        self.cbox_EparentescoInfo.setObjectName(u"cbox_EparentescoInfo")
        self.cbox_EparentescoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.cbox_EparentescoInfo, 10, 5, 1, 1)

        self.ql_EgradoseccionText = QLabel(self.frame_11)
        self.ql_EgradoseccionText.setObjectName(u"ql_EgradoseccionText")
        self.ql_EgradoseccionText.setFont(font1)
        self.ql_EgradoseccionText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_EgradoseccionText, 11, 4, 1, 1)

        self.cbox_Egradoseccion = QComboBox(self.frame_11)
        self.cbox_Egradoseccion.setObjectName(u"cbox_Egradoseccion")
        self.cbox_Egradoseccion.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.cbox_Egradoseccion, 11, 5, 1, 1)


        self.gridLayout_4.addWidget(self.frame_11, 1, 0, 1, 1)

        self.tabWidget.addTab(self.qw_Estudiantes, "")
        self.qw_Representantes = QWidget()
        self.qw_Representantes.setObjectName(u"qw_Representantes")
        self.gridLayout_2 = QGridLayout(self.qw_Representantes)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_8 = QFrame(self.qw_Representantes)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"background-color: rgb(85, 90, 95);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_3 = QSpacerItem(274, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_3, 0, 5, 2, 2)

        self.horizontalSpacer_4 = QSpacerItem(275, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_4, 0, 0, 2, 1)

        self.label_19 = QLabel(self.frame_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_8.addWidget(self.label_19, 2, 4, 1, 1)

        self.bttn_Rsalir = QPushButton(self.frame_8)
        self.bttn_Rsalir.setObjectName(u"bttn_Rsalir")
        self.bttn_Rsalir.setCursor(QCursor(Qt.PointingHandCursor))
        self.bttn_Rsalir.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #757a80;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{		\n"
"		color: rgb(255, 255, 255);\n"
"	 	background-color:#333639;\n"
"}")
        self.bttn_Rsalir.setIcon(icon2)
        self.bttn_Rsalir.setIconSize(QSize(50, 50))
        self.bttn_Rsalir.setFlat(True)

        self.gridLayout_8.addWidget(self.bttn_Rsalir, 1, 4, 1, 1)

        self.bttn_Rlimpiar = QPushButton(self.frame_8)
        self.bttn_Rlimpiar.setObjectName(u"bttn_Rlimpiar")
        self.bttn_Rlimpiar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bttn_Rlimpiar.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #757a80;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{		\n"
"		color: rgb(255, 255, 255);\n"
"	 	background-color:#333639;\n"
"}")
        self.bttn_Rlimpiar.setIcon(icon)
        self.bttn_Rlimpiar.setIconSize(QSize(50, 50))
        self.bttn_Rlimpiar.setFlat(True)

        self.gridLayout_8.addWidget(self.bttn_Rlimpiar, 1, 3, 1, 1)

        self.label_15 = QLabel(self.frame_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_8.addWidget(self.label_15, 2, 3, 1, 1)

        self.bttn_Rguardar = QPushButton(self.frame_8)
        self.bttn_Rguardar.setObjectName(u"bttn_Rguardar")
        self.bttn_Rguardar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bttn_Rguardar.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #757a80;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{		\n"
"		color: rgb(255, 255, 255);\n"
"	 	background-color:#333639;\n"
"}")
        self.bttn_Rguardar.setIcon(icon1)
        self.bttn_Rguardar.setIconSize(QSize(50, 50))
        self.bttn_Rguardar.setFlat(True)

        self.gridLayout_8.addWidget(self.bttn_Rguardar, 1, 2, 1, 1)

        self.label_16 = QLabel(self.frame_8)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_8.addWidget(self.label_16, 2, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_8, 3, 0, 1, 1)

        self.line_5 = QFrame(self.qw_Representantes)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 2, 0, 1, 1)

        self.frame_5 = QFrame(self.qw_Representantes)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(85, 90, 95);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ql_Rbasededatos = QLabel(self.frame_5)
        self.ql_Rbasededatos.setObjectName(u"ql_Rbasededatos")
        self.ql_Rbasededatos.setFont(font2)
        self.ql_Rbasededatos.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.ql_Rbasededatos)

        self.ql_Ringresarinfo = QLabel(self.frame_5)
        self.ql_Ringresarinfo.setObjectName(u"ql_Ringresarinfo")
        self.ql_Ringresarinfo.setFont(font2)
        self.ql_Ringresarinfo.setStyleSheet(u"color: rgb(85, 170, 255);")

        self.verticalLayout_2.addWidget(self.ql_Ringresarinfo)


        self.gridLayout_2.addWidget(self.frame_5, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.qw_Representantes)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.qlinee_Rdireccioninfo = QLineEdit(self.frame_7)
        self.qlinee_Rdireccioninfo.setObjectName(u"qlinee_Rdireccioninfo")
        self.qlinee_Rdireccioninfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.qlinee_Rdireccioninfo, 6, 1, 1, 1)

        self.ql_RcedulaText = QLabel(self.frame_7)
        self.ql_RcedulaText.setObjectName(u"ql_RcedulaText")
        self.ql_RcedulaText.setFont(font1)
        self.ql_RcedulaText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.ql_RcedulaText, 4, 0, 1, 1)

        self.ql_RobservacionesText = QLabel(self.frame_7)
        self.ql_RobservacionesText.setObjectName(u"ql_RobservacionesText")
        self.ql_RobservacionesText.setFont(font1)
        self.ql_RobservacionesText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.ql_RobservacionesText, 3, 3, 1, 1)

        self.qlinee_RapellidosInfo = QLineEdit(self.frame_7)
        self.qlinee_RapellidosInfo.setObjectName(u"qlinee_RapellidosInfo")
        self.qlinee_RapellidosInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.qlinee_RapellidosInfo, 3, 1, 1, 1)

        self.line_6 = QFrame(self.frame_7)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line_6, 0, 0, 1, 5)

        self.qlinee_RcedulaInfo = QLineEdit(self.frame_7)
        self.qlinee_RcedulaInfo.setObjectName(u"qlinee_RcedulaInfo")
        self.qlinee_RcedulaInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")
        self.qlinee_RcedulaInfo.setMaxLength(8)

        self.gridLayout_7.addWidget(self.qlinee_RcedulaInfo, 4, 1, 1, 1)

        self.qlinee_RntelefonoInfo = QLineEdit(self.frame_7)
        self.qlinee_RntelefonoInfo.setObjectName(u"qlinee_RntelefonoInfo")
        self.qlinee_RntelefonoInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.qlinee_RntelefonoInfo, 5, 1, 1, 1)

        self.qlinee_RobservacionesInfo = QLineEdit(self.frame_7)
        self.qlinee_RobservacionesInfo.setObjectName(u"qlinee_RobservacionesInfo")
        self.qlinee_RobservacionesInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.qlinee_RobservacionesInfo, 3, 4, 1, 1)

        self.ql_RdireccionText = QLabel(self.frame_7)
        self.ql_RdireccionText.setObjectName(u"ql_RdireccionText")
        self.ql_RdireccionText.setFont(font1)
        self.ql_RdireccionText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.ql_RdireccionText, 6, 0, 1, 1)

        self.qlinee_RdirecciontrabInfo = QLineEdit(self.frame_7)
        self.qlinee_RdirecciontrabInfo.setObjectName(u"qlinee_RdirecciontrabInfo")
        self.qlinee_RdirecciontrabInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.qlinee_RdirecciontrabInfo, 1, 4, 1, 1)

        self.line_4 = QFrame(self.frame_7)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line_4, 1, 2, 7, 1)

        self.ql_RdirecciontrabText = QLabel(self.frame_7)
        self.ql_RdirecciontrabText.setObjectName(u"ql_RdirecciontrabText")
        self.ql_RdirecciontrabText.setFont(font1)
        self.ql_RdirecciontrabText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.ql_RdirecciontrabText, 1, 3, 1, 1)

        self.ql_RntelefonoText = QLabel(self.frame_7)
        self.ql_RntelefonoText.setObjectName(u"ql_RntelefonoText")
        self.ql_RntelefonoText.setFont(font1)
        self.ql_RntelefonoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.ql_RntelefonoText, 5, 0, 1, 1)

        self.ql_RapellidoText = QLabel(self.frame_7)
        self.ql_RapellidoText.setObjectName(u"ql_RapellidoText")
        self.ql_RapellidoText.setFont(font1)
        self.ql_RapellidoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.ql_RapellidoText, 3, 0, 1, 1)

        self.qlinee_RnombreInfo = QLineEdit(self.frame_7)
        self.qlinee_RnombreInfo.setObjectName(u"qlinee_RnombreInfo")
        self.qlinee_RnombreInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.qlinee_RnombreInfo, 1, 1, 1, 1)

        self.ql_RnombreText = QLabel(self.frame_7)
        self.ql_RnombreText.setObjectName(u"ql_RnombreText")
        self.ql_RnombreText.setFont(font1)
        self.ql_RnombreText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.ql_RnombreText, 1, 0, 1, 1)

        self.ql_RestadolabText = QLabel(self.frame_7)
        self.ql_RestadolabText.setObjectName(u"ql_RestadolabText")
        self.ql_RestadolabText.setFont(font1)
        self.ql_RestadolabText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.ql_RestadolabText, 4, 3, 1, 1)

        self.qlinee_estadolabInfo = QLineEdit(self.frame_7)
        self.qlinee_estadolabInfo.setObjectName(u"qlinee_estadolabInfo")
        self.qlinee_estadolabInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.qlinee_estadolabInfo, 4, 4, 1, 1)

        self.ql_RtotalrepreText = QLabel(self.frame_7)
        self.ql_RtotalrepreText.setObjectName(u"ql_RtotalrepreText")
        self.ql_RtotalrepreText.setFont(font1)
        self.ql_RtotalrepreText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.ql_RtotalrepreText, 5, 3, 1, 1)

        self.qlinee_RtotalrepreInfo = QLineEdit(self.frame_7)
        self.qlinee_RtotalrepreInfo.setObjectName(u"qlinee_RtotalrepreInfo")
        self.qlinee_RtotalrepreInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.qlinee_RtotalrepreInfo, 5, 4, 1, 1)


        self.gridLayout_2.addWidget(self.frame_7, 1, 0, 1, 1)

        self.tabWidget.addTab(self.qw_Representantes, "")
        self.qw_Profesores = QWidget()
        self.qw_Profesores.setObjectName(u"qw_Profesores")
        self.gridLayout = QGridLayout(self.qw_Profesores)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.qw_Profesores)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(85, 90, 95);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ql_Pbasededatos = QLabel(self.frame)
        self.ql_Pbasededatos.setObjectName(u"ql_Pbasededatos")
        self.ql_Pbasededatos.setFont(font2)
        self.ql_Pbasededatos.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.ql_Pbasededatos)

        self.ql_Pingresarinfo = QLabel(self.frame)
        self.ql_Pingresarinfo.setObjectName(u"ql_Pingresarinfo")
        self.ql_Pingresarinfo.setFont(font2)
        self.ql_Pingresarinfo.setStyleSheet(u"color: rgb(85, 170, 255);")

        self.verticalLayout.addWidget(self.ql_Pingresarinfo)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.line_2 = QFrame(self.qw_Profesores)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 1)

        self.line_3 = QFrame(self.qw_Profesores)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 2, 0, 1, 1)

        self.frame_4 = QFrame(self.qw_Profesores)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.ql_PsexoText = QLabel(self.frame_4)
        self.ql_PsexoText.setObjectName(u"ql_PsexoText")
        self.ql_PsexoText.setFont(font1)
        self.ql_PsexoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.ql_PsexoText, 5, 0, 1, 1)

        self.qlinee_PnombreInfo = QLineEdit(self.frame_4)
        self.qlinee_PnombreInfo.setObjectName(u"qlinee_PnombreInfo")
        self.qlinee_PnombreInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.qlinee_PnombreInfo, 0, 1, 1, 1)

        self.qlinee_PsexoInfo = QLineEdit(self.frame_4)
        self.qlinee_PsexoInfo.setObjectName(u"qlinee_PsexoInfo")
        self.qlinee_PsexoInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.qlinee_PsexoInfo, 5, 1, 1, 1)

        self.ql_PanosserviText = QLabel(self.frame_4)
        self.ql_PanosserviText.setObjectName(u"ql_PanosserviText")
        self.ql_PanosserviText.setFont(font1)
        self.ql_PanosserviText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.ql_PanosserviText, 0, 3, 1, 1)

        self.qlinee_PanosserviInfo = QLineEdit(self.frame_4)
        self.qlinee_PanosserviInfo.setObjectName(u"qlinee_PanosserviInfo")
        self.qlinee_PanosserviInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.qlinee_PanosserviInfo, 0, 4, 1, 1)

        self.ql_PnombreText = QLabel(self.frame_4)
        self.ql_PnombreText.setObjectName(u"ql_PnombreText")
        self.ql_PnombreText.setFont(font1)
        self.ql_PnombreText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.ql_PnombreText, 0, 0, 1, 1)

        self.ql_PfnacimientoText = QLabel(self.frame_4)
        self.ql_PfnacimientoText.setObjectName(u"ql_PfnacimientoText")
        self.ql_PfnacimientoText.setFont(font1)
        self.ql_PfnacimientoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.ql_PfnacimientoText, 6, 0, 1, 1)

        self.line = QFrame(self.frame_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line, 0, 2, 7, 1)

        self.qlinee_PcedulaInfo = QLineEdit(self.frame_4)
        self.qlinee_PcedulaInfo.setObjectName(u"qlinee_PcedulaInfo")
        self.qlinee_PcedulaInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")
        self.qlinee_PcedulaInfo.setMaxLength(8)

        self.gridLayout_5.addWidget(self.qlinee_PcedulaInfo, 3, 1, 1, 1)

        self.qlinee_PfnacimientoInfo = QLineEdit(self.frame_4)
        self.qlinee_PfnacimientoInfo.setObjectName(u"qlinee_PfnacimientoInfo")
        self.qlinee_PfnacimientoInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.qlinee_PfnacimientoInfo, 6, 1, 1, 1)

        self.ql_PcedulaText = QLabel(self.frame_4)
        self.ql_PcedulaText.setObjectName(u"ql_PcedulaText")
        self.ql_PcedulaText.setFont(font1)
        self.ql_PcedulaText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.ql_PcedulaText, 3, 0, 1, 1)

        self.qlinee_PapellidosInfo = QLineEdit(self.frame_4)
        self.qlinee_PapellidosInfo.setObjectName(u"qlinee_PapellidosInfo")
        self.qlinee_PapellidosInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.qlinee_PapellidosInfo, 2, 1, 1, 1)

        self.ql_PapellidoText = QLabel(self.frame_4)
        self.ql_PapellidoText.setObjectName(u"ql_PapellidoText")
        self.ql_PapellidoText.setFont(font1)
        self.ql_PapellidoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.ql_PapellidoText, 2, 0, 1, 1)

        self.ql_PcodcargoText = QLabel(self.frame_4)
        self.ql_PcodcargoText.setObjectName(u"ql_PcodcargoText")
        self.ql_PcodcargoText.setFont(font1)
        self.ql_PcodcargoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.ql_PcodcargoText, 2, 3, 1, 1)

        self.qlinee_PcodcargoInfo = QLineEdit(self.frame_4)
        self.qlinee_PcodcargoInfo.setObjectName(u"qlinee_PcodcargoInfo")
        self.qlinee_PcodcargoInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.qlinee_PcodcargoInfo, 2, 4, 1, 1)

        self.ql_PntelefonoText = QLabel(self.frame_4)
        self.ql_PntelefonoText.setObjectName(u"ql_PntelefonoText")
        self.ql_PntelefonoText.setFont(font1)
        self.ql_PntelefonoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.ql_PntelefonoText, 5, 3, 1, 1)

        self.qlinee_PntelefonoInfo = QLineEdit(self.frame_4)
        self.qlinee_PntelefonoInfo.setObjectName(u"qlinee_PntelefonoInfo")
        self.qlinee_PntelefonoInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.qlinee_PntelefonoInfo, 5, 4, 1, 1)

        self.ql_PcoddepenText = QLabel(self.frame_4)
        self.ql_PcoddepenText.setObjectName(u"ql_PcoddepenText")
        self.ql_PcoddepenText.setFont(font1)
        self.ql_PcoddepenText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.ql_PcoddepenText, 3, 3, 1, 1)

        self.qlinee_PcoddepenInfo = QLineEdit(self.frame_4)
        self.qlinee_PcoddepenInfo.setObjectName(u"qlinee_PcoddepenInfo")
        self.qlinee_PcoddepenInfo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.qlinee_PcoddepenInfo, 3, 4, 1, 1)

        self.ql_PgradodocText = QLabel(self.frame_4)
        self.ql_PgradodocText.setObjectName(u"ql_PgradodocText")
        self.ql_PgradodocText.setFont(font1)
        self.ql_PgradodocText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.ql_PgradodocText, 6, 3, 1, 1)

        self.qcbox_PgradodocInfo = QComboBox(self.frame_4)
        self.qcbox_PgradodocInfo.addItem("")
        self.qcbox_PgradodocInfo.addItem("")
        self.qcbox_PgradodocInfo.addItem("")
        self.qcbox_PgradodocInfo.addItem("")
        self.qcbox_PgradodocInfo.addItem("")
        self.qcbox_PgradodocInfo.addItem("")
        self.qcbox_PgradodocInfo.addItem("")
        self.qcbox_PgradodocInfo.setObjectName(u"qcbox_PgradodocInfo")
        self.qcbox_PgradodocInfo.setCursor(QCursor(Qt.PointingHandCursor))
        self.qcbox_PgradodocInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qcbox_PgradodocInfo.setEditable(False)
        self.qcbox_PgradodocInfo.setDuplicatesEnabled(False)

        self.gridLayout_5.addWidget(self.qcbox_PgradodocInfo, 6, 4, 1, 1)


        self.gridLayout.addWidget(self.frame_4, 4, 0, 1, 1)

        self.frame_6 = QFrame(self.qw_Profesores)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(85, 90, 95);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 0, 2, 1)

        self.bttn_Psalir = QPushButton(self.frame_6)
        self.bttn_Psalir.setObjectName(u"bttn_Psalir")
        self.bttn_Psalir.setCursor(QCursor(Qt.PointingHandCursor))
        self.bttn_Psalir.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #757a80;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{		\n"
"		color: rgb(255, 255, 255);\n"
"	 	background-color:#333639;\n"
"}")
        self.bttn_Psalir.setIcon(icon2)
        self.bttn_Psalir.setIconSize(QSize(50, 50))
        self.bttn_Psalir.setFlat(True)

        self.gridLayout_6.addWidget(self.bttn_Psalir, 0, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)

        self.bttn_Pguardar = QPushButton(self.frame_6)
        self.bttn_Pguardar.setObjectName(u"bttn_Pguardar")
        self.bttn_Pguardar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bttn_Pguardar.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #757a80;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{		\n"
"		color: rgb(255, 255, 255);\n"
"	 	background-color:#333639;\n"
"}")
        self.bttn_Pguardar.setIcon(icon1)
        self.bttn_Pguardar.setIconSize(QSize(50, 50))
        self.bttn_Pguardar.setFlat(True)

        self.gridLayout_6.addWidget(self.bttn_Pguardar, 0, 1, 1, 1)

        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.label_13, 1, 1, 1, 1)

        self.bttn_Plimpiar = QPushButton(self.frame_6)
        self.bttn_Plimpiar.setObjectName(u"bttn_Plimpiar")
        self.bttn_Plimpiar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bttn_Plimpiar.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #757a80;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{		\n"
"		color: rgb(255, 255, 255);\n"
"	 	background-color:#333639;\n"
"}")
        self.bttn_Plimpiar.setIcon(icon)
        self.bttn_Plimpiar.setIconSize(QSize(50, 50))
        self.bttn_Plimpiar.setFlat(True)

        self.gridLayout_6.addWidget(self.bttn_Plimpiar, 0, 2, 1, 1)

        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.label_14, 1, 2, 1, 1)

        self.label_20 = QLabel(self.frame_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_6.addWidget(self.label_20, 1, 4, 1, 1)


        self.gridLayout.addWidget(self.frame_6, 6, 0, 1, 1)

        self.tabWidget.addTab(self.qw_Profesores, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        QWidget.setTabOrder(self.qlinee_EcedulaInfo, self.qlinee_EnombreInfo)
        QWidget.setTabOrder(self.qlinee_EnombreInfo, self.qlinee_EapellidosInfo)
        QWidget.setTabOrder(self.qlinee_EapellidosInfo, self.qlinee_EsexoInfo)
        QWidget.setTabOrder(self.qlinee_EsexoInfo, self.qlinee_EedadInfo)
        QWidget.setTabOrder(self.qlinee_EedadInfo, self.bttn_Eguardar)
        QWidget.setTabOrder(self.bttn_Eguardar, self.bttn_Elimpiar)
        QWidget.setTabOrder(self.bttn_Elimpiar, self.bttn_Salir)
        QWidget.setTabOrder(self.bttn_Salir, self.qlinee_RnombreInfo)
        QWidget.setTabOrder(self.qlinee_RnombreInfo, self.qlinee_RapellidosInfo)
        QWidget.setTabOrder(self.qlinee_RapellidosInfo, self.qlinee_RcedulaInfo)
        QWidget.setTabOrder(self.qlinee_RcedulaInfo, self.qlinee_RntelefonoInfo)
        QWidget.setTabOrder(self.qlinee_RntelefonoInfo, self.qlinee_Rdireccioninfo)
        QWidget.setTabOrder(self.qlinee_Rdireccioninfo, self.qlinee_RdirecciontrabInfo)
        QWidget.setTabOrder(self.qlinee_RdirecciontrabInfo, self.qlinee_RobservacionesInfo)
        QWidget.setTabOrder(self.qlinee_RobservacionesInfo, self.qlinee_estadolabInfo)
        QWidget.setTabOrder(self.qlinee_estadolabInfo, self.qlinee_RtotalrepreInfo)
        QWidget.setTabOrder(self.qlinee_RtotalrepreInfo, self.qlinee_PnombreInfo)
        QWidget.setTabOrder(self.qlinee_PnombreInfo, self.qlinee_PapellidosInfo)
        QWidget.setTabOrder(self.qlinee_PapellidosInfo, self.qlinee_PcedulaInfo)
        QWidget.setTabOrder(self.qlinee_PcedulaInfo, self.qlinee_PsexoInfo)
        QWidget.setTabOrder(self.qlinee_PsexoInfo, self.qlinee_PfnacimientoInfo)
        QWidget.setTabOrder(self.qlinee_PfnacimientoInfo, self.bttn_Psalir)

        self.retranslateUi(AnadirDatos)
        self.bttn_Rlimpiar.clicked.connect(self.qlinee_RtotalrepreInfo.clear)
        self.bttn_Rlimpiar.clicked.connect(self.qlinee_RcedulaInfo.clear)
        self.bttn_Rlimpiar.clicked.connect(self.qlinee_RapellidosInfo.clear)
        self.bttn_Rlimpiar.clicked.connect(self.qlinee_RnombreInfo.clear)
        self.bttn_Rlimpiar.clicked.connect(self.qlinee_RobservacionesInfo.clear)
        self.bttn_Rlimpiar.clicked.connect(self.qlinee_RdirecciontrabInfo.clear)
        self.bttn_Rlimpiar.clicked.connect(self.qlinee_Rdireccioninfo.clear)
        self.bttn_Rlimpiar.clicked.connect(self.qlinee_RntelefonoInfo.clear)
        self.bttn_Salir.clicked.connect(AnadirDatos.close)
        self.bttn_Rlimpiar.clicked.connect(self.qlinee_estadolabInfo.clear)
        self.bttn_Elimpiar.clicked.connect(self.qlinee_EfnacimientoInfo.clear)
        self.bttn_Elimpiar.clicked.connect(self.qlinee_EedadInfo.clear)
        self.bttn_Elimpiar.clicked.connect(self.qlinee_EsexoInfo.clear)
        self.bttn_Elimpiar.clicked.connect(self.qlinee_EcedulaInfo.clear)
        self.bttn_Elimpiar.clicked.connect(self.qlinee_EapellidosInfo.clear)
        self.bttn_Elimpiar.clicked.connect(self.qlinee_EnombreInfo.clear)
        self.bttn_Elimpiar.clicked.connect(self.qlinee_EobservacionesInfo.clear)
        self.bttn_Elimpiar.clicked.connect(self.qlinee_EdireccionInfo.clear)
        self.bttn_Elimpiar.clicked.connect(self.qlinee_ElnacimientoInfo.clear)
        self.bttn_Rsalir.clicked.connect(AnadirDatos.close)
        self.bttn_Plimpiar.clicked.connect(self.qlinee_PapellidosInfo.clear)
        self.bttn_Plimpiar.clicked.connect(self.qlinee_PcodcargoInfo.clear)
        self.bttn_Plimpiar.clicked.connect(self.qlinee_PanosserviInfo.clear)
        self.bttn_Plimpiar.clicked.connect(self.qlinee_PcedulaInfo.clear)
        self.bttn_Plimpiar.clicked.connect(self.qlinee_PnombreInfo.clear)
        self.bttn_Plimpiar.clicked.connect(self.qlinee_PntelefonoInfo.clear)
        self.bttn_Plimpiar.clicked.connect(self.qlinee_PfnacimientoInfo.clear)
        self.bttn_Plimpiar.clicked.connect(self.qlinee_PsexoInfo.clear)
        self.bttn_Plimpiar.clicked.connect(self.qlinee_PcoddepenInfo.clear)
        self.bttn_Psalir.clicked.connect(AnadirDatos.close)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AnadirDatos)
    # setupUi

    def retranslateUi(self, AnadirDatos):
        AnadirDatos.setWindowTitle(QCoreApplication.translate("AnadirDatos", u"INGRESO DE DATOS", None))
        self.label_18.setText(QCoreApplication.translate("AnadirDatos", u"<html><head/><body><p align=\"center\">Guardar</p></body></html>", None))
        self.bttn_Elimpiar.setText("")
        self.bttn_Eguardar.setText("")
        self.label_2.setText(QCoreApplication.translate("AnadirDatos", u"<html><head/><body><p align=\"center\">Salir</p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("AnadirDatos", u"<html><head/><body><p align=\"center\">Limpiar</p></body></html>", None))
        self.bttn_Salir.setText("")
        self.ql_Ebasededatos.setText(QCoreApplication.translate("AnadirDatos", u"<html><head/><body><p align=\"center\">BASE DE DATOS</p></body></html>", None))
        self.ql_Eingresarinfo.setText(QCoreApplication.translate("AnadirDatos", u"<html><head/><body><p align=\"center\">INGRESE LA INFORMACION RESPECTIVA DEL ESTUDIANTES</p></body></html>", None))
        self.qlinee_EapellidosInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"APELLIDO", None))
        self.ql_EnombreText.setText(QCoreApplication.translate("AnadirDatos", u"Nombres", None))
        self.qlinee_EnombreInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"NOMBRE", None))
        self.qlinee_EcedulaInfo.setInputMask(QCoreApplication.translate("AnadirDatos", u"99999999", None))
        self.qlinee_EcedulaInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"12345678", None))
        self.ql_EapellidoText.setText(QCoreApplication.translate("AnadirDatos", u"Apellidos", None))
        self.qlinee_EedadInfo.setInputMask(QCoreApplication.translate("AnadirDatos", u"99", None))
        self.qlinee_EedadInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"1", None))
        self.qlinee_EsexoInfo.setInputMask(QCoreApplication.translate("AnadirDatos", u"A", None))
        self.qlinee_EsexoInfo.setText("")
        self.qlinee_EsexoInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"M / F", None))
        self.ql_EsexoText.setText(QCoreApplication.translate("AnadirDatos", u"Sexo", None))
        self.ql_EcedulaText.setText(QCoreApplication.translate("AnadirDatos", u"Cedula", None))
        self.ql_EedadText.setText(QCoreApplication.translate("AnadirDatos", u"Edad", None))
        self.ql_EfnacimientoText.setText(QCoreApplication.translate("AnadirDatos", u"F.Nacimiento", None))
        self.qlinee_EfnacimientoInfo.setInputMask(QCoreApplication.translate("AnadirDatos", u"99/99/9999", None))
        self.qlinee_EfnacimientoInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"DD/MM/AAAA", None))
        self.ql_ElnacimientoText.setText(QCoreApplication.translate("AnadirDatos", u"L.Nacimiento", None))
        self.qlinee_ElnacimientoInfo.setInputMask("")
        self.qlinee_ElnacimientoInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"Maracay, Monta\u00f1a Fresca...", None))
        self.ql_EestadoText.setText(QCoreApplication.translate("AnadirDatos", u"Estado", None))
        self.ql_EdireccionText.setText(QCoreApplication.translate("AnadirDatos", u"Direccion", None))
        self.qlinee_EdireccionInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"Maracay, Limon...", None))
        self.ql_EobservacionesText.setText(QCoreApplication.translate("AnadirDatos", u"Observaciones", None))
        self.qlinee_EobservacionesInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"Observaciones", None))
        self.ql_ErepresentanteText.setText(QCoreApplication.translate("AnadirDatos", u"Representante", None))
        self.ql_EparentescoText.setText(QCoreApplication.translate("AnadirDatos", u"Pentesco", None))
        self.ql_EgradoseccionText.setText(QCoreApplication.translate("AnadirDatos", u"Grado-Secci\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.qw_Estudiantes), QCoreApplication.translate("AnadirDatos", u"Estudiantes", None))
        self.label_19.setText(QCoreApplication.translate("AnadirDatos", u"<html><head/><body><p align=\"center\">Salir</p></body></html>", None))
        self.bttn_Rsalir.setText("")
        self.bttn_Rlimpiar.setText("")
        self.label_15.setText(QCoreApplication.translate("AnadirDatos", u"<html><head/><body><p align=\"center\">Limpiar</p></body></html>", None))
        self.bttn_Rguardar.setText("")
        self.label_16.setText(QCoreApplication.translate("AnadirDatos", u"<html><head/><body><p align=\"center\">Guardar</p></body></html>", None))
        self.ql_Rbasededatos.setText(QCoreApplication.translate("AnadirDatos", u"<html><head/><body><p align=\"center\">BASE DE DATOS</p></body></html>", None))
        self.ql_Ringresarinfo.setText(QCoreApplication.translate("AnadirDatos", u"<html><head/><body><p align=\"center\">INGRESE LA INFORMACION RESPECTIVA DEL REPRESENTANTE</p></body></html>", None))
        self.qlinee_Rdireccioninfo.setInputMask("")
        self.qlinee_Rdireccioninfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"Maracay, Monta\u00f1a Fresca...", None))
        self.ql_RcedulaText.setText(QCoreApplication.translate("AnadirDatos", u"Cedula", None))
        self.ql_RobservacionesText.setText(QCoreApplication.translate("AnadirDatos", u"Observaciones", None))
        self.qlinee_RapellidosInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"APELLIDO", None))
        self.qlinee_RcedulaInfo.setInputMask(QCoreApplication.translate("AnadirDatos", u"99999999", None))
        self.qlinee_RcedulaInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"12345678", None))
        self.qlinee_RntelefonoInfo.setInputMask(QCoreApplication.translate("AnadirDatos", u"(9999)-9999999", None))
        self.qlinee_RntelefonoInfo.setText(QCoreApplication.translate("AnadirDatos", u"()-", None))
        self.qlinee_RntelefonoInfo.setPlaceholderText("")
        self.qlinee_RobservacionesInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"Observaciones", None))
        self.ql_RdireccionText.setText(QCoreApplication.translate("AnadirDatos", u"Direccion", None))
        self.qlinee_RdirecciontrabInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"Maracay, Limon...", None))
        self.ql_RdirecciontrabText.setText(QCoreApplication.translate("AnadirDatos", u"Direccion de Trabajo", None))
        self.ql_RntelefonoText.setText(QCoreApplication.translate("AnadirDatos", u"Telefono", None))
        self.ql_RapellidoText.setText(QCoreApplication.translate("AnadirDatos", u"Apellidos", None))
        self.qlinee_RnombreInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"NOMBRE", None))
        self.ql_RnombreText.setText(QCoreApplication.translate("AnadirDatos", u"Nombres", None))
        self.ql_RestadolabText.setText(QCoreApplication.translate("AnadirDatos", u"Estado Laboral", None))
        self.qlinee_estadolabInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"Activo/Retirado", None))
        self.ql_RtotalrepreText.setText(QCoreApplication.translate("AnadirDatos", u"Total de Representados", None))
        self.qlinee_RtotalrepreInfo.setInputMask(QCoreApplication.translate("AnadirDatos", u"99", None))
        self.qlinee_RtotalrepreInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.qw_Representantes), QCoreApplication.translate("AnadirDatos", u"Representantes", None))
        self.ql_Pbasededatos.setText(QCoreApplication.translate("AnadirDatos", u"<html><head/><body><p align=\"center\">BASE DE DATOS</p></body></html>", None))
        self.ql_Pingresarinfo.setText(QCoreApplication.translate("AnadirDatos", u"<html><head/><body><p align=\"center\">INGRESE LA INFORMACION RESPECTIVA DEL DOCENTE</p></body></html>", None))
        self.ql_PsexoText.setText(QCoreApplication.translate("AnadirDatos", u"Sexo", None))
        self.qlinee_PnombreInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"NOMBRE", None))
        self.qlinee_PsexoInfo.setInputMask(QCoreApplication.translate("AnadirDatos", u"A", None))
        self.qlinee_PsexoInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"M / F", None))
        self.ql_PanosserviText.setText(QCoreApplication.translate("AnadirDatos", u"A\u00f1os de servicios", None))
        self.qlinee_PanosserviInfo.setInputMask(QCoreApplication.translate("AnadirDatos", u"99", None))
        self.qlinee_PanosserviInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"10", None))
        self.ql_PnombreText.setText(QCoreApplication.translate("AnadirDatos", u"Nombres", None))
        self.ql_PfnacimientoText.setText(QCoreApplication.translate("AnadirDatos", u"F.Nacimiento", None))
        self.qlinee_PcedulaInfo.setInputMask(QCoreApplication.translate("AnadirDatos", u"99999999", None))
        self.qlinee_PcedulaInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"12345678", None))
        self.qlinee_PfnacimientoInfo.setInputMask(QCoreApplication.translate("AnadirDatos", u"99/99/9999", None))
        self.qlinee_PfnacimientoInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"DD/MM/AAAA", None))
        self.ql_PcedulaText.setText(QCoreApplication.translate("AnadirDatos", u"Cedula", None))
        self.qlinee_PapellidosInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"APELLIDO", None))
        self.ql_PapellidoText.setText(QCoreApplication.translate("AnadirDatos", u"Apellidos", None))
        self.ql_PcodcargoText.setText(QCoreApplication.translate("AnadirDatos", u"Codigo de cargo", None))
        self.qlinee_PcodcargoInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"1125DB", None))
        self.ql_PntelefonoText.setText(QCoreApplication.translate("AnadirDatos", u"Telefono", None))
        self.qlinee_PntelefonoInfo.setInputMask(QCoreApplication.translate("AnadirDatos", u"(9999)-9999999", None))
        self.qlinee_PntelefonoInfo.setText(QCoreApplication.translate("AnadirDatos", u"()-", None))
        self.qlinee_PntelefonoInfo.setPlaceholderText("")
        self.ql_PcoddepenText.setText(QCoreApplication.translate("AnadirDatos", u"Codigo de dependencia", None))
        self.qlinee_PcoddepenInfo.setPlaceholderText(QCoreApplication.translate("AnadirDatos", u"121300", None))
        self.ql_PgradodocText.setText(QCoreApplication.translate("AnadirDatos", u"Grado del docente", None))
        self.qcbox_PgradodocInfo.setItemText(0, QCoreApplication.translate("AnadirDatos", u"Preescolar", None))
        self.qcbox_PgradodocInfo.setItemText(1, QCoreApplication.translate("AnadirDatos", u"1er Grado", None))
        self.qcbox_PgradodocInfo.setItemText(2, QCoreApplication.translate("AnadirDatos", u"2er Grado", None))
        self.qcbox_PgradodocInfo.setItemText(3, QCoreApplication.translate("AnadirDatos", u"3er Grado", None))
        self.qcbox_PgradodocInfo.setItemText(4, QCoreApplication.translate("AnadirDatos", u"4to Grado", None))
        self.qcbox_PgradodocInfo.setItemText(5, QCoreApplication.translate("AnadirDatos", u"5to Grado", None))
        self.qcbox_PgradodocInfo.setItemText(6, QCoreApplication.translate("AnadirDatos", u"6to Grado", None))

        self.bttn_Psalir.setText("")
        self.bttn_Pguardar.setText("")
        self.label_13.setText(QCoreApplication.translate("AnadirDatos", u"<html><head/><body><p align=\"center\">Guardar</p></body></html>", None))
        self.bttn_Plimpiar.setText("")
        self.label_14.setText(QCoreApplication.translate("AnadirDatos", u"<html><head/><body><p align=\"center\">Limpiar</p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("AnadirDatos", u"<html><head/><body><p align=\"center\">Salir</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.qw_Profesores), QCoreApplication.translate("AnadirDatos", u"Profesores", None))
    # retranslateUi

