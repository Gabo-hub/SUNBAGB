# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_estudiantes.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import views.resource_rc

class Ui_Estudiantes(object):
    def setupUi(self, Estudiantes):
        if not Estudiantes.objectName():
            Estudiantes.setObjectName(u"Estudiantes")
        Estudiantes.setWindowModality(Qt.WindowModal)
        Estudiantes.resize(837, 649)
        Estudiantes.setMouseTracking(False)
        Estudiantes.setAcceptDrops(False)
        Estudiantes.setStyleSheet(u"background-color: rgb(51, 54, 57);")
        self.gridLayout_9 = QGridLayout(Estudiantes)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.widget = QWidget(Estudiantes)
        self.widget.setObjectName(u"widget")
        self.gridLayout_10 = QGridLayout(self.widget)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.headframe = QFrame(self.widget)
        self.headframe.setObjectName(u"headframe")
        self.headframe.setStyleSheet(u"background-color: rgb(85, 90, 95);")
        self.headframe.setFrameShape(QFrame.StyledPanel)
        self.headframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.headframe)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.internalframe = QGridLayout()
        self.internalframe.setObjectName(u"internalframe")
        self.internalframe.setContentsMargins(10, -1, -1, -1)
        self.bttn_verestudiantes = QToolButton(self.headframe)
        self.bttn_verestudiantes.setObjectName(u"bttn_verestudiantes")

        self.internalframe.addWidget(self.bttn_verestudiantes, 3, 1, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.qlinee_EcedulaSearch = QLineEdit(self.headframe)
        self.qlinee_EcedulaSearch.setObjectName(u"qlinee_EcedulaSearch")
        self.qlinee_EcedulaSearch.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.qlinee_EcedulaSearch, 0, 1, 1, 1)

        self.ql_EcedulaSearch = QLabel(self.headframe)
        self.ql_EcedulaSearch.setObjectName(u"ql_EcedulaSearch")
        font = QFont()
        font.setFamily(u"Poppins")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ql_EcedulaSearch.setFont(font)
        self.ql_EcedulaSearch.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.ql_EcedulaSearch, 0, 0, 1, 1, Qt.AlignLeft)


        self.internalframe.addLayout(self.gridLayout_5, 8, 0, 1, 1)

        self.ql_EescribanombresText = QLabel(self.headframe)
        self.ql_EescribanombresText.setObjectName(u"ql_EescribanombresText")
        palette = QPalette()
        brush = QBrush(QColor(85, 170, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(85, 90, 95, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(85, 170, 255, 128))
        brush2.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(85, 170, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush4 = QBrush(QColor(85, 170, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.ql_EescribanombresText.setPalette(palette)
        self.ql_EescribanombresText.setFont(font)
        self.ql_EescribanombresText.setStyleSheet(u"color: rgb(85, 170, 255);")

        self.internalframe.addWidget(self.ql_EescribanombresText, 4, 0, 1, 2)

        self.ql_EbuscarbaseText = QLabel(self.headframe)
        self.ql_EbuscarbaseText.setObjectName(u"ql_EbuscarbaseText")
        self.ql_EbuscarbaseText.setFont(font)
        self.ql_EbuscarbaseText.setAutoFillBackground(False)
        self.ql_EbuscarbaseText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.internalframe.addWidget(self.ql_EbuscarbaseText, 3, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.ql_EnombreSearch = QLabel(self.headframe)
        self.ql_EnombreSearch.setObjectName(u"ql_EnombreSearch")
        self.ql_EnombreSearch.setFont(font)
        self.ql_EnombreSearch.setStyleSheet(u"color: rgb(255, 255,255);")

        self.gridLayout_7.addWidget(self.ql_EnombreSearch, 0, 0, 3, 1)

        self.qlinee_EnombreSearch = QLineEdit(self.headframe)
        self.qlinee_EnombreSearch.setObjectName(u"qlinee_EnombreSearch")
        self.qlinee_EnombreSearch.setLayoutDirection(Qt.LeftToRight)
        self.qlinee_EnombreSearch.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_EnombreSearch.setMaxLength(32767)
        self.qlinee_EnombreSearch.setFrame(True)
        self.qlinee_EnombreSearch.setClearButtonEnabled(False)

        self.gridLayout_7.addWidget(self.qlinee_EnombreSearch, 0, 1, 3, 1)


        self.internalframe.addLayout(self.gridLayout_7, 7, 0, 1, 1)

        self.bttn_Ebuscar = QPushButton(self.headframe)
        self.bttn_Ebuscar.setObjectName(u"bttn_Ebuscar")
        self.bttn_Ebuscar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bttn_Ebuscar.setMouseTracking(False)
        self.bttn_Ebuscar.setFocusPolicy(Qt.StrongFocus)
        self.bttn_Ebuscar.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #757a80;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#333639;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Botones salida/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bttn_Ebuscar.setIcon(icon)
        self.bttn_Ebuscar.setIconSize(QSize(50, 50))
        self.bttn_Ebuscar.setCheckable(False)
        self.bttn_Ebuscar.setAutoRepeat(False)
        self.bttn_Ebuscar.setAutoExclusive(False)
        self.bttn_Ebuscar.setFlat(False)

        self.internalframe.addWidget(self.bttn_Ebuscar, 7, 1, 3, 1)


        self.gridLayout_6.addLayout(self.internalframe, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.headframe, 0, 0, 1, 1)

        self.bodyframe = QFrame(self.widget)
        self.bodyframe.setObjectName(u"bodyframe")
        self.bodyframe.setFrameShape(QFrame.StyledPanel)
        self.bodyframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.bodyframe)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.line = QFrame(self.bodyframe)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_8.addWidget(self.line, 0, 0, 1, 3)

        self.line_2 = QFrame(self.bodyframe)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_8.addWidget(self.line_2, 2, 1, 2, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, -1, -1, -1)
        self.qlinee_EfnacimientoInfo = QLineEdit(self.bodyframe)
        self.qlinee_EfnacimientoInfo.setObjectName(u"qlinee_EfnacimientoInfo")
        self.qlinee_EfnacimientoInfo.setEnabled(True)
        self.qlinee_EfnacimientoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_EfnacimientoInfo.setReadOnly(True)

        self.gridLayout.addWidget(self.qlinee_EfnacimientoInfo, 4, 4, 1, 2)

        self.ql_EsexoText = QLabel(self.bodyframe)
        self.ql_EsexoText.setObjectName(u"ql_EsexoText")
        font1 = QFont()
        font1.setFamily(u"Poppins")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.ql_EsexoText.setFont(font1)
        self.ql_EsexoText.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ql_EsexoText.setTextFormat(Qt.AutoText)
        self.ql_EsexoText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ql_EsexoText, 3, 0, 1, 1)

        self.qlinee_EsexoInfo = QLineEdit(self.bodyframe)
        self.qlinee_EsexoInfo.setObjectName(u"qlinee_EsexoInfo")
        self.qlinee_EsexoInfo.setEnabled(True)
        self.qlinee_EsexoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_EsexoInfo.setReadOnly(True)

        self.gridLayout.addWidget(self.qlinee_EsexoInfo, 3, 1, 1, 3)

        self.qlinee_EnombresInfo = QLineEdit(self.bodyframe)
        self.qlinee_EnombresInfo.setObjectName(u"qlinee_EnombresInfo")
        self.qlinee_EnombresInfo.setEnabled(True)
        self.qlinee_EnombresInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_EnombresInfo.setReadOnly(True)

        self.gridLayout.addWidget(self.qlinee_EnombresInfo, 1, 2, 1, 4)

        self.qlinee_ElnacimientoInfo = QLineEdit(self.bodyframe)
        self.qlinee_ElnacimientoInfo.setObjectName(u"qlinee_ElnacimientoInfo")
        self.qlinee_ElnacimientoInfo.setEnabled(True)
        self.qlinee_ElnacimientoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_ElnacimientoInfo.setReadOnly(True)

        self.gridLayout.addWidget(self.qlinee_ElnacimientoInfo, 6, 3, 1, 3)

        self.qlinee_EcedulaInfo = QLineEdit(self.bodyframe)
        self.qlinee_EcedulaInfo.setObjectName(u"qlinee_EcedulaInfo")
        self.qlinee_EcedulaInfo.setEnabled(True)
        self.qlinee_EcedulaInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_EcedulaInfo.setFrame(True)
        self.qlinee_EcedulaInfo.setEchoMode(QLineEdit.Normal)
        self.qlinee_EcedulaInfo.setDragEnabled(False)
        self.qlinee_EcedulaInfo.setReadOnly(True)
        self.qlinee_EcedulaInfo.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.qlinee_EcedulaInfo, 0, 2, 1, 4)

        self.ql_EapellidosText = QLabel(self.bodyframe)
        self.ql_EapellidosText.setObjectName(u"ql_EapellidosText")
        self.ql_EapellidosText.setFont(font1)
        self.ql_EapellidosText.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ql_EapellidosText.setTextFormat(Qt.AutoText)
        self.ql_EapellidosText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ql_EapellidosText, 2, 0, 1, 2)

        self.qlinee_EapellidosInfo = QLineEdit(self.bodyframe)
        self.qlinee_EapellidosInfo.setObjectName(u"qlinee_EapellidosInfo")
        self.qlinee_EapellidosInfo.setEnabled(True)
        self.qlinee_EapellidosInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_EapellidosInfo.setReadOnly(True)

        self.gridLayout.addWidget(self.qlinee_EapellidosInfo, 2, 2, 1, 4)

        self.ql_EfnacimientoText = QLabel(self.bodyframe)
        self.ql_EfnacimientoText.setObjectName(u"ql_EfnacimientoText")
        self.ql_EfnacimientoText.setFont(font1)
        self.ql_EfnacimientoText.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ql_EfnacimientoText.setTextFormat(Qt.AutoText)
        self.ql_EfnacimientoText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ql_EfnacimientoText, 4, 0, 1, 4, Qt.AlignLeft)

        self.ql_EcedulaText = QLabel(self.bodyframe)
        self.ql_EcedulaText.setObjectName(u"ql_EcedulaText")
        self.ql_EcedulaText.setFont(font1)
        self.ql_EcedulaText.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ql_EcedulaText.setTextFormat(Qt.AutoText)
        self.ql_EcedulaText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ql_EcedulaText, 0, 0, 1, 2, Qt.AlignLeft)

        self.qlinee_EedadInfo = QLineEdit(self.bodyframe)
        self.qlinee_EedadInfo.setObjectName(u"qlinee_EedadInfo")
        self.qlinee_EedadInfo.setEnabled(True)
        self.qlinee_EedadInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_EedadInfo.setReadOnly(True)

        self.gridLayout.addWidget(self.qlinee_EedadInfo, 3, 5, 1, 1)

        self.ql_EestadosText = QLabel(self.bodyframe)
        self.ql_EestadosText.setObjectName(u"ql_EestadosText")
        self.ql_EestadosText.setFont(font1)
        self.ql_EestadosText.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ql_EestadosText.setTextFormat(Qt.AutoText)
        self.ql_EestadosText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ql_EestadosText, 5, 0, 1, 2, Qt.AlignLeft)

        self.qlinee_EestadoInfo = QLineEdit(self.bodyframe)
        self.qlinee_EestadoInfo.setObjectName(u"qlinee_EestadoInfo")
        self.qlinee_EestadoInfo.setEnabled(True)
        self.qlinee_EestadoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_EestadoInfo.setReadOnly(True)

        self.gridLayout.addWidget(self.qlinee_EestadoInfo, 5, 2, 1, 4)

        self.ql_ElnacimientoText = QLabel(self.bodyframe)
        self.ql_ElnacimientoText.setObjectName(u"ql_ElnacimientoText")
        self.ql_ElnacimientoText.setFont(font1)
        self.ql_ElnacimientoText.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ql_ElnacimientoText.setTextFormat(Qt.AutoText)
        self.ql_ElnacimientoText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ql_ElnacimientoText, 6, 0, 1, 3, Qt.AlignLeft)

        self.ql_EnombresText = QLabel(self.bodyframe)
        self.ql_EnombresText.setObjectName(u"ql_EnombresText")
        self.ql_EnombresText.setFont(font1)
        self.ql_EnombresText.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ql_EnombresText.setTextFormat(Qt.AutoText)
        self.ql_EnombresText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ql_EnombresText, 1, 0, 1, 2)

        self.ql_EedadText = QLabel(self.bodyframe)
        self.ql_EedadText.setObjectName(u"ql_EedadText")
        self.ql_EedadText.setFont(font1)
        self.ql_EedadText.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ql_EedadText.setTextFormat(Qt.AutoText)
        self.ql_EedadText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ql_EedadText, 3, 4, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout, 2, 0, 2, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ql_EdireccionText = QLabel(self.bodyframe)
        self.ql_EdireccionText.setObjectName(u"ql_EdireccionText")
        self.ql_EdireccionText.setFont(font1)
        self.ql_EdireccionText.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ql_EdireccionText.setTextFormat(Qt.AutoText)
        self.ql_EdireccionText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.ql_EdireccionText, 0, 0, 1, 1)

        self.qpte_EdireccionInfo = QPlainTextEdit(self.bodyframe)
        self.qpte_EdireccionInfo.setObjectName(u"qpte_EdireccionInfo")
        self.qpte_EdireccionInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qpte_EdireccionInfo.setReadOnly(True)

        self.gridLayout_2.addWidget(self.qpte_EdireccionInfo, 0, 1, 1, 1)

        self.ql_EtobservacionText = QLabel(self.bodyframe)
        self.ql_EtobservacionText.setObjectName(u"ql_EtobservacionText")
        self.ql_EtobservacionText.setFont(font1)
        self.ql_EtobservacionText.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ql_EtobservacionText.setTextFormat(Qt.AutoText)
        self.ql_EtobservacionText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.ql_EtobservacionText, 1, 0, 1, 1)

        self.qpte_EobservacionesInfo = QPlainTextEdit(self.bodyframe)
        self.qpte_EobservacionesInfo.setObjectName(u"qpte_EobservacionesInfo")
        self.qpte_EobservacionesInfo.setEnabled(True)
        self.qpte_EobservacionesInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qpte_EobservacionesInfo.setFrameShape(QFrame.StyledPanel)
        self.qpte_EobservacionesInfo.setFrameShadow(QFrame.Sunken)
        self.qpte_EobservacionesInfo.setReadOnly(True)

        self.gridLayout_2.addWidget(self.qpte_EobservacionesInfo, 1, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_2, 3, 2, 1, 1)

        self.line_3 = QFrame(self.bodyframe)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_8.addWidget(self.line_3, 5, 0, 1, 3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, -1, -1, -1)
        self.ql_EntelefonicoText = QLabel(self.bodyframe)
        self.ql_EntelefonicoText.setObjectName(u"ql_EntelefonicoText")
        self.ql_EntelefonicoText.setFont(font1)
        self.ql_EntelefonicoText.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ql_EntelefonicoText.setTextFormat(Qt.AutoText)
        self.ql_EntelefonicoText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.ql_EntelefonicoText, 2, 0, 1, 2, Qt.AlignLeft)

        self.ql_EparentescoText = QLabel(self.bodyframe)
        self.ql_EparentescoText.setObjectName(u"ql_EparentescoText")
        self.ql_EparentescoText.setFont(font1)
        self.ql_EparentescoText.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ql_EparentescoText.setTextFormat(Qt.AutoText)
        self.ql_EparentescoText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.ql_EparentescoText, 1, 0, 1, 2, Qt.AlignLeft)

        self.ql_EgradoseccionInfo = QLineEdit(self.bodyframe)
        self.ql_EgradoseccionInfo.setObjectName(u"ql_EgradoseccionInfo")
        self.ql_EgradoseccionInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.ql_EgradoseccionInfo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.ql_EgradoseccionInfo, 3, 3, 1, 1)

        self.qlinee_ErepresentanteInfo = QLineEdit(self.bodyframe)
        self.qlinee_ErepresentanteInfo.setObjectName(u"qlinee_ErepresentanteInfo")
        self.qlinee_ErepresentanteInfo.setEnabled(True)
        self.qlinee_ErepresentanteInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_ErepresentanteInfo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.qlinee_ErepresentanteInfo, 0, 3, 1, 1)

        self.qlinee_EparentescoInfo = QLineEdit(self.bodyframe)
        self.qlinee_EparentescoInfo.setObjectName(u"qlinee_EparentescoInfo")
        self.qlinee_EparentescoInfo.setEnabled(True)
        self.qlinee_EparentescoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_EparentescoInfo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.qlinee_EparentescoInfo, 1, 3, 1, 1)

        self.qlinee_EntelefonicoInfo = QLineEdit(self.bodyframe)
        self.qlinee_EntelefonicoInfo.setObjectName(u"qlinee_EntelefonicoInfo")
        self.qlinee_EntelefonicoInfo.setEnabled(True)
        self.qlinee_EntelefonicoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.qlinee_EntelefonicoInfo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.qlinee_EntelefonicoInfo, 2, 3, 1, 1)

        self.ql_ErepresentanteText = QLabel(self.bodyframe)
        self.ql_ErepresentanteText.setObjectName(u"ql_ErepresentanteText")
        self.ql_ErepresentanteText.setFont(font1)
        self.ql_ErepresentanteText.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ql_ErepresentanteText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.ql_ErepresentanteText, 0, 0, 1, 3, Qt.AlignLeft)

        self.ql_EgradoseccionText = QLabel(self.bodyframe)
        self.ql_EgradoseccionText.setObjectName(u"ql_EgradoseccionText")
        self.ql_EgradoseccionText.setFont(font1)
        self.ql_EgradoseccionText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.ql_EgradoseccionText, 3, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_4, 2, 2, 1, 1)


        self.gridLayout_10.addWidget(self.bodyframe, 1, 0, 1, 1)

        self.footerframe = QFrame(self.widget)
        self.footerframe.setObjectName(u"footerframe")
        self.footerframe.setStyleSheet(u"background-color: rgb(85, 90, 95);")
        self.footerframe.setFrameShape(QFrame.StyledPanel)
        self.footerframe.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.footerframe)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.bttn_Erimprimir = QPushButton(self.footerframe)
        self.bttn_Erimprimir.setObjectName(u"bttn_Erimprimir")
        self.bttn_Erimprimir.setCursor(QCursor(Qt.PointingHandCursor))
        self.bttn_Erimprimir.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #757a80;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#333639;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Botones salida/imprimir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bttn_Erimprimir.setIcon(icon1)
        self.bttn_Erimprimir.setIconSize(QSize(81, 61))
        self.bttn_Erimprimir.setFlat(True)

        self.gridLayout_3.addWidget(self.bttn_Erimprimir, 0, 1, 1, 1)

        self.bttn_Erefrescar = QPushButton(self.footerframe)
        self.bttn_Erefrescar.setObjectName(u"bttn_Erefrescar")
        self.bttn_Erefrescar.setCursor(QCursor(Qt.PointingHandCursor))
        self.bttn_Erefrescar.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #757a80;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#333639;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Botones salida/refresh-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bttn_Erefrescar.setIcon(icon2)
        self.bttn_Erefrescar.setIconSize(QSize(81, 61))
        self.bttn_Erefrescar.setFlat(True)

        self.gridLayout_3.addWidget(self.bttn_Erefrescar, 0, 0, 1, 1)

        self.ql_EsalirText = QLabel(self.footerframe)
        self.ql_EsalirText.setObjectName(u"ql_EsalirText")
        font2 = QFont()
        font2.setFamily(u"Poppins")
        font2.setBold(True)
        font2.setWeight(75)
        self.ql_EsalirText.setFont(font2)
        self.ql_EsalirText.setCursor(QCursor(Qt.IBeamCursor))
        self.ql_EsalirText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.ql_EsalirText, 1, 2, 1, 1)

        self.ql_EimprimirText = QLabel(self.footerframe)
        self.ql_EimprimirText.setObjectName(u"ql_EimprimirText")
        self.ql_EimprimirText.setFont(font2)
        self.ql_EimprimirText.setCursor(QCursor(Qt.IBeamCursor))
        self.ql_EimprimirText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.ql_EimprimirText, 1, 1, 1, 1)

        self.ql_ErefrescarText = QLabel(self.footerframe)
        self.ql_ErefrescarText.setObjectName(u"ql_ErefrescarText")
        self.ql_ErefrescarText.setFont(font2)
        self.ql_ErefrescarText.setCursor(QCursor(Qt.IBeamCursor))
        self.ql_ErefrescarText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.ql_ErefrescarText, 1, 0, 1, 1)

        self.bttn_Esalir = QPushButton(self.footerframe)
        self.bttn_Esalir.setObjectName(u"bttn_Esalir")
        self.bttn_Esalir.setCursor(QCursor(Qt.PointingHandCursor))
        self.bttn_Esalir.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: #757a80;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#333639;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Botones salida/salir_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bttn_Esalir.setIcon(icon3)
        self.bttn_Esalir.setIconSize(QSize(81, 61))
        self.bttn_Esalir.setFlat(True)

        self.gridLayout_3.addWidget(self.bttn_Esalir, 0, 2, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_10.addWidget(self.footerframe, 2, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget, 0, 0, 1, 1)

#if QT_CONFIG(shortcut)
        self.ql_EsalirText.setBuddy(self.bttn_Erefrescar)
        self.ql_EimprimirText.setBuddy(self.bttn_Erefrescar)
        self.ql_ErefrescarText.setBuddy(self.bttn_Erefrescar)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Estudiantes)
        self.bttn_Erefrescar.clicked.connect(self.qpte_EobservacionesInfo.clear)
        self.bttn_Erefrescar.clicked.connect(self.qlinee_ErepresentanteInfo.clear)
        self.bttn_Erefrescar.clicked.connect(self.qlinee_EntelefonicoInfo.clear)
        self.bttn_Erefrescar.clicked.connect(self.qlinee_EparentescoInfo.clear)
        self.bttn_Erefrescar.clicked.connect(self.qlinee_EedadInfo.clear)
        self.bttn_Erefrescar.clicked.connect(self.qlinee_EcedulaInfo.clear)
        self.bttn_Erefrescar.clicked.connect(self.qlinee_EestadoInfo.clear)
        self.bttn_Erefrescar.clicked.connect(self.qlinee_EsexoInfo.clear)
        self.bttn_Erefrescar.clicked.connect(self.qlinee_EnombresInfo.clear)
        self.bttn_Erefrescar.clicked.connect(self.qlinee_EfnacimientoInfo.clear)
        self.bttn_Erefrescar.clicked.connect(self.qlinee_ElnacimientoInfo.clear)
        self.bttn_Erefrescar.clicked.connect(self.qlinee_EapellidosInfo.clear)
        self.bttn_Erefrescar.clicked.connect(self.qlinee_EnombreSearch.clear)
        self.qlinee_EcedulaSearch.textEdited.connect(self.qlinee_EnombreSearch.clear)
        self.qlinee_EnombreSearch.textEdited.connect(self.qlinee_EcedulaSearch.clear)
        self.bttn_Erefrescar.clicked.connect(self.qlinee_EcedulaSearch.clear)
        self.qlinee_EnombreSearch.returnPressed.connect(self.bttn_Ebuscar.setFocus)
        self.bttn_Erefrescar.clicked.connect(self.qpte_EdireccionInfo.clear)

        QMetaObject.connectSlotsByName(Estudiantes)
    # setupUi

    def retranslateUi(self, Estudiantes):
        Estudiantes.setWindowTitle(QCoreApplication.translate("Estudiantes", u"Estudiantes", None))
        self.bttn_verestudiantes.setText(QCoreApplication.translate("Estudiantes", u"Ver Estudiantes", None))
        self.qlinee_EcedulaSearch.setInputMask("")
        self.qlinee_EcedulaSearch.setPlaceholderText(QCoreApplication.translate("Estudiantes", u"                   Introduce la cedula para mostrar", None))
        self.ql_EcedulaSearch.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">C\u00e9dula</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.ql_EescribanombresText.setToolTip(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p>Escriba los dos nombres y los apellidos en ese orden</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ql_EescribanombresText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">ESCRIBA LOS NOMBRES Y LOS APELLIDOS DEL ESTUDIANTE EN ESE ORDEN</span></p></body></html>", None))
        self.ql_EbuscarbaseText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">BUSCAR EN LA BASE DE DATOS</span></p></body></html>", None))
        self.ql_EnombreSearch.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p><span style=\" font-weight:600;\">Nombre</span></p></body></html>", None))
        self.qlinee_EnombreSearch.setInputMask("")
        self.qlinee_EnombreSearch.setText("")
        self.qlinee_EnombreSearch.setPlaceholderText(QCoreApplication.translate("Estudiantes", u"                   Introduce el nombre del estudiante para mostrar", None))
        self.bttn_Ebuscar.setText("")
        self.qlinee_EfnacimientoInfo.setInputMask(QCoreApplication.translate("Estudiantes", u"99/99/9999", None))
        self.qlinee_EfnacimientoInfo.setText(QCoreApplication.translate("Estudiantes", u"//", None))
        self.ql_EsexoText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p>Sexo</p></body></html>", None))
        self.qlinee_EsexoInfo.setText("")
        self.qlinee_EnombresInfo.setText("")
        self.qlinee_ElnacimientoInfo.setText("")
        self.qlinee_EcedulaInfo.setText("")
        self.ql_EapellidosText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p>Apellidos</p></body></html>", None))
        self.qlinee_EapellidosInfo.setText("")
        self.ql_EfnacimientoText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p>F.Nacimiento</p></body></html>", None))
        self.ql_EcedulaText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p>C\u00e9dula</p></body></html>", None))
        self.qlinee_EedadInfo.setText("")
        self.ql_EestadosText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p>Estado</p></body></html>", None))
        self.qlinee_EestadoInfo.setText("")
        self.ql_ElnacimientoText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p>L.Nacimiento</p></body></html>", None))
        self.ql_EnombresText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p>Nombres</p></body></html>", None))
        self.ql_EedadText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p>Edad</p></body></html>", None))
        self.ql_EdireccionText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p>Direcci\u00f3n</p></body></html>", None))
        self.qpte_EdireccionInfo.setPlainText("")
        self.ql_EtobservacionText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p>Observaciones</p></body></html>", None))
        self.qpte_EobservacionesInfo.setPlainText("")
        self.ql_EntelefonicoText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p>N. Telefonico</p></body></html>", None))
        self.ql_EparentescoText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p>Parentesco</p></body></html>", None))
        self.qlinee_ErepresentanteInfo.setText("")
        self.qlinee_EparentescoInfo.setText("")
        self.qlinee_EntelefonicoInfo.setInputMask(QCoreApplication.translate("Estudiantes", u"(9999) -999999", None))
        self.qlinee_EntelefonicoInfo.setText(QCoreApplication.translate("Estudiantes", u"() -", None))
        self.ql_ErepresentanteText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p>Representante</p></body></html>", None))
        self.ql_EgradoseccionText.setText(QCoreApplication.translate("Estudiantes", u"Grado y Secci\u00f3n", None))
        self.bttn_Erimprimir.setText("")
        self.bttn_Erefrescar.setText("")
        self.ql_EsalirText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SALIR</span></p></body></html>", None))
        self.ql_EimprimirText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">IMPRIMIR</span></p></body></html>", None))
        self.ql_ErefrescarText.setText(QCoreApplication.translate("Estudiantes", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">REFRESCAR</span></p></body></html>", None))
        self.bttn_Esalir.setText("")
    # retranslateUi

