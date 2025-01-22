# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateEdit, QDialogButtonBox,
    QHBoxLayout, QLabel, QListView, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(807, 600)
        MainWindow.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widgetIzquierda = QWidget(self.centralwidget)
        self.widgetIzquierda.setObjectName(u"widgetIzquierda")
        self.widgetIzquierda.setGeometry(QRect(-1, -1, 191, 581))
        self.widgetIzquierda.setStyleSheet(u"background-color:rgb(206, 151, 0);")
        self.btn_Imprimir = QPushButton(self.widgetIzquierda)
        self.btn_Imprimir.setObjectName(u"btn_Imprimir")
        self.btn_Imprimir.setGeometry(QRect(20, 120, 151, 61))
        self.btn_Imprimir.setStyleSheet(u"background-color:rgb(180, 180, 180);\n"
"font-size: 20px;")
        self.btn_Fichar = QPushButton(self.widgetIzquierda)
        self.btn_Fichar.setObjectName(u"btn_Fichar")
        self.btn_Fichar.setGeometry(QRect(20, 40, 151, 61))
        self.btn_Fichar.setStyleSheet(u"background-color:rgb(180, 180, 180);\n"
"font-size: 20px;\n"
"")
        self.widgetAbajo = QWidget(self.centralwidget)
        self.widgetAbajo.setObjectName(u"widgetAbajo")
        self.widgetAbajo.setGeometry(QRect(189, 419, 621, 161))
        self.widgetAbajo.setStyleSheet(u"background-color:rgb(151, 0, 206);")
        self.buttonBox = QDialogButtonBox(self.widgetAbajo)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(400, 30, 193, 71))
        self.buttonBox.setStyleSheet(u"background-color:rgb(180, 180, 180);")
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.textEdit_PanelMensajes = QTextEdit(self.widgetAbajo)
        self.textEdit_PanelMensajes.setObjectName(u"textEdit_PanelMensajes")
        self.textEdit_PanelMensajes.setGeometry(QRect(30, 10, 351, 101))
        self.textEdit_PanelMensajes.setStyleSheet(u"background-color:rgb(255, 255, 255);")
        self.textEdit_PanelMensajes.setReadOnly(True)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(190, 0, 621, 421))
        self.stackedWidget.setFocusPolicy(Qt.WheelFocus)
        self.stackedWidget.setStyleSheet(u"background-color:rgb(0, 146, 181);")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.horizontalLayoutWidget = QWidget(self.page_1)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(70, 70, 461, 99))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font-size: 30px;")

        self.verticalLayout.addWidget(self.label_2)

        self.dateEdit_FechaDesde = QDateEdit(self.horizontalLayoutWidget)
        self.dateEdit_FechaDesde.setObjectName(u"dateEdit_FechaDesde")
        self.dateEdit_FechaDesde.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"font-size: 30px;")

        self.verticalLayout.addWidget(self.dateEdit_FechaDesde)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font-size: 30px;")

        self.verticalLayout_2.addWidget(self.label_5)

        self.dateEdit_FechaHasta = QDateEdit(self.horizontalLayoutWidget)
        self.dateEdit_FechaHasta.setObjectName(u"dateEdit_FechaHasta")
        self.dateEdit_FechaHasta.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"font-size: 30px;")

        self.verticalLayout_2.addWidget(self.dateEdit_FechaHasta)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayoutWidget_3 = QWidget(self.page_1)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(70, 220, 251, 151))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.verticalLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-size: 20px;")

        self.verticalLayout_3.addWidget(self.label_6)

        self.listView_EstadoTrabajadores = QListView(self.verticalLayoutWidget_3)
        self.listView_EstadoTrabajadores.setObjectName(u"listView_EstadoTrabajadores")
        self.listView_EstadoTrabajadores.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.listView_EstadoTrabajadores)

        self.pushButtonImprimir = QPushButton(self.page_1)
        self.pushButtonImprimir.setObjectName(u"pushButtonImprimir")
        self.pushButtonImprimir.setGeometry(QRect(390, 270, 93, 28))
        self.pushButtonImprimir.setStyleSheet(u"background-color:rgb(180, 180, 180);\n"
"font-size: 20px;")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.btn_EmitirFichaje = QPushButton(self.page_2)
        self.btn_EmitirFichaje.setObjectName(u"btn_EmitirFichaje")
        self.btn_EmitirFichaje.setGeometry(QRect(230, 320, 151, 61))
        self.btn_EmitirFichaje.setStyleSheet(u"background-color:rgb(180, 180, 180);\n"
"font-size: 20px;")
        self.textEdit_Hora = QTextEdit(self.page_2)
        self.textEdit_Hora.setObjectName(u"textEdit_Hora")
        self.textEdit_Hora.setGeometry(QRect(330, 60, 251, 87))
        font = QFont()
        font.setPointSize(24)
        self.textEdit_Hora.setFont(font)
        self.textEdit_Hora.setStyleSheet(u"background-color:rgb(255, 255, 255);")
        self.textEdit_Fecha = QTextEdit(self.page_2)
        self.textEdit_Fecha.setObjectName(u"textEdit_Fecha")
        self.textEdit_Fecha.setGeometry(QRect(50, 60, 251, 87))
        self.textEdit_Fecha.setFont(font)
        self.textEdit_Fecha.setStyleSheet(u"background-color:rgb(255, 255, 255);")
        self.horizontalLayoutWidget_2 = QWidget(self.page_2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(50, 170, 401, 89))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 30px;")

        self.horizontalLayout_2.addWidget(self.label)

        self.textEdit_TeclearCodigo = QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_TeclearCodigo.setObjectName(u"textEdit_TeclearCodigo")
        self.textEdit_TeclearCodigo.setStyleSheet(u"background-color:rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.textEdit_TeclearCodigo)

        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_Imprimir.setText(QCoreApplication.translate("MainWindow", u"imprimir", None))
        self.btn_Fichar.setText(QCoreApplication.translate("MainWindow", u"fichar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Fecha desde", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Fecha hasta", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Estado trabajadores", None))
        self.pushButtonImprimir.setText(QCoreApplication.translate("MainWindow", u"Imprimir", None))
        self.btn_EmitirFichaje.setText(QCoreApplication.translate("MainWindow", u"Emitir Fichaje", None))
        self.textEdit_Hora.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">HH : MM</span></p></body></html>", None))
        self.textEdit_Fecha.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">Dia / Mes / A\u00f1o</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Teclea tu c\u00f3digo", None))
    # retranslateUi

