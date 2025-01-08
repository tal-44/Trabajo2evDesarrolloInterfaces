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
        self.conexion = sqlite3.connect("BBDDTrabajadoresYReloj.db")
        self.cursor = self.conexion.cursor()
        
        print(self.cursor.execute("SELECT * FROM Trabajador"))
        
        self.conexion.commit()
        
        self.cursor.close()
        self.conexion.close()
        """        
        
        super().__init__(parent)
        loadUi("mainWindow.ui", self)
        
        self.update_label()

        
    def mostrarInfo(self):
        self.lblMensajes.setText()
        self.lblMensajes.show()
        
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