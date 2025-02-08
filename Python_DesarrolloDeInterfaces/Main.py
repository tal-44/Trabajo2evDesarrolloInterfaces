from DAO import Conexion
from Log import Log
from Modelo import Impresion_PDF

"""
from Fichaje import *
from Trabajador import *
"""

from datetime import *
import sqlite3
from io import *
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt, QTimer, QTime, QDate, pyqtSlot
import logging

class Main(QMainWindow):
    
    logging.basicConfig(filename='log/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        
    def __init__(self, parent=None):
        
        """
        Summary
        
        
        """
        
        super(Main, self).__init__()
        super().__init__(parent)
        loadUi("mainWindow.ui", self)
        
        self.mostrarInfo("sin mensajes")
        self.mostrarPanelFichar()
        
        self.btn_Fichar.clicked.connect(self.mostrarPanelFichar)
        self.btn_Imprimir.clicked.connect(self.mostrarPanelImprimir)
        
        self.btn_EmitirFichaje.clicked.connect(self.emitirFichaje)
        self.pushButtonImprimir.clicked.connect(self.imprimir)

        
    def mostrarInfo(self, mensaje):
        '''
        Muestra un mensaje en el panel de mensajes
        '''
        
        self.textEdit_PanelMensajes.setText(mensaje)
        self.textEdit_PanelMensajes.show()
        
    def mostrarPanelFichar(self):
        self.stackedWidget.setCurrentIndex(1)
        self.btn_Imprimir.show()
        self.btn_Fichar.hide()
        self.buttonBox.hide()
        
        self.update_label()
        self.update_label_panelMensajes()
        
        self.textEdit_TeclearCodigo.setFocus()
        
    def mostrarPanelImprimir(self):        
        self.stackedWidget.setCurrentIndex(0)
        self.btn_Fichar.show()
        self.btn_Imprimir.hide()
        self.buttonBox.hide()
        
        self.dateEdit_FechaDesde.setDate(QDate.currentDate())
        self.dateEdit_FechaHasta.setDate(QDate.currentDate())
        
        self.update_label_panelMensajes()
        self.mostrarListaTrabajadores()
        
    def mostrarListaTrabajadores(self):
        '''
        Metodo que hace una consulta a la base de datos y muestra los trabajadores en el listWidget
        '''
        
        try:
            conexion = Conexion().get_connection()            
            cursor = conexion.cursor() 
            
            query = 'SELECT Nombre FROM Trabajador'
            
            cursor.execute(query)
            
            nombres = cursor.fetchall()
            
            self.listWidget_Trabajadores.clear()
            for nombre in nombres:
                item = QtWidgets.QListWidgetItem(nombre[0])
                self.listWidget_Trabajadores.addItem(item)
            
            
            cursor.close()
            conexion.commit()
            
        except sqlite3.Error as e:
            Log.log_error(e)
            
        finally:
            Conexion().close_connection(conexion)
        
    def emitirFichaje(self):
        '''
        Comprueba el codigo introducido y realiza el fichaje si es correcto
        '''
        
        codigo = self.textEdit_TeclearCodigo.toPlainText()        
                
        if codigo == "" or codigo is None:
            self.mostrarInfo("Introduzca un codigo")
            Log.log_error("Codigo no introducido")
            return
        
        try:            
            
            conexion = Conexion().get_connection()                       
            cursor = conexion.cursor()
                        
            query = 'SELECT Estado FROM Trabajador WHERE idtr = ?'
            
            cursor.execute(query, (codigo,))
            estado = cursor.fetchone()
            
            if estado is None:
                self.textEdit_PanelMensajes.setText("Codigo no valido")
                Log.log_error("Codigo no valido")
                return
            
            estado = estado[0]
            
            if estado == 'IN':
                estado = 'OUT'
            else:
                estado = 'IN'
                
            query = 'UPDATE Trabajador SET Estado = ? WHERE idtr = ?'
            
            cursor.execute(query, (estado, codigo,))
                        
            query = 'SELECT Nombre FROM Trabajador WHERE idtr = ?'
            
            cursor.execute(query, (codigo,))
            nombre = cursor.fetchone()[0]
            
            cursor.close()
            conexion.commit()
            
            self.buttonBox.show()
            self.textEdit_PanelMensajes.setText(nombre + ' ' + estado + ', ¿Acepta el fichaje?')
            
            self.buttonBox.accepted.connect(lambda: self.confirmar_fichaje(cursor, conexion, codigo, nombre, estado))
            self.buttonBox.rejected.connect(lambda: self.cancelar_fichaje(codigo, nombre, cursor))
                    
        except sqlite3.Error as e:
            print(e)
            Log.log_error(e)
                        
        finally:
            Conexion().close_connection(conexion)
            
    def confirmar_fichaje(self, cursor, conexion, codigo, nombre, estado):
        
        try:
            
        
            conexion = Conexion().get_connection()                       
            cursor = conexion.cursor()
        
            query = 'INSERT INTO Reloj (idtr, nombre, fecha, hora, estado) VALUES (?, ?, ?, ?, ?)'
            cursor.execute(query, (codigo, nombre, QDate.currentDate().toString(), QTime.currentTime().toString(), estado))
        
            Log.log_fichaje(codigo, estado, nombre)
        
            self.textEdit_PanelMensajes.setText("Fichaje realizado")
        
            self.buttonBox.hide()        
            self.textEdit_TeclearCodigo.setText("")
            self.textEdit_TeclearCodigo.setFocus()
                
            cursor.close()
            conexion.commit()
             
        except sqlite3.Error as e:
            print(e)
            Log.log_error(e)    
        finally:
            Conexion().close_connection(conexion)
        
    def cancelar_fichaje(self, codigo, nombre, cursor):
        
        Log.log_fichaje_rechazado(codigo, nombre)
        
        self.textEdit_PanelMensajes.setText("Fichaje cancelado")
        
        self.buttonBox.hide()
        self.textEdit_TeclearCodigo.setText("")
        self.textEdit_TeclearCodigo.setFocus()
            
    def imprimir(self):
        
        trabajadores = self.listWidget_Trabajadores.selectedItems()
        
        if len(trabajadores) == 0:
            self.mostrarInfo("No se han seleccionado trabajadores")
            Log.log_error("No se han seleccionado trabajadores")
            return

    #    fecha_desde = self.dateEdit_FechaDesde.date().toString()
    #    fecha_hasta = self.dateEdit_FechaHasta.date().toString()
        
        fecha_desde = self.dateEdit_FechaDesde.date()
        fecha_hasta = self.dateEdit_FechaHasta.date()
        
        if fecha_desde > fecha_hasta:
            self.mostrarInfo("Las fechas no son coherentes")
            Log.log_error("Las fechas no son coherentes")
            return
        
        try:
            
            conexion = Conexion().get_connection()
            cursor = conexion.cursor()
            
            query = 'SELECT idtr FROM Trabajador WHERE nombre = ?'
            
            idtrs = []
            
            for trabajador in trabajadores:
                
                cursor.execute(query, (trabajador.text(),))
                idtr = cursor.fetchone()[0]
                
                idtrs.append(idtr)
                
            impresion_pdf = Impresion_PDF()
            impresion_pdf.crear(fecha_desde, fecha_hasta, trabajadores=idtrs)
                 
            cursor.close()
                
            
        
        except sqlite3.Error as e:
            print(e)
            Log.log_error(e)
        finally:
            Conexion().close_connection(conexion)

        
    def update_label(self):
        """
        Actualiza aas estiquetas de dia y hora y ejecuta un temporizador para actualizar las etiquetas cada segundo
        
        """
        
        fecha_actual = QDate.currentDate()
        hora_actual = QTime.currentTime()
        self.textEdit_Fecha.setText(fecha_actual.toString("dd/MM/yy"))
        self.textEdit_Hora.setText(hora_actual.toString("HH:mm:ss"))
        
        timer = QTimer(self)
        timer.timeout.connect(self.update_label)
        timer.singleShot(1000, self.update_label)
        
    def update_label_panelMensajes(self):
        
        self.textEdit_PanelMensajes.setText("")
        
        timer = QTimer(self)
        timer.timeout.connect(self.update_label_panelMensajes)
        timer.singleShot(10000, self.update_label_panelMensajes)
    
    
if __name__ == "__main__":    
    
    app = QApplication(sys.argv)
    ventana = Main()
    ventana.show()
    sys.exit(app.exec())