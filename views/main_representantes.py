# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_representantes.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import views.resource_rc

class Ui_Representantes(object):
    def setupUi(self, Representantes):
        if not Representantes.objectName():
            Representantes.setObjectName(u"Representantes")
        Representantes.setWindowModality(Qt.WindowModal)
        Representantes.resize(813, 960)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Representantes.sizePolicy().hasHeightForWidth())
        Representantes.setSizePolicy(sizePolicy)
        Representantes.setStyleSheet(u"background-color: rgb(51, 54, 57);")
        self.gridLayout_2 = QGridLayout(Representantes)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.CentralWidget = QGridLayout()
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.line = QFrame(Representantes)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.CentralWidget.addWidget(self.line, 1, 0, 1, 1)

        self.FootFrame = QFrame(Representantes)
        self.FootFrame.setObjectName(u"FootFrame")
        self.FootFrame.setStyleSheet(u"background-color: rgb(85, 90, 95);")
        self.FootFrame.setFrameShape(QFrame.StyledPanel)
        self.FootFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.FootFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.bttn_Rrefrescar = QPushButton(self.FootFrame)
        self.bttn_Rrefrescar.setObjectName(u"bttn_Rrefrescar")
        icon = QIcon()
        icon.addFile(u":/Botones salida/refresh-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bttn_Rrefrescar.setIcon(icon)
        self.bttn_Rrefrescar.setIconSize(QSize(50, 50))
        self.bttn_Rrefrescar.setFlat(True)

        self.gridLayout_7.addWidget(self.bttn_Rrefrescar, 0, 0, 1, 1)

        self.textimprimir = QLabel(self.FootFrame)
        self.textimprimir.setObjectName(u"textimprimir")
        font = QFont()
        font.setFamily(u"Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textimprimir.setFont(font)
        self.textimprimir.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.textimprimir, 1, 1, 1, 1)

        self.textrefrescar = QLabel(self.FootFrame)
        self.textrefrescar.setObjectName(u"textrefrescar")
        self.textrefrescar.setFont(font)
        self.textrefrescar.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.textrefrescar, 1, 0, 1, 1)

        self.bttn_Rimprimir = QPushButton(self.FootFrame)
        self.bttn_Rimprimir.setObjectName(u"bttn_Rimprimir")
        icon1 = QIcon()
        icon1.addFile(u":/Botones salida/imprimir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bttn_Rimprimir.setIcon(icon1)
        self.bttn_Rimprimir.setIconSize(QSize(50, 50))
        self.bttn_Rimprimir.setFlat(True)

        self.gridLayout_7.addWidget(self.bttn_Rimprimir, 0, 1, 1, 1)

        self.bttnRsalir = QPushButton(self.FootFrame)
        self.bttnRsalir.setObjectName(u"bttnRsalir")
        icon2 = QIcon()
        icon2.addFile(u":/Botones salida/salir_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bttnRsalir.setIcon(icon2)
        self.bttnRsalir.setIconSize(QSize(50, 50))
        self.bttnRsalir.setFlat(True)

        self.gridLayout_7.addWidget(self.bttnRsalir, 0, 2, 1, 1)

        self.textsalir = QLabel(self.FootFrame)
        self.textsalir.setObjectName(u"textsalir")
        self.textsalir.setFont(font)
        self.textsalir.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.textsalir, 1, 2, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.CentralWidget.addWidget(self.FootFrame, 4, 0, 1, 1)

        self.Headframe = QFrame(Representantes)
        self.Headframe.setObjectName(u"Headframe")
        self.Headframe.setFrameShape(QFrame.StyledPanel)
        self.Headframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.Headframe)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.Headframe)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(85, 90, 95);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ql_RcedulaSearch = QLabel(self.frame)
        self.ql_RcedulaSearch.setObjectName(u"ql_RcedulaSearch")
        font1 = QFont()
        font1.setFamily(u"Poppins")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.ql_RcedulaSearch.setFont(font1)
        self.ql_RcedulaSearch.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.ql_RcedulaSearch)

        self.qlinee_RcedulaSearch = QLineEdit(self.frame)
        self.qlinee_RcedulaSearch.setObjectName(u"qlinee_RcedulaSearch")
        self.qlinee_RcedulaSearch.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.qlinee_RcedulaSearch)


        self.gridLayout_8.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ql_RnombreSearch = QLabel(self.frame)
        self.ql_RnombreSearch.setObjectName(u"ql_RnombreSearch")
        self.ql_RnombreSearch.setFont(font1)
        self.ql_RnombreSearch.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.ql_RnombreSearch)

        self.qlinee_RnombreSearch = QLineEdit(self.frame)
        self.qlinee_RnombreSearch.setObjectName(u"qlinee_RnombreSearch")
        self.qlinee_RnombreSearch.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.qlinee_RnombreSearch)


        self.gridLayout_8.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.bttn_Rbuscar = QPushButton(self.frame)
        self.bttn_Rbuscar.setObjectName(u"bttn_Rbuscar")
        icon3 = QIcon()
        icon3.addFile(u":/Botones salida/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bttn_Rbuscar.setIcon(icon3)
        self.bttn_Rbuscar.setIconSize(QSize(50, 50))
        self.bttn_Rbuscar.setFlat(False)

        self.gridLayout_8.addWidget(self.bttn_Rbuscar, 3, 1, 3, 1)

        self.ql_RescribanombresText = QLabel(self.frame)
        self.ql_RescribanombresText.setObjectName(u"ql_RescribanombresText")
        self.ql_RescribanombresText.setFont(font1)
        self.ql_RescribanombresText.setStyleSheet(u"color: rgb(85, 170, 255);")

        self.gridLayout_8.addWidget(self.ql_RescribanombresText, 2, 0, 1, 2)

        self.ql_RbuscarbaseText = QLabel(self.frame)
        self.ql_RbuscarbaseText.setObjectName(u"ql_RbuscarbaseText")
        self.ql_RbuscarbaseText.setFont(font1)
        self.ql_RbuscarbaseText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_8.addWidget(self.ql_RbuscarbaseText, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.CentralWidget.addWidget(self.Headframe, 0, 0, 1, 1)

        self.line_2 = QFrame(Representantes)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.CentralWidget.addWidget(self.line_2, 3, 0, 1, 1)

        self.BodyFrame = QFrame(Representantes)
        self.BodyFrame.setObjectName(u"BodyFrame")
        self.BodyFrame.setMaximumSize(QSize(16777215, 16777215))
        self.BodyFrame.setFrameShape(QFrame.StyledPanel)
        self.BodyFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.BodyFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.qlinee_RnombresInfo = QLineEdit(self.BodyFrame)
        self.qlinee_RnombresInfo.setObjectName(u"qlinee_RnombresInfo")
        self.qlinee_RnombresInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_RnombresInfo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.qlinee_RnombresInfo, 0, 2, 1, 1)

        self.qlinee_RapellidosInfo = QLineEdit(self.BodyFrame)
        self.qlinee_RapellidosInfo.setObjectName(u"qlinee_RapellidosInfo")
        self.qlinee_RapellidosInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_RapellidosInfo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.qlinee_RapellidosInfo, 1, 2, 1, 1)

        self.ql_RcedulaText = QLabel(self.BodyFrame)
        self.ql_RcedulaText.setObjectName(u"ql_RcedulaText")
        self.ql_RcedulaText.setFont(font)
        self.ql_RcedulaText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.ql_RcedulaText, 2, 0, 1, 1)

        self.ql_RapellidosText = QLabel(self.BodyFrame)
        self.ql_RapellidosText.setObjectName(u"ql_RapellidosText")
        self.ql_RapellidosText.setFont(font)
        self.ql_RapellidosText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.ql_RapellidosText, 1, 0, 1, 1)

        self.ql_RnombresText = QLabel(self.BodyFrame)
        self.ql_RnombresText.setObjectName(u"ql_RnombresText")
        self.ql_RnombresText.setFont(font)
        self.ql_RnombresText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.ql_RnombresText, 0, 0, 1, 1)

        self.qlinee_RcedulaInfo = QLineEdit(self.BodyFrame)
        self.qlinee_RcedulaInfo.setObjectName(u"qlinee_RcedulaInfo")
        self.qlinee_RcedulaInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_RcedulaInfo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.qlinee_RcedulaInfo, 2, 2, 1, 1)

        self.qlinee_RntelefonoInfo = QLineEdit(self.BodyFrame)
        self.qlinee_RntelefonoInfo.setObjectName(u"qlinee_RntelefonoInfo")
        self.qlinee_RntelefonoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_RntelefonoInfo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.qlinee_RntelefonoInfo, 3, 2, 1, 1)

        self.ql_RntelefonoText = QLabel(self.BodyFrame)
        self.ql_RntelefonoText.setObjectName(u"ql_RntelefonoText")
        self.ql_RntelefonoText.setFont(font)
        self.ql_RntelefonoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.ql_RntelefonoText, 3, 0, 1, 1)

        self.qlinee_RtotalrepreInfo = QLineEdit(self.BodyFrame)
        self.qlinee_RtotalrepreInfo.setObjectName(u"qlinee_RtotalrepreInfo")
        self.qlinee_RtotalrepreInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_RtotalrepreInfo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.qlinee_RtotalrepreInfo, 4, 2, 1, 1)

        self.ql_RtotalrepreText = QLabel(self.BodyFrame)
        self.ql_RtotalrepreText.setObjectName(u"ql_RtotalrepreText")
        self.ql_RtotalrepreText.setFont(font)
        self.ql_RtotalrepreText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.ql_RtotalrepreText, 4, 0, 1, 1)

        self.qlinee_RparentescoInfo = QLineEdit(self.BodyFrame)
        self.qlinee_RparentescoInfo.setObjectName(u"qlinee_RparentescoInfo")
        self.qlinee_RparentescoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_RparentescoInfo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.qlinee_RparentescoInfo, 5, 2, 1, 1)

        self.ql_RparentescoText = QLabel(self.BodyFrame)
        self.ql_RparentescoText.setObjectName(u"ql_RparentescoText")
        self.ql_RparentescoText.setFont(font)
        self.ql_RparentescoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.ql_RparentescoText, 5, 0, 1, 1)

        self.qlinee_RestadolabInfo = QLineEdit(self.BodyFrame)
        self.qlinee_RestadolabInfo.setObjectName(u"qlinee_RestadolabInfo")
        self.qlinee_RestadolabInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_RestadolabInfo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.qlinee_RestadolabInfo, 6, 2, 1, 1)

        self.ql_RestadoLabText = QLabel(self.BodyFrame)
        self.ql_RestadoLabText.setObjectName(u"ql_RestadoLabText")
        self.ql_RestadoLabText.setFont(font)
        self.ql_RestadoLabText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.ql_RestadoLabText, 6, 0, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_4)

        self.line_3 = QFrame(self.BodyFrame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_3)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.qpte_RdireccionInfo = QPlainTextEdit(self.BodyFrame)
        self.qpte_RdireccionInfo.setObjectName(u"qpte_RdireccionInfo")
        self.qpte_RdireccionInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_10.addWidget(self.qpte_RdireccionInfo, 2, 2, 1, 1)

        self.ql_RobservacionesText = QLabel(self.BodyFrame)
        self.ql_RobservacionesText.setObjectName(u"ql_RobservacionesText")
        self.ql_RobservacionesText.setFont(font)
        self.ql_RobservacionesText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_10.addWidget(self.ql_RobservacionesText, 4, 1, 1, 1)

        self.qpte_RobservacionesInfo = QPlainTextEdit(self.BodyFrame)
        self.qpte_RobservacionesInfo.setObjectName(u"qpte_RobservacionesInfo")
        self.qpte_RobservacionesInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_10.addWidget(self.qpte_RobservacionesInfo, 4, 2, 1, 1)

        self.ql_RdireccionText = QLabel(self.BodyFrame)
        self.ql_RdireccionText.setObjectName(u"ql_RdireccionText")
        self.ql_RdireccionText.setFont(font)
        self.ql_RdireccionText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_10.addWidget(self.ql_RdireccionText, 2, 1, 1, 1)

        self.qpte_RdirecciontrabajoInfo = QPlainTextEdit(self.BodyFrame)
        self.qpte_RdirecciontrabajoInfo.setObjectName(u"qpte_RdirecciontrabajoInfo")
        self.qpte_RdirecciontrabajoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_10.addWidget(self.qpte_RdirecciontrabajoInfo, 3, 2, 1, 1)

        self.ql_RdireccionTrabText = QLabel(self.BodyFrame)
        self.ql_RdireccionTrabText.setObjectName(u"ql_RdireccionTrabText")
        self.ql_RdireccionTrabText.setFont(font)
        self.ql_RdireccionTrabText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_10.addWidget(self.ql_RdireccionTrabText, 3, 1, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_10)


        self.CentralWidget.addWidget(self.BodyFrame, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.CentralWidget, 0, 0, 1, 1)


        self.retranslateUi(Representantes)
        self.bttn_Rrefrescar.clicked.connect(self.qpte_RdireccionInfo.clear)
        self.bttn_Rrefrescar.clicked.connect(self.qlinee_RntelefonoInfo.clear)
        self.bttn_Rrefrescar.clicked.connect(self.qlinee_RcedulaInfo.clear)
        self.bttn_Rrefrescar.clicked.connect(self.qlinee_RapellidosInfo.clear)
        self.bttn_Rrefrescar.clicked.connect(self.qlinee_RnombresInfo.clear)
        self.bttn_Rrefrescar.clicked.connect(self.qlinee_RcedulaSearch.clear)
        self.bttn_Rrefrescar.clicked.connect(self.qlinee_RnombreSearch.clear)
        self.bttn_Rrefrescar.clicked.connect(self.qlinee_RtotalrepreInfo.clear)
        self.bttn_Rrefrescar.clicked.connect(self.qlinee_RparentescoInfo.clear)
        self.bttn_Rrefrescar.clicked.connect(self.qlinee_RestadolabInfo.clear)
        self.bttn_Rrefrescar.clicked.connect(self.qpte_RdirecciontrabajoInfo.clear)
        self.bttn_Rrefrescar.clicked.connect(self.qpte_RobservacionesInfo.clear)
        self.qlinee_RnombreSearch.textEdited.connect(self.qlinee_RcedulaSearch.clear)
        self.qlinee_RcedulaSearch.textEdited.connect(self.qlinee_RnombreSearch.clear)

        QMetaObject.connectSlotsByName(Representantes)
    # setupUi

    def retranslateUi(self, Representantes):
        Representantes.setWindowTitle(QCoreApplication.translate("Representantes", u"Representantes", None))
        self.bttn_Rrefrescar.setText("")
        self.textimprimir.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\">Imprimir</p></body></html>", None))
        self.textrefrescar.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\">Refrescar</p></body></html>", None))
        self.bttn_Rimprimir.setText("")
        self.bttnRsalir.setText("")
        self.textsalir.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\">Salir</p></body></html>", None))
        self.ql_RcedulaSearch.setText(QCoreApplication.translate("Representantes", u"C\u00e9dula", None))
        self.qlinee_RcedulaSearch.setPlaceholderText(QCoreApplication.translate("Representantes", u"                   Introduce la cedula para mostrar la informacion", None))
        self.ql_RnombreSearch.setText(QCoreApplication.translate("Representantes", u"Nombre", None))
        self.qlinee_RnombreSearch.setPlaceholderText(QCoreApplication.translate("Representantes", u"                   Introduce el nombre del representante para mostrar", None))
        self.bttn_Rbuscar.setText("")
        self.ql_RescribanombresText.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">INFORMACION PARA BUSCAR INFORMACION DEL REPRESENTANTE</span></p></body></html>", None))
        self.ql_RbuscarbaseText.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\">BUSCAR EN LA BASE DE DATOS</p></body></html>", None))
        self.ql_RcedulaText.setText(QCoreApplication.translate("Representantes", u"Cedula", None))
        self.ql_RapellidosText.setText(QCoreApplication.translate("Representantes", u"Apellidos", None))
        self.ql_RnombresText.setText(QCoreApplication.translate("Representantes", u"Nombres", None))
        self.qlinee_RntelefonoInfo.setInputMask(QCoreApplication.translate("Representantes", u"(9999)-9999999", None))
        self.ql_RntelefonoText.setText(QCoreApplication.translate("Representantes", u"Telefono", None))
        self.ql_RtotalrepreText.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\">Total de Representados</p></body></html>", None))
        self.qlinee_RparentescoInfo.setText("")
        self.ql_RparentescoText.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p>Parentesco</p></body></html>", None))
        self.ql_RestadoLabText.setText(QCoreApplication.translate("Representantes", u"Estado Laboral", None))
        self.ql_RobservacionesText.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\">Observaciones</p></body></html>", None))
        self.ql_RdireccionText.setText(QCoreApplication.translate("Representantes", u"Direcci\u00f3n", None))
        self.ql_RdireccionTrabText.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\">Direcci\u00f3n Trabajo</p></body></html>", None))
    # retranslateUi

