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
        
        super().__init__(parent)
        loadUi("mainWindow.ui", self)

        
    
    
    
if __name__ == "__main__":    
    
    app = QApplication(sys.argv)
    ventana = Main()
    ventana.show()
    sys.exit(app.exec())