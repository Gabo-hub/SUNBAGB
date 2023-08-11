# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windows.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import views.resource_rc

class Ui_Principal(object):
    def setupUi(self, Principal):
        if not Principal.objectName():
            Principal.setObjectName(u"Principal")
        Principal.setEnabled(True)
        Principal.resize(661, 504)
        Principal.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u":/Botones categoria/Webp.net-resizeimage.png", QSize(), QIcon.Normal, QIcon.Off)
        Principal.setWindowIcon(icon)
        Principal.setLayoutDirection(Qt.LeftToRight)
        Principal.setStyleSheet(u"background-color: rgb(51, 54, 57);")
        Principal.setIconSize(QSize(24, 24))
        self.actionRegistro_de_La_Data = QAction(Principal)
        self.actionRegistro_de_La_Data.setObjectName(u"actionRegistro_de_La_Data")
        font = QFont()
        font.setFamily(u"Poppins")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.actionRegistro_de_La_Data.setFont(font)
        self.actionRegistro_de_La_Data.setShortcutContext(Qt.ApplicationShortcut)
        self.CentralWidget = QWidget(Principal)
        self.CentralWidget.setObjectName(u"CentralWidget")
        self.CentralWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.CentralWidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self.CentralWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.CentralWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(85, 90, 95);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Poppins")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setTextFormat(Qt.RichText)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_6)

        self.bprofesores_3 = QPushButton(self.CentralWidget)
        self.bprofesores_3.setObjectName(u"bprofesores_3")
        self.bprofesores_3.setStyleSheet(u"QPushButton:hover\n"
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
        icon1.addFile(u":/Botones categoria/c635eec91f05b8a1c4f03a7b2eae770c.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bprofesores_3.setIcon(icon1)
        self.bprofesores_3.setIconSize(QSize(119, 140))
        self.bprofesores_3.setFlat(True)

        self.verticalLayout_8.addWidget(self.bprofesores_3)

        self.label_6 = QLabel(self.CentralWidget)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setFamily(u"Poppins")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.label_6)

        self.verticalSpacer_5 = QSpacerItem(20, 14, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_7)

        self.bestudiantes_3 = QPushButton(self.CentralWidget)
        self.bestudiantes_3.setObjectName(u"bestudiantes_3")
        self.bestudiantes_3.setAutoFillBackground(False)
        self.bestudiantes_3.setStyleSheet(u"QPushButton:hover\n"
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
        icon2.addFile(u":/Botones categoria/f7e559c21b8e17b80fecd9ead3e0338f.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bestudiantes_3.setIcon(icon2)
        self.bestudiantes_3.setIconSize(QSize(121, 150))
        self.bestudiantes_3.setCheckable(False)
        self.bestudiantes_3.setChecked(False)
        self.bestudiantes_3.setAutoRepeat(False)
        self.bestudiantes_3.setAutoExclusive(False)
        self.bestudiantes_3.setAutoDefault(False)
        self.bestudiantes_3.setFlat(True)

        self.verticalLayout_4.addWidget(self.bestudiantes_3)

        self.labelestudiantes_3 = QLabel(self.CentralWidget)
        self.labelestudiantes_3.setObjectName(u"labelestudiantes_3")
        font3 = QFont()
        font3.setFamily(u"Poppins")
        font3.setBold(True)
        font3.setWeight(75)
        self.labelestudiantes_3.setFont(font3)
        self.labelestudiantes_3.setStyleSheet(u"color:rgb(255, 255, 255)")

        self.verticalLayout_4.addWidget(self.labelestudiantes_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_8)

        self.brepresentantes_3 = QPushButton(self.CentralWidget)
        self.brepresentantes_3.setObjectName(u"brepresentantes_3")
        self.brepresentantes_3.setStyleSheet(u"QPushButton:hover\n"
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
        icon3.addFile(u":/Botones categoria/representantes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.brepresentantes_3.setIcon(icon3)
        self.brepresentantes_3.setIconSize(QSize(123, 150))
        self.brepresentantes_3.setFlat(True)

        self.verticalLayout_9.addWidget(self.brepresentantes_3)

        self.label_7 = QLabel(self.CentralWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.label_7)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_9)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.frame_2 = QFrame(self.CentralWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(85, 90, 95);\n"
"color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"")
        self.checkBox.setIconSize(QSize(25, 23))

        self.horizontalLayout.addWidget(self.checkBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        font4 = QFont()
        font4.setFamily(u"Poppins")
        font4.setPointSize(10)
        self.pushButton_4.setFont(font4)
        self.pushButton_4.setStyleSheet(u"QPushButton:hover\n"
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
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setFlat(False)

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout.addWidget(self.frame_2)

        Principal.setCentralWidget(self.CentralWidget)
        self.menubar = QMenuBar(Principal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 661, 21))
        self.menubar.setFont(font)
        self.menubar.setCursor(QCursor(Qt.PointingHandCursor))
        self.menubar.setStyleSheet(u"background-color: rgb(85, 90, 95);\n"
"color: rgb(255, 255, 255);")
        self.menuIngresar_datos = QMenu(self.menubar)
        self.menuIngresar_datos.setObjectName(u"menuIngresar_datos")
        Principal.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuIngresar_datos.menuAction())
        self.menuIngresar_datos.addAction(self.actionRegistro_de_La_Data)

        self.retranslateUi(Principal)

        self.bestudiantes_3.setDefault(False)
        self.pushButton_4.setDefault(False)


        QMetaObject.connectSlotsByName(Principal)
    # setupUi

    def retranslateUi(self, Principal):
        Principal.setWindowTitle("")
        self.actionRegistro_de_La_Data.setText(QCoreApplication.translate("Principal", u"Registro de La Data", None))
#if QT_CONFIG(statustip)
        self.actionRegistro_de_La_Data.setStatusTip(QCoreApplication.translate("Principal", u"Abrir", None))
#endif // QT_CONFIG(statustip)
        self.label.setText(QCoreApplication.translate("Principal", u"<html><head/><body><p align=\"center\">REGISTRO INSTITUCIONAL<br/>ANTONIO GUZMAN BLANCO</p></body></html>", None))
        self.bprofesores_3.setText("")
        self.label_6.setText(QCoreApplication.translate("Principal", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Profesores</span></p></body></html>", None))
        self.bestudiantes_3.setText("")
        self.labelestudiantes_3.setText(QCoreApplication.translate("Principal", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Estudiantes</span></p></body></html>", None))
        self.brepresentantes_3.setText("")
        self.label_7.setText(QCoreApplication.translate("Principal", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Representantes</span></p></body></html>", None))
        self.checkBox.setText(QCoreApplication.translate("Principal", u"Modo Claro", None))
        self.pushButton_4.setText(QCoreApplication.translate("Principal", u"Cerrar", None))
        self.menuIngresar_datos.setTitle(QCoreApplication.translate("Principal", u"Ingresar datos", None))
    # retranslateUi

