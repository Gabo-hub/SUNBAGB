# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ebusquedabmkJTO.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_eBusqueda(object):
    def setupUi(self, eBusqueda):
        if not eBusqueda.objectName():
            eBusqueda.setObjectName(u"eBusqueda")
        eBusqueda.resize(656, 536)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(eBusqueda.sizePolicy().hasHeightForWidth())
        eBusqueda.setSizePolicy(sizePolicy)
        eBusqueda.setStyleSheet(u"background-color: rgb(51, 54, 57);")
        eBusqueda.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(eBusqueda)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(eBusqueda)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(16777215, 90))
        self.frame.setStyleSheet(u"background-color: rgb(85, 90, 95);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setLineWidth(0)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 15, 15, -1)
        self.txtCategoria = QLineEdit(self.frame)
        self.txtCategoria.setObjectName(u"txtCategoria")
        self.txtCategoria.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.txtCategoria, 1, 1, 1, 1)

        self.lblColumna1 = QLabel(self.frame)
        self.lblColumna1.setObjectName(u"lblColumna1")
        self.lblColumna1.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setFamilies([u"Poppins"])
        font.setPointSize(12)
        font.setBold(True)
        self.lblColumna1.setFont(font)
        self.lblColumna1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblColumna1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lblColumna1, 0, 0, 1, 1)

        self.lblColumna2 = QLabel(self.frame)
        self.lblColumna2.setObjectName(u"lblColumna2")
        self.lblColumna2.setFont(font)
        self.lblColumna2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblColumna2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.lblColumna2, 1, 0, 1, 1)

        self.txtNumeracion = QLineEdit(self.frame)
        self.txtNumeracion.setObjectName(u"txtNumeracion")
        self.txtNumeracion.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.txtNumeracion, 0, 1, 1, 1)

        self.cbox_grado = QComboBox(self.frame)
        self.cbox_grado.setObjectName(u"cbox_grado")
        self.cbox_grado.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cbox_grado, 2, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.frTabla = QFrame(eBusqueda)
        self.frTabla.setObjectName(u"frTabla")
        self.frTabla.setFrameShape(QFrame.Shape.StyledPanel)
        self.frTabla.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frTabla)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tblBusqueda = QTableWidget(self.frTabla)
        if (self.tblBusqueda.columnCount() < 2):
            self.tblBusqueda.setColumnCount(2)
        font1 = QFont()
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        __qtablewidgetitem.setBackground(QColor(24, 42, 127));
        self.tblBusqueda.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tblBusqueda.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tblBusqueda.rowCount() < 12):
            self.tblBusqueda.setRowCount(12)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblBusqueda.setItem(0, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblBusqueda.setItem(0, 1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblBusqueda.setItem(1, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblBusqueda.setItem(1, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblBusqueda.setItem(2, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblBusqueda.setItem(2, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblBusqueda.setItem(3, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tblBusqueda.setItem(3, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tblBusqueda.setItem(4, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tblBusqueda.setItem(4, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tblBusqueda.setItem(5, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tblBusqueda.setItem(5, 1, __qtablewidgetitem13)
        self.tblBusqueda.setObjectName(u"tblBusqueda")
        self.tblBusqueda.setEnabled(True)
        self.tblBusqueda.setAutoScroll(True)
        self.tblBusqueda.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblBusqueda.setAlternatingRowColors(True)
        self.tblBusqueda.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tblBusqueda.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblBusqueda.setRowCount(12)
        self.tblBusqueda.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_4.addWidget(self.tblBusqueda)

        self.frPieBotonSalir = QFrame(self.frTabla)
        self.frPieBotonSalir.setObjectName(u"frPieBotonSalir")
        self.frPieBotonSalir.setMinimumSize(QSize(0, 20))
        self.frPieBotonSalir.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(85, 90, 95);\n"
"}\n"
"QPushButton{\n"
"	color:rgb(255, 255, 255);\n"
"	background-color: rgb(71, 93, 144);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"	background-color: rgb(89, 118, 181);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{		\n"
"	background-color: rgb(62, 82, 125);\n"
"}")
        self.frPieBotonSalir.setFrameShape(QFrame.Shape.StyledPanel)
        self.frPieBotonSalir.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frPieBotonSalir)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frPieBotonSalir)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnSalir = QPushButton(self.frPieBotonSalir)
        self.btnSalir.setObjectName(u"btnSalir")
        font2 = QFont()
        font2.setFamilies([u"Poppins"])
        font2.setPointSize(9)
        font2.setBold(False)
        self.btnSalir.setFont(font2)

        self.horizontalLayout.addWidget(self.btnSalir)


        self.verticalLayout_4.addWidget(self.frPieBotonSalir)


        self.verticalLayout.addWidget(self.frTabla)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(eBusqueda)

        QMetaObject.connectSlotsByName(eBusqueda)
    # setupUi

    def retranslateUi(self, eBusqueda):
        eBusqueda.setWindowTitle(QCoreApplication.translate("eBusqueda", u"BUSQUEDA", None))
        self.txtCategoria.setPlaceholderText(QCoreApplication.translate("eBusqueda", u"B\u00fasqueda por palabras Claves...", None))
        self.lblColumna1.setText(QCoreApplication.translate("eBusqueda", u"CEDULA", None))
        self.lblColumna2.setText(QCoreApplication.translate("eBusqueda", u"CATEGORIA", None))
        self.txtNumeracion.setPlaceholderText(QCoreApplication.translate("eBusqueda", u"B\u00fasqueda por palabras Claves...", None))
        self.cbox_grado.setPlaceholderText(QCoreApplication.translate("eBusqueda", u"B\u00fasqueda por grado", None))
        self.label.setText(QCoreApplication.translate("eBusqueda", u"GRADO", None))
        ___qtablewidgetitem = self.tblBusqueda.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("eBusqueda", u"ID NUMERACION", None));
        ___qtablewidgetitem1 = self.tblBusqueda.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("eBusqueda", u"CATEGORIA", None));

        __sortingEnabled = self.tblBusqueda.isSortingEnabled()
        self.tblBusqueda.setSortingEnabled(False)
        self.tblBusqueda.setSortingEnabled(__sortingEnabled)

        self.label_3.setText(QCoreApplication.translate("eBusqueda", u"Seleccione su opci\u00f3n y Oprima Doble Click", None))
        self.btnSalir.setText(QCoreApplication.translate("eBusqueda", u"Salir", None))
    # retranslateUi

