# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SpotyUNIypLIax.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1252, 647)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_inferior = QFrame(self.centralwidget)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_lateral = QFrame(self.frame_inferior)
        self.frame_lateral.setObjectName(u"frame_lateral")
        self.frame_lateral.setMinimumSize(QSize(250, 0))
        self.frame_lateral.setMaximumSize(QSize(0, 16777215))
        self.frame_lateral.setStyleSheet(u"QFrame{\n"
"background-color:rgb(105, 105, 255)\n"
"}\n"
"\n"
"QPushButton{\n"
"background:qlineargradient(spread:pad, x1:0.0695224, y1:0.943, x2:0.825871, y2:0.745, stop:0.00497512 rgba(255, 255, 255, 255), stop:1 rgba(74, 68, 255, 255));\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font 75 12pt \"Arial Narrow\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(255, 255, 255);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"font 75 12pt \"Arial Narrow\";\n"
"}")
        self.frame_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_lateral)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_inicio = QPushButton(self.frame_lateral)
        self.bt_inicio.setObjectName(u"bt_inicio")
        self.bt_inicio.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setFamily(u"Georgia")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.bt_inicio.setFont(font)
        icon = QIcon()
        icon.addFile(u"ola.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_inicio.setIcon(icon)
        self.bt_inicio.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_inicio)

        self.bt_canciones = QPushButton(self.frame_lateral)
        self.bt_canciones.setObjectName(u"bt_canciones")
        self.bt_canciones.setMinimumSize(QSize(200, 40))
        font1 = QFont()
        font1.setFamily(u"Georgia")
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.bt_canciones.setFont(font1)
        self.bt_canciones.setLayoutDirection(Qt.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u"musica.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_canciones.setIcon(icon1)
        self.bt_canciones.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_canciones)

        self.bt_planes = QPushButton(self.frame_lateral)
        self.bt_planes.setObjectName(u"bt_planes")
        self.bt_planes.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setFamily(u"Georgia")
        font2.setBold(True)
        font2.setWeight(75)
        self.bt_planes.setFont(font2)
        self.bt_planes.setLayoutDirection(Qt.RightToLeft)
        icon2 = QIcon()
        icon2.addFile(u"agregar-contacto.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_planes.setIcon(icon2)
        self.bt_planes.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_planes)

        self.bt_cliente = QPushButton(self.frame_lateral)
        self.bt_cliente.setObjectName(u"bt_cliente")
        self.bt_cliente.setMinimumSize(QSize(0, 40))
        self.bt_cliente.setFont(font2)
        self.bt_cliente.setLayoutDirection(Qt.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u"usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cliente.setIcon(icon3)
        self.bt_cliente.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_cliente)

        self.bt_pp_cliente = QPushButton(self.frame_lateral)
        self.bt_pp_cliente.setObjectName(u"bt_pp_cliente")
        self.bt_pp_cliente.setMinimumSize(QSize(0, 40))
        self.bt_pp_cliente.setFont(font2)
        self.bt_pp_cliente.setLayoutDirection(Qt.RightToLeft)
        icon4 = QIcon()
        icon4.addFile(u"cliente.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_pp_cliente.setIcon(icon4)
        self.bt_pp_cliente.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_pp_cliente)

        self.bt_listas = QPushButton(self.frame_lateral)
        self.bt_listas.setObjectName(u"bt_listas")
        self.bt_listas.setMinimumSize(QSize(0, 40))
        self.bt_listas.setFont(font2)
        icon5 = QIcon()
        icon5.addFile(u"play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_listas.setIcon(icon5)
        self.bt_listas.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.bt_listas)

        self.verticalSpacer = QSpacerItem(20, 268, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_program = QLabel(self.frame_lateral)
        self.label_program.setObjectName(u"label_program")
        self.label_program.setMinimumSize(QSize(0, 50))
        font3 = QFont()
        font3.setFamily(u"Baskerville Old Face")
        font3.setPointSize(24)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_program.setFont(font3)
        self.label_program.setStyleSheet(u"background:qlineargradient(spread:pad, x1:1, y1:0.892, x2:0, y2:0.761136, stop:0.00497512 rgba(255, 255, 255, 255), stop:1 rgba(74, 68, 255, 255))")
        self.label_program.setScaledContents(False)
        self.label_program.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_program)


        self.horizontalLayout_3.addWidget(self.frame_lateral)

        self.frame_contenedor = QFrame(self.frame_inferior)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        self.frame_contenedor.setMinimumSize(QSize(1000, 0))
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_contenedor)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_contenedor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setStyleSheet(u"background:qlineargradient(spread:pad, x1:1, y1:0.892, x2:0, y2:0.761136, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(177, 175, 255, 255))")
        self.page_inicio = QWidget()
        self.page_inicio.setObjectName(u"page_inicio")
        self.verticalLayout_7 = QVBoxLayout(self.page_inicio)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.page_inicio)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(1000000, 1000000))
        font4 = QFont()
        font4.setPointSize(11)
        self.label.setFont(font4)

        self.verticalLayout_7.addWidget(self.label)

        self.stackedWidget.addWidget(self.page_inicio)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.volumen = QSlider(self.page)
        self.volumen.setObjectName(u"volumen")
        self.volumen.setMinimumSize(QSize(100, 20))
        font5 = QFont()
        font5.setBold(False)
        font5.setWeight(50)
        self.volumen.setFont(font5)
        self.volumen.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0.0695224, y1:0.943, x2:0.825871, y2:0.745, stop:0.00497512 rgba(255, 255, 255, 255), stop:1 rgba(74, 68, 255, 255))")
        self.volumen.setLocale(QLocale(QLocale.Spanish, QLocale.Spain))
        self.volumen.setSliderPosition(50)
        self.volumen.setOrientation(Qt.Horizontal)
        self.volumen.setInvertedAppearance(False)
        self.volumen.setTickInterval(10)
        self.volumen.setMinimum(0)
        self.volumen.setMaximum(100)


        self.gridLayout_2.addWidget(self.volumen, 1, 7, 1, 1)

        self.bt_pausar = QPushButton(self.page)
        self.bt_pausar.setObjectName(u"bt_pausar")
        icon6 = QIcon()
        icon6.addFile(u"pausar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_pausar.setIcon(icon6)
        self.bt_pausar.setIconSize(QSize(28, 28))

        self.gridLayout_2.addWidget(self.bt_pausar, 1, 4, 1, 1)

        self.tableView = QTableView(self.page)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setCornerButtonEnabled(True)

        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 10)

        self.bt_reproducir = QPushButton(self.page)
        self.bt_reproducir.setObjectName(u"bt_reproducir")
        self.bt_reproducir.setIcon(icon5)
        self.bt_reproducir.setIconSize(QSize(28, 28))

        self.gridLayout_2.addWidget(self.bt_reproducir, 1, 2, 1, 1)

        self.bt_reanudar = QPushButton(self.page)
        self.bt_reanudar.setObjectName(u"bt_reanudar")
        icon7 = QIcon()
        icon7.addFile(u"reanudar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_reanudar.setIcon(icon7)
        self.bt_reanudar.setIconSize(QSize(28, 28))

        self.gridLayout_2.addWidget(self.bt_reanudar, 1, 5, 1, 1)

        self.bt_canciones_2 = QPushButton(self.page)
        self.bt_canciones_2.setObjectName(u"bt_canciones_2")
        self.bt_canciones_2.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u"buscarc.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_canciones_2.setIcon(icon8)
        self.bt_canciones_2.setIconSize(QSize(28, 28))

        self.gridLayout_2.addWidget(self.bt_canciones_2, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(301, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 9, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(301, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.bt_detener = QPushButton(self.page)
        self.bt_detener.setObjectName(u"bt_detener")
        icon9 = QIcon()
        icon9.addFile(u"detener.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_detener.setIcon(icon9)
        self.bt_detener.setIconSize(QSize(28, 28))

        self.gridLayout_2.addWidget(self.bt_detener, 1, 6, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_6 = QVBoxLayout(self.page_1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.p_planes = QPushButton(self.page_1)
        self.p_planes.setObjectName(u"p_planes")
        self.p_planes.setStyleSheet(u"background-color:rgb(0, 0, 127)")

        self.verticalLayout_6.addWidget(self.p_planes)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.p_clientes = QPushButton(self.page_2)
        self.p_clientes.setObjectName(u"p_clientes")
        self.p_clientes.setStyleSheet(u"background-color:rgb(0, 255, 255)")

        self.verticalLayout_3.addWidget(self.p_clientes)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.p_pp_clientes = QPushButton(self.page_3)
        self.p_pp_clientes.setObjectName(u"p_pp_clientes")
        self.p_pp_clientes.setStyleSheet(u"background-color:rgb(0, 170, 255)")

        self.verticalLayout_8.addWidget(self.p_pp_clientes)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_5 = QVBoxLayout(self.page_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.p_listas = QPushButton(self.page_4)
        self.p_listas.setObjectName(u"p_listas")
        self.p_listas.setStyleSheet(u"background-color:rgb(170, 85, 255)")

        self.verticalLayout_5.addWidget(self.p_listas)

        self.stackedWidget.addWidget(self.page_4)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.frame_contenedor)


        self.gridLayout.addWidget(self.frame_inferior, 1, 0, 1, 1)

        self.frame_superior = QFrame(self.centralwidget)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 40))
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setStyleSheet(u"background-color:rgba(16, 57, 191, 200)")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bt_menu = QPushButton(self.frame_superior)
        self.bt_menu.setObjectName(u"bt_menu")
        self.bt_menu.setMinimumSize(QSize(250, 32))
        font6 = QFont()
        font6.setFamily(u"Georgia")
        font6.setPointSize(11)
        font6.setBold(True)
        font6.setUnderline(False)
        font6.setWeight(75)
        font6.setStrikeOut(False)
        self.bt_menu.setFont(font6)
        self.bt_menu.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"background-color:rgba(16, 57, 191, 227)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px solid #rgb(255, 255, 255);\n"
"background-color:rgb(255, 255, 255)\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"menus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon10)
        self.bt_menu.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_menu)

        self.horizontalSpacer = QSpacerItem(872, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.bt_ocultar = QPushButton(self.frame_superior)
        self.bt_ocultar.setObjectName(u"bt_ocultar")
        self.bt_ocultar.setMaximumSize(QSize(16777215, 35))
        self.bt_ocultar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"background-color:rgb(33, 0, 99)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px solid #rgb(0, 0, 255);\n"
"background-color:rgb(0, 0, 255)\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"ocultarp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_ocultar.setIcon(icon11)
        self.bt_ocultar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_ocultar)

        self.bt_minimizar = QPushButton(self.frame_superior)
        self.bt_minimizar.setObjectName(u"bt_minimizar")
        self.bt_minimizar.setMaximumSize(QSize(16777215, 35))
        self.bt_minimizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"background-color:rgb(33, 0, 99)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px solid #rgb(0, 0, 255);\n"
"background-color:rgb(0, 0, 255)\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"minimizarp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimizar.setIcon(icon12)
        self.bt_minimizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_minimizar)

        self.bt_maximizar = QPushButton(self.frame_superior)
        self.bt_maximizar.setObjectName(u"bt_maximizar")
        self.bt_maximizar.setMaximumSize(QSize(16777215, 35))
        self.bt_maximizar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"background-color:rgb(33, 0, 99)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px solid #rgb(0, 0, 255);\n"
"background-color:rgb(0, 0, 255)\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"maximizarp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_maximizar.setIcon(icon13)
        self.bt_maximizar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_maximizar)

        self.bt_cerrar = QPushButton(self.frame_superior)
        self.bt_cerrar.setObjectName(u"bt_cerrar")
        self.bt_cerrar.setMaximumSize(QSize(16777215, 35))
        self.bt_cerrar.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"background-color:rgb(33, 0, 99)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 5px solid #rgb(255, 0, 0);\n"
"background-color:rgb(255, 0, 0)\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"cerrarp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_cerrar.setIcon(icon14)
        self.bt_cerrar.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_cerrar)


        self.gridLayout.addWidget(self.frame_superior, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_inicio.setText(QCoreApplication.translate("MainWindow", u"\u00bfQue es SpotyUN?", None))
        self.bt_canciones.setText(QCoreApplication.translate("MainWindow", u"  CANCIONES", None))
        self.bt_planes.setText(QCoreApplication.translate("MainWindow", u"  PLANES  ", None))
        self.bt_cliente.setText(QCoreApplication.translate("MainWindow", u"  CLIENTE", None))
        self.bt_pp_cliente.setText(QCoreApplication.translate("MainWindow", u"PLANES CLIENTE     ", None))
        self.bt_listas.setText(QCoreApplication.translate("MainWindow", u"  MI LISTA", None))
        self.label_program.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-style:italic; color:#000000; vertical-align:super;\">SpotyUN</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nulla culpa nostrud amet nostrud qui nisi qui incididunt ipsum minim amet. In non cupidatat velit magna in dolore ea dolore cupidatat do. Esse id eiusmod in fugiat amet veniam quis consequat. Dolore proident cupidatat aliquip dolore proident. Non laborum labore voluptate do anim ipsum velit ea dolor. Nisi eiusmod mollit non elit minim ullamco qui velit laborum ut. Deserunt ea cillum aliqua laborum pariatur.\n"
"\n"
"Do elit ad occaecat eiusmod dolor dolore ullamco ullamco eiusmod nostrud aliqua eiusmod minim. Aliqua deserunt ea do officia officia non voluptate. Nostrud occaecat cupidatat culpa occaecat. Dolor do in Lorem aute eiusmod elit proident. Ut eiusmod ad nostrud pariatur est. Cupidatat magna ullamco minim non.\n"
"\n"
"Laboris cillum consequat mollit anim tempor consequat fugiat exercitation. Et Lorem ad mollit irure amet eu cupidatat reprehenderit sunt fugiat enim labore proident. Eu reprehenderit ex pariatur sit nostrud in consequat. Voluptate quis consequat tempor in minim anim pariatur in reprehend"
                        "erit. Cillum voluptate mollit sunt elit sint consequat incididunt aliqua reprehenderit Lorem dolore sunt excepteur occaecat. Elit adipisicing ex in cupidatat ut ex fugiat eu ipsum et magna qui ipsum incididunt. Nulla excepteur velit tempor qui eiusmod deserunt anim irure qui elit.", None))
        self.bt_pausar.setText("")
        self.bt_reproducir.setText("")
        self.bt_reanudar.setText("")
        self.bt_canciones_2.setText("")
        self.bt_detener.setText("")
        self.p_planes.setText(QCoreApplication.translate("MainWindow", u"Planes", None))
        self.p_clientes.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.p_pp_clientes.setText(QCoreApplication.translate("MainWindow", u"Planes cliente", None))
        self.p_listas.setText(QCoreApplication.translate("MainWindow", u"Mi lista", None))
        self.bt_menu.setText(QCoreApplication.translate("MainWindow", u"  MENU", None))
        self.bt_ocultar.setText("")
        self.bt_minimizar.setText("")
        self.bt_maximizar.setText("")
        self.bt_cerrar.setText("")
    # retranslateUi

