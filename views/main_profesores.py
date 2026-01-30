# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_profesoresxVTbUQ.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget, QComboBox)
import views.resource_rc

class Ui_Profesores(object):
    def setupUi(self, Profesores):
        if not Profesores.objectName():
            Profesores.setObjectName(u"Profesores")
        Profesores.setWindowModality(Qt.WindowModality.ApplicationModal)
        Profesores.resize(741, 526)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Profesores.sizePolicy().hasHeightForWidth())
        Profesores.setSizePolicy(sizePolicy)
        Profesores.setStyleSheet(u"background-color: rgb(51, 54, 57);")
        self.gridLayout_2 = QGridLayout(Profesores)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.CentralWidget = QGridLayout()
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.FootFrame = QFrame(Profesores)
        self.FootFrame.setObjectName(u"FootFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.FootFrame.sizePolicy().hasHeightForWidth())
        self.FootFrame.setSizePolicy(sizePolicy1)
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
        self.textsalir = QLabel(self.FootFrame)
        self.textsalir.setObjectName(u"textsalir")
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setBold(True)
        self.textsalir.setFont(font)
        self.textsalir.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.textsalir.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.textsalir, 1, 3, 1, 1)

        self.bttn_salir = QPushButton(self.FootFrame)
        self.bttn_salir.setObjectName(u"bttn_salir")
        self.bttn_salir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bttn_salir.setStyleSheet(u"QPushButton:hover\n"
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
        icon.addFile(u":/Botones salida/salir_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bttn_salir.setIcon(icon)
        self.bttn_salir.setIconSize(QSize(50, 50))
        self.bttn_salir.setFlat(True)

        self.gridLayout_7.addWidget(self.bttn_salir, 0, 3, 1, 1)

        self.bttn_imprimir = QPushButton(self.FootFrame)
        self.bttn_imprimir.setObjectName(u"bttn_imprimir")
        self.bttn_imprimir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bttn_imprimir.setStyleSheet(u"QPushButton:hover\n"
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
        icon1.addFile(u":/Botones salida/imprimir.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bttn_imprimir.setIcon(icon1)
        self.bttn_imprimir.setIconSize(QSize(50, 50))
        self.bttn_imprimir.setFlat(True)

        self.gridLayout_7.addWidget(self.bttn_imprimir, 0, 2, 1, 1)

        self.textimprimir = QLabel(self.FootFrame)
        self.textimprimir.setObjectName(u"textimprimir")
        self.textimprimir.setFont(font)
        self.textimprimir.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.textimprimir.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.textimprimir, 1, 2, 1, 1)

        self.bttn_refrescar = QPushButton(self.FootFrame)
        self.bttn_refrescar.setObjectName(u"bttn_refrescar")
        self.bttn_refrescar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bttn_refrescar.setStyleSheet(u"QPushButton:hover\n"
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
        icon2.addFile(u":/Botones salida/refresh-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bttn_refrescar.setIcon(icon2)
        self.bttn_refrescar.setIconSize(QSize(50, 50))
        self.bttn_refrescar.setFlat(True)

        self.gridLayout_7.addWidget(self.bttn_refrescar, 0, 0, 1, 1)

        self.textrefrescar = QLabel(self.FootFrame)
        self.textrefrescar.setObjectName(u"textrefrescar")
        self.textrefrescar.setFont(font)
        self.textrefrescar.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.textrefrescar.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.textrefrescar, 1, 0, 1, 1)

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
        icon3 = QIcon()
        icon3.addFile(u":/Botones salida/edit-book.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bttn_editar.setIcon(icon3)
        self.bttn_editar.setIconSize(QSize(50, 50))
        self.bttn_editar.setFlat(True)

        self.gridLayout_7.addWidget(self.bttn_editar, 0, 1, 1, 1)

        self.label = QLabel(self.FootFrame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.label.setMouseTracking(True)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.label, 1, 1, 1, 1)

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
        self.ql_guardarText.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
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
        self.ql_cancelarText.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.ql_cancelarText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_7.addWidget(self.ql_cancelarText, 1, 5, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.CentralWidget.addWidget(self.FootFrame, 4, 0, 1, 1)

        self.line = QFrame(Profesores)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.CentralWidget.addWidget(self.line, 1, 0, 1, 1)

        self.Headframe = QFrame(Profesores)
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
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ql_buscarText = QLabel(self.frame)
        self.ql_buscarText.setObjectName(u"ql_buscarText")
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.ql_buscarText.setFont(font2)
        self.ql_buscarText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.ql_buscarText)

        self.ql_docenteText = QLabel(self.frame)
        self.ql_docenteText.setObjectName(u"ql_docenteText")
        self.ql_docenteText.setFont(font2)
        self.ql_docenteText.setStyleSheet(u"color: rgb(85, 170, 255);")

        self.verticalLayout_2.addWidget(self.ql_docenteText)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.bttn_verprofesores = QToolButton(self.frame)
        self.bttn_verprofesores.setObjectName(u"bttn_verprofesores")
        self.bttn_verprofesores.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bttn_verprofesores.setStyleSheet(u"QPushButton:hover\n"
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
        self.bttn_verprofesores.setAutoRaise(False)
        self.bttn_verprofesores.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout_5.addWidget(self.bttn_verprofesores)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lbel_nombreSearch = QLabel(self.frame)
        self.lbel_nombreSearch.setObjectName(u"lbel_nombreSearch")
        self.lbel_nombreSearch.setFont(font2)
        self.lbel_nombreSearch.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.lbel_nombreSearch)

        self.qlinee_nombreSearch = QLineEdit(self.frame)
        self.qlinee_nombreSearch.setObjectName(u"qlinee_nombreSearch")
        self.qlinee_nombreSearch.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.qlinee_nombreSearch)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lbel_cedulaSearch = QLabel(self.frame)
        self.lbel_cedulaSearch.setObjectName(u"lbel_cedulaSearch")
        self.lbel_cedulaSearch.setFont(font2)
        self.lbel_cedulaSearch.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.lbel_cedulaSearch)

        self.qlinee_cedulaSearch = QLineEdit(self.frame)
        self.qlinee_cedulaSearch.setObjectName(u"qlinee_cedulaSearch")
        self.qlinee_cedulaSearch.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_2.addWidget(self.qlinee_cedulaSearch)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.bttn_busqueda = QPushButton(self.frame)
        self.bttn_busqueda.setObjectName(u"bttn_busqueda")
        self.bttn_busqueda.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.bttn_busqueda.setStyleSheet(u"QPushButton:hover\n"
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
        self.bttn_busqueda.setIcon(icon4)
        self.bttn_busqueda.setIconSize(QSize(50, 50))
        self.bttn_busqueda.setFlat(True)

        self.horizontalLayout_4.addWidget(self.bttn_busqueda)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.CentralWidget.addWidget(self.Headframe, 0, 0, 1, 1)

        self.line_2 = QFrame(Profesores)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.CentralWidget.addWidget(self.line_2, 3, 0, 1, 1)

        self.BodyFrame = QFrame(Profesores)
        self.BodyFrame.setObjectName(u"BodyFrame")
        self.BodyFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.BodyFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.BodyFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.ql_codcargoText = QLabel(self.BodyFrame)
        self.ql_codcargoText.setObjectName(u"ql_codcargoText")
        font3 = QFont()
        font3.setFamilies([u"Poppins"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.ql_codcargoText.setFont(font3)
        self.ql_codcargoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_codcargoText, 3, 0, 1, 1)

        self.cbox_gradodocInfo = QComboBox(self.BodyFrame)
        self.cbox_gradodocInfo.setObjectName(u"cbox_gradodocInfo")
        self.cbox_gradodocInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_9.addWidget(self.cbox_gradodocInfo, 1, 1, 1, 1)

        self.qlinee_coddepenInfo = QLineEdit(self.BodyFrame)
        self.qlinee_coddepenInfo.setObjectName(u"qlinee_coddepenInfo")
        self.qlinee_coddepenInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qlinee_coddepenInfo.setReadOnly(True)

        self.gridLayout_9.addWidget(self.qlinee_coddepenInfo, 4, 1, 1, 1)

        self.qlinee_codcargoInfo = QLineEdit(self.BodyFrame)
        self.qlinee_codcargoInfo.setObjectName(u"qlinee_codcargoInfo")
        self.qlinee_codcargoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qlinee_codcargoInfo.setReadOnly(True)

        self.gridLayout_9.addWidget(self.qlinee_codcargoInfo, 3, 1, 1, 1)

        self.qlinee_telefonoInfo = QLineEdit(self.BodyFrame)
        self.qlinee_telefonoInfo.setObjectName(u"qlinee_telefonoInfo")
        self.qlinee_telefonoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qlinee_telefonoInfo.setReadOnly(True)

        self.gridLayout_9.addWidget(self.qlinee_telefonoInfo, 0, 1, 1, 1)

        self.qlinee_anosServiciosText = QLineEdit(self.BodyFrame)
        self.qlinee_anosServiciosText.setObjectName(u"qlinee_anosServiciosText")
        self.qlinee_anosServiciosText.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qlinee_anosServiciosText.setReadOnly(True)

        self.gridLayout_9.addWidget(self.qlinee_anosServiciosText, 2, 1, 1, 1)

        self.ql_anosServiciosText = QLabel(self.BodyFrame)
        self.ql_anosServiciosText.setObjectName(u"ql_anosServiciosText")
        self.ql_anosServiciosText.setFont(font3)
        self.ql_anosServiciosText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_anosServiciosText, 2, 0, 1, 1)

        self.ql_gradodocText = QLabel(self.BodyFrame)
        self.ql_gradodocText.setObjectName(u"ql_gradodocText")
        font4 = QFont()
        font4.setFamilies([u"Poppins"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.ql_gradodocText.setFont(font4)
        self.ql_gradodocText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_gradodocText, 1, 0, 1, 1)

        self.ql_telefonoText = QLabel(self.BodyFrame)
        self.ql_telefonoText.setObjectName(u"ql_telefonoText")
        self.ql_telefonoText.setFont(font3)
        self.ql_telefonoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_telefonoText, 0, 0, 1, 1)

        self.ql_codigodepenText = QLabel(self.BodyFrame)
        self.ql_codigodepenText.setObjectName(u"ql_codigodepenText")
        self.ql_codigodepenText.setFont(font3)
        self.ql_codigodepenText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.ql_codigodepenText, 4, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_9, 0, 2, 3, 1)

        self.line_3 = QFrame(self.BodyFrame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_5.addWidget(self.line_3, 0, 1, 3, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.ql_fnacimientoText = QLabel(self.BodyFrame)
        self.ql_fnacimientoText.setObjectName(u"ql_fnacimientoText")
        self.ql_fnacimientoText.setFont(font3)
        self.ql_fnacimientoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.ql_fnacimientoText, 5, 0, 1, 1)

        self.qlinee_nombreInfo = QLineEdit(self.BodyFrame)
        self.qlinee_nombreInfo.setObjectName(u"qlinee_nombreInfo")
        self.qlinee_nombreInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qlinee_nombreInfo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.qlinee_nombreInfo, 0, 2, 1, 1)

        self.ql_apellidoText = QLabel(self.BodyFrame)
        self.ql_apellidoText.setObjectName(u"ql_apellidoText")
        self.ql_apellidoText.setFont(font3)
        self.ql_apellidoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.ql_apellidoText, 1, 0, 1, 1)

        self.ql_nombreText = QLabel(self.BodyFrame)
        self.ql_nombreText.setObjectName(u"ql_nombreText")
        self.ql_nombreText.setFont(font3)
        self.ql_nombreText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.ql_nombreText, 0, 0, 1, 1)

        self.qlinee_sexoInfo = QLineEdit(self.BodyFrame)
        self.qlinee_sexoInfo.setObjectName(u"qlinee_sexoInfo")
        self.qlinee_sexoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qlinee_sexoInfo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.qlinee_sexoInfo, 4, 2, 1, 1)

        self.ql_sexoText = QLabel(self.BodyFrame)
        self.ql_sexoText.setObjectName(u"ql_sexoText")
        self.ql_sexoText.setFont(font3)
        self.ql_sexoText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.ql_sexoText, 4, 0, 1, 1)

        self.qlinee_fnacimientoinfo = QLineEdit(self.BodyFrame)
        self.qlinee_fnacimientoinfo.setObjectName(u"qlinee_fnacimientoinfo")
        self.qlinee_fnacimientoinfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qlinee_fnacimientoinfo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.qlinee_fnacimientoinfo, 5, 2, 1, 1)

        self.qlinee_apellidoInfo = QLineEdit(self.BodyFrame)
        self.qlinee_apellidoInfo.setObjectName(u"qlinee_apellidoInfo")
        self.qlinee_apellidoInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qlinee_apellidoInfo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.qlinee_apellidoInfo, 1, 2, 1, 1)

        self.ql_cedulaText = QLabel(self.BodyFrame)
        self.ql_cedulaText.setObjectName(u"ql_cedulaText")
        self.ql_cedulaText.setFont(font3)
        self.ql_cedulaText.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.ql_cedulaText, 2, 0, 1, 1)

        self.qlinee_cedulaInfo = QLineEdit(self.BodyFrame)
        self.qlinee_cedulaInfo.setObjectName(u"qlinee_cedulaInfo")
        self.qlinee_cedulaInfo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.qlinee_cedulaInfo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.qlinee_cedulaInfo, 2, 2, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 3, 1)


        self.CentralWidget.addWidget(self.BodyFrame, 2, 0, 1, 1)


        self.gridLayout_2.addLayout(self.CentralWidget, 0, 0, 1, 1)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.qlinee_nombreSearch, self.qlinee_cedulaSearch)
        QWidget.setTabOrder(self.qlinee_cedulaSearch, self.qlinee_nombreInfo)
        QWidget.setTabOrder(self.qlinee_nombreInfo, self.qlinee_apellidoInfo)
        QWidget.setTabOrder(self.qlinee_apellidoInfo, self.qlinee_cedulaInfo)
        QWidget.setTabOrder(self.qlinee_cedulaInfo, self.qlinee_sexoInfo)
        QWidget.setTabOrder(self.qlinee_sexoInfo, self.qlinee_fnacimientoinfo)
        QWidget.setTabOrder(self.qlinee_fnacimientoinfo, self.qlinee_telefonoInfo)
        QWidget.setTabOrder(self.qlinee_telefonoInfo, self.cbox_gradodocInfo)
        QWidget.setTabOrder(self.cbox_gradodocInfo, self.qlinee_anosServiciosText)
        QWidget.setTabOrder(self.qlinee_anosServiciosText, self.qlinee_codcargoInfo)
        QWidget.setTabOrder(self.qlinee_codcargoInfo, self.qlinee_coddepenInfo)
        QWidget.setTabOrder(self.qlinee_coddepenInfo, self.bttn_refrescar)
        QWidget.setTabOrder(self.bttn_refrescar, self.bttn_editar)
        QWidget.setTabOrder(self.bttn_editar, self.bttn_imprimir)
        QWidget.setTabOrder(self.bttn_imprimir, self.bttn_salir)

        self.retranslateUi(Profesores)
        self.bttn_refrescar.clicked.connect(self.qlinee_telefonoInfo.clear)
        self.bttn_refrescar.clicked.connect(self.qlinee_cedulaInfo.clear)
        self.bttn_refrescar.clicked.connect(self.qlinee_apellidoInfo.clear)
        self.bttn_refrescar.clicked.connect(self.qlinee_nombreInfo.clear)
        self.bttn_refrescar.clicked.connect(self.qlinee_cedulaSearch.clear)
        self.bttn_refrescar.clicked.connect(self.qlinee_nombreSearch.clear)
        self.bttn_refrescar.clicked.connect(self.qlinee_sexoInfo.clear)
        self.bttn_refrescar.clicked.connect(self.qlinee_fnacimientoinfo.clear)
        self.qlinee_nombreSearch.textEdited.connect(self.qlinee_cedulaSearch.clear)
        self.qlinee_cedulaSearch.textEdited.connect(self.qlinee_nombreSearch.clear)
        self.bttn_refrescar.clicked.connect(self.qlinee_anosServiciosText.clear)
        self.bttn_refrescar.clicked.connect(self.qlinee_codcargoInfo.clear)
        self.bttn_refrescar.clicked.connect(self.qlinee_coddepenInfo.clear)
        self.bttn_salir.clicked.connect(Profesores.close)

        QMetaObject.connectSlotsByName(Profesores)
    # setupUi

    def retranslateUi(self, Profesores):
        Profesores.setWindowTitle(QCoreApplication.translate("Profesores", u"Profesores", None))
        self.textsalir.setText(QCoreApplication.translate("Profesores", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SALIR</span></p></body></html>", None))
        self.bttn_salir.setText("")
        self.bttn_imprimir.setText("")
        self.textimprimir.setText(QCoreApplication.translate("Profesores", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">IMPRIMIR</span></p></body></html>", None))
        self.bttn_refrescar.setText("")
        self.textrefrescar.setText(QCoreApplication.translate("Profesores", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">REFRESCAR</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Profesores", u"<html><head/><body><p align=\"center\">EDITAR</p></body></html>", None))
        self.ql_buscarText.setText(QCoreApplication.translate("Profesores", u"<html><head/><body><p align=\"center\">BUSCAR EN LA BASE DE DATOS</p></body></html>", None))
        self.ql_docenteText.setText(QCoreApplication.translate("Profesores", u"<html><head/><body><p align=\"center\">INFORMACION PARA BUSCAR INFORMACION DEL DOCENTE</p></body></html>", None))
        self.bttn_verprofesores.setText(QCoreApplication.translate("Profesores", u"Ver Profesores", None))
        self.lbel_nombreSearch.setText(QCoreApplication.translate("Profesores", u"Nombre", None))
        self.qlinee_nombreSearch.setPlaceholderText(QCoreApplication.translate("Profesores", u"                   Introduce el nombre del representante para mostrar", None))
        self.lbel_cedulaSearch.setText(QCoreApplication.translate("Profesores", u"C\u00e9dula", None))
        self.qlinee_cedulaSearch.setPlaceholderText(QCoreApplication.translate("Profesores", u"                   Introduce la cedula para mostrar la informacion", None))
        self.bttn_busqueda.setText("")
        self.ql_codcargoText.setText(QCoreApplication.translate("Profesores", u"<html><head/><body><p align=\"justify\">Codigo de cargo</p></body></html>", None))
        self.qlinee_telefonoInfo.setInputMask(QCoreApplication.translate("Profesores", u"(9999)-9999999", None))
        self.ql_anosServiciosText.setText(QCoreApplication.translate("Profesores", u"A\u00f1os de servicios", None))
        self.ql_gradodocText.setText(QCoreApplication.translate("Profesores", u"Grado del docente", None))
        self.ql_telefonoText.setText(QCoreApplication.translate("Profesores", u"Telefono", None))
        self.ql_codigodepenText.setText(QCoreApplication.translate("Profesores", u"<html><head/><body><p align=\"justify\">Codigo de dependencia</p></body></html>", None))
        self.ql_fnacimientoText.setText(QCoreApplication.translate("Profesores", u"<html><head/><body><p align=\"center\">F.Nacimiento</p></body></html>", None))
        self.ql_apellidoText.setText(QCoreApplication.translate("Profesores", u"Apellidos", None))
        self.ql_nombreText.setText(QCoreApplication.translate("Profesores", u"Nombres", None))
        self.ql_sexoText.setText(QCoreApplication.translate("Profesores", u"<html><head/><body><p align=\"justify\">Sexo</p></body></html>", None))
        self.qlinee_fnacimientoinfo.setInputMask(QCoreApplication.translate("Profesores", u"99/99/9999", None))
        self.qlinee_fnacimientoinfo.setText(QCoreApplication.translate("Profesores", u"//", None))
        self.ql_cedulaText.setText(QCoreApplication.translate("Profesores", u"Cedula", None))
        self.ql_guardarText.setText(QCoreApplication.translate("Profesores", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">GUARDAR</span></p></body></html>", None))
        self.ql_cancelarText.setText(QCoreApplication.translate("Profesores", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">CANCELAR</span></p></body></html>", None))
    # retranslateUi

