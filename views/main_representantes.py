# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_representantesMbsZDI.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)
import views.resource_rc

class Ui_Representantes(object):
    def setupUi(self, Representantes):
        if not Representantes.objectName():
            Representantes.setObjectName(u"Representantes")
        Representantes.setWindowModality(Qt.WindowModality.WindowModal)
        Representantes.resize(840, 551)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
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
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.CentralWidget.addWidget(self.line, 1, 0, 1, 1)

        self.FootFrame = QFrame(Representantes)
        self.FootFrame.setObjectName(u"FootFrame")
        self.FootFrame.setMaximumSize(QSize(16777215, 115))
        self.FootFrame.setStyleSheet(u"background-color: rgb(85, 90, 95);")
        self.FootFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.FootFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.FootFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.textrefrescar = QLabel(self.FootFrame)
        self.textrefrescar.setObjectName(u"textrefrescar")
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(10)
        font.setBold(True)
        self.textrefrescar.setFont(font)
        self.textrefrescar.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.textrefrescar, 1, 0, 1, 1)

        self.bttn_Rrefrescar = QPushButton(self.FootFrame)
        self.bttn_Rrefrescar.setObjectName(u"bttn_Rrefrescar")
        self.bttn_Rrefrescar.setStyleSheet(u"QPushButton:hover\n"
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
        icon.addFile(u":/Botones salida/refresh-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bttn_Rrefrescar.setIcon(icon)
        self.bttn_Rrefrescar.setIconSize(QSize(50, 50))
        self.bttn_Rrefrescar.setFlat(True)

        self.gridLayout_7.addWidget(self.bttn_Rrefrescar, 0, 0, 1, 1)

        self.bttn_editar = QPushButton(self.FootFrame)
        self.bttn_editar.setObjectName(u"bttn_editar")
        self.bttn_editar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bttn_editar.setStyleSheet(u"QPushButton:hover\n"
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
        icon1.addFile(u":/Botones salida/edit-book.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bttn_editar.setIcon(icon1)
        self.bttn_editar.setIconSize(QSize(81, 61))
        self.bttn_editar.setFlat(True)

        self.gridLayout_7.addWidget(self.bttn_editar, 0, 1, 1, 1)

        self.label = QLabel(self.FootFrame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.label.setMouseTracking(True)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.label, 1, 1, 1, 1)

        self.bttn_Rimprimir = QPushButton(self.FootFrame)
        self.bttn_Rimprimir.setObjectName(u"bttn_Rimprimir")
        self.bttn_Rimprimir.setStyleSheet(u"QPushButton:hover\n"
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
        icon2.addFile(u":/Botones salida/imprimir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bttn_Rimprimir.setIcon(icon2)
        self.bttn_Rimprimir.setIconSize(QSize(50, 50))
        self.bttn_Rimprimir.setFlat(True)

        self.gridLayout_7.addWidget(self.bttn_Rimprimir, 0, 2, 1, 1)

        self.textimprimir = QLabel(self.FootFrame)
        self.textimprimir.setObjectName(u"textimprimir")
        self.textimprimir.setFont(font)
        self.textimprimir.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.textimprimir, 1, 2, 1, 1)

        self.bttnRsalir = QPushButton(self.FootFrame)
        self.bttnRsalir.setObjectName(u"bttnRsalir")
        self.bttnRsalir.setStyleSheet(u"QPushButton:hover\n"
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
        icon3.addFile(u":/Botones salida/salir_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bttnRsalir.setIcon(icon3)
        self.bttnRsalir.setIconSize(QSize(50, 50))
        self.bttnRsalir.setFlat(True)

        self.gridLayout_7.addWidget(self.bttnRsalir, 0, 3, 1, 1)

        self.textsalir = QLabel(self.FootFrame)
        self.textsalir.setObjectName(u"textsalir")
        self.textsalir.setFont(font)
        self.textsalir.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.textsalir, 1, 3, 1, 1)

        self.bttn_guardar = QPushButton(self.FootFrame)
        self.bttn_guardar.setObjectName(u"bttn_guardar")
        self.bttn_guardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bttn_guardar.setStyleSheet(u"QPushButton:hover\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/Botones salida/save-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bttn_guardar.setIcon(icon4)
        self.bttn_guardar.setIconSize(QSize(50, 50))
        self.bttn_guardar.setFlat(True)

        self.gridLayout_7.addWidget(self.bttn_guardar, 0, 4, 1, 1)

        self.ql_guardarText = QLabel(self.FootFrame)
        self.ql_guardarText.setObjectName(u"ql_guardarText")
        self.ql_guardarText.setFont(font)
        self.ql_guardarText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.ql_guardarText, 1, 4, 1, 1)

        self.bttn_cancelar = QPushButton(self.FootFrame)
        self.bttn_cancelar.setObjectName(u"bttn_cancelar")
        self.bttn_cancelar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bttn_cancelar.setStyleSheet(u"QPushButton:hover\n"
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
        icon5 = QIcon()
        icon5.addFile(u":/Botones salida/icon-park--close-one.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bttn_cancelar.setIcon(icon5)
        self.bttn_cancelar.setIconSize(QSize(50, 50))
        self.bttn_cancelar.setFlat(True)

        self.gridLayout_7.addWidget(self.bttn_cancelar, 0, 5, 1, 1)

        self.ql_cancelarText = QLabel(self.FootFrame)
        self.ql_cancelarText.setObjectName(u"ql_cancelarText")
        self.ql_cancelarText.setFont(font)
        self.ql_cancelarText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.ql_cancelarText, 1, 5, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.CentralWidget.addWidget(self.FootFrame, 4, 0, 1, 1)

        self.Headframe = QFrame(Representantes)
        self.Headframe.setObjectName(u"Headframe")
        self.Headframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.Headframe.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.Headframe)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.Headframe)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(85, 90, 95);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ql_RbuscarbaseText = QLabel(self.frame)
        self.ql_RbuscarbaseText.setObjectName(u"ql_RbuscarbaseText")
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.ql_RbuscarbaseText.setFont(font2)
        self.ql_RbuscarbaseText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.ql_RbuscarbaseText)

        self.ql_RescribanombresText = QLabel(self.frame)
        self.ql_RescribanombresText.setObjectName(u"ql_RescribanombresText")
        self.ql_RescribanombresText.setFont(font2)
        self.ql_RescribanombresText.setStyleSheet(u"color: rgb(85, 170, 255);")

        self.verticalLayout_2.addWidget(self.ql_RescribanombresText)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.bttn_verrepresentantes = QToolButton(self.frame)
        self.bttn_verrepresentantes.setObjectName(u"bttn_verrepresentantes")
        self.bttn_verrepresentantes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.bttn_verrepresentantes)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ql_RnombreSearch = QLabel(self.frame)
        self.ql_RnombreSearch.setObjectName(u"ql_RnombreSearch")
        self.ql_RnombreSearch.setFont(font2)
        self.ql_RnombreSearch.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.ql_RnombreSearch)

        self.qlinee_RnombreSearch = QLineEdit(self.frame)
        self.qlinee_RnombreSearch.setObjectName(u"qlinee_RnombreSearch")
        self.qlinee_RnombreSearch.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.qlinee_RnombreSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ql_RcedulaSearch = QLabel(self.frame)
        self.ql_RcedulaSearch.setObjectName(u"ql_RcedulaSearch")
        self.ql_RcedulaSearch.setFont(font2)
        self.ql_RcedulaSearch.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.ql_RcedulaSearch)

        self.qlinee_RcedulaSearch = QLineEdit(self.frame)
        self.qlinee_RcedulaSearch.setObjectName(u"qlinee_RcedulaSearch")
        self.qlinee_RcedulaSearch.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_2.addWidget(self.qlinee_RcedulaSearch)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.bttn_Rbuscar = QPushButton(self.frame)
        self.bttn_Rbuscar.setObjectName(u"bttn_Rbuscar")
        self.bttn_Rbuscar.setStyleSheet(u"QPushButton:hover\n"
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
        icon4 = QIcon()
        icon4.addFile(u":/Botones salida/search-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bttn_Rbuscar.setIcon(icon4)
        self.bttn_Rbuscar.setIconSize(QSize(50, 50))
        self.bttn_Rbuscar.setFlat(True)

        self.horizontalLayout_5.addWidget(self.bttn_Rbuscar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.CentralWidget.addWidget(self.Headframe, 0, 0, 1, 1)

        self.line_2 = QFrame(Representantes)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.CentralWidget.addWidget(self.line_2, 3, 0, 1, 1)

        self.BodyFrame = QFrame(Representantes)
        self.BodyFrame.setObjectName(u"BodyFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.BodyFrame.sizePolicy().hasHeightForWidth())
        self.BodyFrame.setSizePolicy(sizePolicy1)
        self.BodyFrame.setMaximumSize(QSize(16777215, 16777215))
        self.BodyFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.BodyFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.BodyFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.ql_RnombresText = QLabel(self.BodyFrame)
        self.ql_RnombresText.setObjectName(u"ql_RnombresText")
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.ql_RnombresText.setFont(font3)
        self.ql_RnombresText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.ql_RnombresText)

        self.qlinee_RnombresInfo = QLineEdit(self.BodyFrame)
        self.qlinee_RnombresInfo.setObjectName(u"qlinee_RnombresInfo")
        self.qlinee_RnombresInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qlinee_RnombresInfo.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.qlinee_RnombresInfo)

        self.ql_RapellidosText = QLabel(self.BodyFrame)
        self.ql_RapellidosText.setObjectName(u"ql_RapellidosText")
        self.ql_RapellidosText.setFont(font3)
        self.ql_RapellidosText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.ql_RapellidosText)

        self.qlinee_RapellidosInfo = QLineEdit(self.BodyFrame)
        self.qlinee_RapellidosInfo.setObjectName(u"qlinee_RapellidosInfo")
        self.qlinee_RapellidosInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qlinee_RapellidosInfo.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.qlinee_RapellidosInfo)

        self.ql_RcedulaText = QLabel(self.BodyFrame)
        self.ql_RcedulaText.setObjectName(u"ql_RcedulaText")
        self.ql_RcedulaText.setFont(font3)
        self.ql_RcedulaText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.ql_RcedulaText)

        self.qlinee_RcedulaInfo = QLineEdit(self.BodyFrame)
        self.qlinee_RcedulaInfo.setObjectName(u"qlinee_RcedulaInfo")
        self.qlinee_RcedulaInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qlinee_RcedulaInfo.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.qlinee_RcedulaInfo)

        self.ql_RntelefonoText = QLabel(self.BodyFrame)
        self.ql_RntelefonoText.setObjectName(u"ql_RntelefonoText")
        self.ql_RntelefonoText.setFont(font3)
        self.ql_RntelefonoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.ql_RntelefonoText)

        self.qlinee_RntelefonoInfo = QLineEdit(self.BodyFrame)
        self.qlinee_RntelefonoInfo.setObjectName(u"qlinee_RntelefonoInfo")
        self.qlinee_RntelefonoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qlinee_RntelefonoInfo.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.qlinee_RntelefonoInfo)

        self.ql_RtotalrepreText = QLabel(self.BodyFrame)
        self.ql_RtotalrepreText.setObjectName(u"ql_RtotalrepreText")
        self.ql_RtotalrepreText.setFont(font3)
        self.ql_RtotalrepreText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.ql_RtotalrepreText)

        self.qlinee_RtotalrepreInfo = QLineEdit(self.BodyFrame)
        self.qlinee_RtotalrepreInfo.setObjectName(u"qlinee_RtotalrepreInfo")
        self.qlinee_RtotalrepreInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qlinee_RtotalrepreInfo.setReadOnly(True)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.qlinee_RtotalrepreInfo)

        self.ql_RparentescoText = QLabel(self.BodyFrame)
        self.ql_RparentescoText.setObjectName(u"ql_RparentescoText")
        self.ql_RparentescoText.setFont(font3)
        self.ql_RparentescoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.ql_RparentescoText)

        self.qlinee_RparentescoInfo = QLineEdit(self.BodyFrame)
        self.qlinee_RparentescoInfo.setObjectName(u"qlinee_RparentescoInfo")
        self.qlinee_RparentescoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qlinee_RparentescoInfo.setReadOnly(True)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.qlinee_RparentescoInfo)

        self.ql_RestadoLabText = QLabel(self.BodyFrame)
        self.ql_RestadoLabText.setObjectName(u"ql_RestadoLabText")
        self.ql_RestadoLabText.setFont(font3)
        self.ql_RestadoLabText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.ql_RestadoLabText)

        self.qlinee_RestadolabInfo = QLineEdit(self.BodyFrame)
        self.qlinee_RestadolabInfo.setObjectName(u"qlinee_RestadolabInfo")
        self.qlinee_RestadolabInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qlinee_RestadolabInfo.setReadOnly(True)

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.qlinee_RestadolabInfo)


        self.horizontalLayout_4.addLayout(self.formLayout)

        self.line_3 = QFrame(self.BodyFrame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.line_3)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.ql_RdireccionText = QLabel(self.BodyFrame)
        self.ql_RdireccionText.setObjectName(u"ql_RdireccionText")
        self.ql_RdireccionText.setFont(font3)
        self.ql_RdireccionText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.ql_RdireccionText)

        self.qpte_RdireccionInfo = QPlainTextEdit(self.BodyFrame)
        self.qpte_RdireccionInfo.setObjectName(u"qpte_RdireccionInfo")
        sizePolicy1.setHeightForWidth(self.qpte_RdireccionInfo.sizePolicy().hasHeightForWidth())
        self.qpte_RdireccionInfo.setSizePolicy(sizePolicy1)
        self.qpte_RdireccionInfo.setMaximumSize(QSize(16777215, 60))
        self.qpte_RdireccionInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qpte_RdireccionInfo.setTabChangesFocus(False)
        self.qpte_RdireccionInfo.setUndoRedoEnabled(True)
        self.qpte_RdireccionInfo.setReadOnly(True)
        self.qpte_RdireccionInfo.setCenterOnScroll(False)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.qpte_RdireccionInfo)

        self.qpte_RdirecciontrabajoInfo = QPlainTextEdit(self.BodyFrame)
        self.qpte_RdirecciontrabajoInfo.setObjectName(u"qpte_RdirecciontrabajoInfo")
        sizePolicy1.setHeightForWidth(self.qpte_RdirecciontrabajoInfo.sizePolicy().hasHeightForWidth())
        self.qpte_RdirecciontrabajoInfo.setSizePolicy(sizePolicy1)
        self.qpte_RdirecciontrabajoInfo.setMaximumSize(QSize(16777215, 60))
        self.qpte_RdirecciontrabajoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qpte_RdirecciontrabajoInfo.setTabChangesFocus(False)
        self.qpte_RdirecciontrabajoInfo.setUndoRedoEnabled(True)
        self.qpte_RdirecciontrabajoInfo.setReadOnly(True)
        self.qpte_RdirecciontrabajoInfo.setCenterOnScroll(False)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.qpte_RdirecciontrabajoInfo)

        self.ql_RdireccionTrabText = QLabel(self.BodyFrame)
        self.ql_RdireccionTrabText.setObjectName(u"ql_RdireccionTrabText")
        self.ql_RdireccionTrabText.setFont(font3)
        self.ql_RdireccionTrabText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.ql_RdireccionTrabText)

        self.qpte_RobservacionesInfo = QPlainTextEdit(self.BodyFrame)
        self.qpte_RobservacionesInfo.setObjectName(u"qpte_RobservacionesInfo")
        sizePolicy1.setHeightForWidth(self.qpte_RobservacionesInfo.sizePolicy().hasHeightForWidth())
        self.qpte_RobservacionesInfo.setSizePolicy(sizePolicy1)
        self.qpte_RobservacionesInfo.setMaximumSize(QSize(16777215, 60))
        self.qpte_RobservacionesInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qpte_RobservacionesInfo.setTabChangesFocus(False)
        self.qpte_RobservacionesInfo.setUndoRedoEnabled(True)
        self.qpte_RobservacionesInfo.setReadOnly(True)
        self.qpte_RobservacionesInfo.setCenterOnScroll(False)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.qpte_RobservacionesInfo)

        self.ql_RobservacionesText = QLabel(self.BodyFrame)
        self.ql_RobservacionesText.setObjectName(u"ql_RobservacionesText")
        self.ql_RobservacionesText.setFont(font3)
        self.ql_RobservacionesText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.ql_RobservacionesText)

        self.ql_REstudiantesList = QLabel(self.BodyFrame)
        self.ql_REstudiantesList.setObjectName(u"ql_REstudiantesList")
        self.ql_REstudiantesList.setFont(font3)
        self.ql_REstudiantesList.setStyleSheet(u"color: rgb(85, 170, 255);")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.ql_REstudiantesList)

        self.qlw_REstudiantes = QListWidget(self.BodyFrame)
        self.qlw_REstudiantes.setObjectName(u"qlw_REstudiantes")
        self.qlw_REstudiantes.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qlw_REstudiantes.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.qlw_REstudiantes.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.qlw_REstudiantes)


        self.horizontalLayout_4.addLayout(self.formLayout_2)


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
        self.textrefrescar.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\">REFRESCAR</p></body></html>", None))
        self.bttn_Rrefrescar.setText("")
        self.label.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\">EDITAR</p></body></html>", None))
        self.bttn_Rimprimir.setText("")
        self.textimprimir.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\">IMPRIMIR</p></body></html>", None))
        self.bttnRsalir.setText("")
        self.textsalir.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\">SALIR</p></body></html>", None))
        self.ql_RbuscarbaseText.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\">BUSCAR EN LA BASE DE DATOS</p></body></html>", None))
        self.ql_RescribanombresText.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">INFORMACION PARA BUSCAR INFORMACION DEL REPRESENTANTE</span></p></body></html>", None))
        self.bttn_verrepresentantes.setText(QCoreApplication.translate("Representantes", u"Ver Representantes", None))
        self.ql_RnombreSearch.setText(QCoreApplication.translate("Representantes", u"Nombre", None))
        self.qlinee_RnombreSearch.setPlaceholderText(QCoreApplication.translate("Representantes", u"                   Introduce el nombre del representante para mostrar", None))
        self.ql_RcedulaSearch.setText(QCoreApplication.translate("Representantes", u"C\u00e9dula", None))
        self.qlinee_RcedulaSearch.setPlaceholderText(QCoreApplication.translate("Representantes", u"                   Introduce la cedula para mostrar la informacion", None))
        self.bttn_Rbuscar.setText("")
        self.ql_RnombresText.setText(QCoreApplication.translate("Representantes", u"Nombres", None))
        self.ql_RapellidosText.setText(QCoreApplication.translate("Representantes", u"Apellidos", None))
        self.ql_RcedulaText.setText(QCoreApplication.translate("Representantes", u"Cedula", None))
        self.ql_RntelefonoText.setText(QCoreApplication.translate("Representantes", u"Telefono", None))
        self.qlinee_RntelefonoInfo.setInputMask(QCoreApplication.translate("Representantes", u"(9999)-9999999", None))
        self.ql_RtotalrepreText.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\">Total de Representados</p></body></html>", None))
        self.ql_RparentescoText.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p>Parentesco</p></body></html>", None))
        self.qlinee_RparentescoInfo.setText("")
        self.ql_RestadoLabText.setText(QCoreApplication.translate("Representantes", u"Estado Laboral", None))
        self.ql_RdireccionText.setText(QCoreApplication.translate("Representantes", u"Direcci\u00f3n", None))
        self.ql_RdireccionTrabText.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\">Direcci\u00f3n Trabajo</p></body></html>", None))
        self.ql_RobservacionesText.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\">Observaciones</p></body></html>", None))
        self.ql_REstudiantesList.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\">Estudiantes <br/>Representados</p></body></html>", None))
        self.ql_guardarText.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">GUARDAR</span></p></body></html>", None))
        self.ql_cancelarText.setText(QCoreApplication.translate("Representantes", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">CANCELAR</span></p></body></html>", None))
    # retranslateUi

