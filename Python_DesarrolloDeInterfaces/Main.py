from datetime import *
import time
"""
from Fichaje import *
from Trabajador import *
"""
import sqlite3
import io
from io import *
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve
from PyQt6 import QtCore, QtWidgets
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt, QTimer, QTime, QDate, pyqtSlot

class Main(QMainWindow):
    
    def __init__(self, parent=None):
        
        """
        Summary
        
        
        """
        
        """       
        from DAO import Conexion  # Assuming Conexion is defined in Fichaje module
        
        conexion = Conexion().get_connection()
        self.cursor = conexion.cursor()
        
        print(self.cursor.execute("SELECT * FROM Trabajador"))
        
        conexion.commit()
        
        self.cursor.close()
        Conexion.close_connection(conexion)
        """        
        
        super(Main, self).__init__()
        super().__init__(parent)
        loadUi("mainWindow.ui", self)
        
        self.mostrarInfo("sin mensajes")
        self.mostrarPanelFichar()
        
        self.btn_Fichar.clicked.connect(self.mostrarPanelFichar)
        self.btn_Imprimir.clicked.connect(self.mostrarPanelImprimir)
        
        self.btn_EmitirFichaje.clicked.connect(self.emitirFichaje)

        
    def mostrarInfo(self, mensaje):
        
        self.textEdit_PanelMensajes.setText(mensaje)
        self.textEdit_PanelMensajes.show()
        
    def mostrarPanelFichar(self):
        
        self.stackedWidget.setCurrentIndex(1)
        
        self.update_label()
        
    def mostrarPanelImprimir(self):        
        self.stackedWidget.setCurrentIndex(0)
        
    def emitirFichaje(self):
        
        codigo = self.textEdit_TeclearCodigo.toPlainText()
        
        if codigo == "":
            self.mostrarInfo("Introduzca un codigo")
            return
        
        try:
            
            conexion = Conexion.get_connection()
            cursor = conexion.cursor()
            
            query = 'SELECT * FROM trabajador WHERE idtr = ?'          ***  
            parametro = codigo
            
            cursor.execute(query, (parametro,))
            
            self.textEdit_PanelMensajes.setText("Fichaje realizado")
            
            conexion.commit()
        
        except sqlite3.Error as e:
            print(e)
                        
        finally:
            Conexion.close_connection(conexion)

        
    def update_label(self):
        """
        Actualiza aas estiquetas de dia y hora y ejecuta un temporizador para actualizar las etiquetas cada segundo
        
        """
        
        fecha_actual = QDate.currentDate()
        hora_actual = QTime.currentTime()
        self.textEdit_Fecha.setText(fecha_actual.toString())
        self.textEdit_Hora.setText(hora_actual.toString())
        
        timer = QTimer(self)
        timer.timeout.connect(self.update_label)
        timer.start(1000)
    
    
if __name__ == "__main__":    
    
    app = QApplication(sys.argv)
    ventana = Main()
    ventana.show()
    sys.exit(app.exec())