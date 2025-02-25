from datetime import *
import sqlite3
from io import *
import sys
import os

from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt, QTimer, QTime, QDate, pyqtSlot
import logging

from DAO.Conexion import Conexion
from Log.Log import Log
from Modelo.Impresion_PDF import Impresion_PDF
import smtplib
from email.mime.text import MIMEText
from Modelo.EnviarEmailAviso import enviarEmailAviso

class Main(QMainWindow):
    
    logging.basicConfig(filename='log/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def __init__(self, parent=None):
        
        super().__init__(parent)
        loadUi("mainWindow.ui", self)

        self.mostrarInfo("Sin mensajes")
        self.mostrarPanelFichar()

        
        self.btn_Fichar.clicked.connect(self.mostrarPanelFichar)
        self.btn_Imprimir.clicked.connect(self.mostrarPanelImprimir)
        self.btn_EmitirFichaje.clicked.connect(self.emitirFichaje)
        self.pushButtonImprimir.clicked.connect(self.imprimir)

        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)
        self.timer.start(1000)

        
        self.timer_verificar_hora = QTimer(self)
        self.timer_verificar_hora.timeout.connect(self.verificar_hora)
        self.timer_verificar_hora.start(60000)  # Verificar cada minuto
        
    def verificar_hora(self):
        
        ahora = datetime.now().time()
        if ahora.hour == 0 and ahora.minute == 0:
            trabajadores_in = self.verificar_fichajes_no_cerrados()
        
        if trabajadores_in:
            mensaje = "Fichajes realizados a las 12 de la noche.\n"
            mensaje += "Los siguientes trabajadores no cerraron su fichaje:\n"
            for idtr, nombre in trabajadores_in:
                mensaje += f"- {nombre} (ID: {idtr})\n"
        else:
            mensaje = "Fichajes realizados a las 12 de la noche.\n"
            mensaje += "Todos los trabajadores han cerrado su fichaje correctamente."
            
            self.enviar_correo_aviso("Fichajes realizados a las 12 de la noche.")
            
    def verificar_fichajes_no_cerrados(self):
   
    
        try:
            conexion = Conexion().get_connection()
            cursor = conexion.cursor()

            # Consulta para buscar trabajadores con estado 'IN'
            cursor.execute('SELECT idtr, Nombre FROM Trabajador WHERE Estado = ?', ('IN',))
            trabajadores_in = cursor.fetchall()

            cursor.close()
            
            for idtr, nombre in trabajadores_in:
                Log.log_error(f"El trabajador {nombre} (ID: {idtr}) no cerró su fichaje")
                
                cursor.execute('INSERT INTO Reloj (idtr, Nombre, Fecha, Hora, estado) VALUES (?, ?, ?, ?, ?)', (idtr, nombre, QDate.currentDate().toString("yyyy-MM-dd"), QTime.currentTime().toString("HH:mm:ss"), 'OUT'))
                cursor.execute('UPDATE Trabajador SET Estado = ? WHERE idtr = ?', ('OUT', idtr))
                Log.log_fichaje(idtr, 'OUT', nombre)
                            
            return trabajadores_in  # Devuelve una lista de tuplas (idtr, nombre)
        except sqlite3.Error as e:
            Log.log_error(f"Error al verificar fichajes no cerrados: {e}")
            return []  # Devuelve una lista vacía en caso de error
        finally:
            Conexion().close_connection(conexion)

    def enviar_correo_aviso(self, mensaje):        
        enviarEmailAviso(self, mensaje)

    def closeEvent(self, event):
         # Verificar si hay trabajadores con estado 'IN'
        trabajadores_in = self.verificar_fichajes_no_cerrados()
    
        if trabajadores_in:
            mensaje = "La aplicación se está cerrando.\n"
            mensaje += "Los siguientes trabajadores no cerraron su fichaje:\n"
            for idtr, nombre in trabajadores_in:
                mensaje += f"- {nombre} (ID: {idtr})\n"
        else:
            mensaje = "La aplicación se está cerrando.\n"
            mensaje += "Todos los trabajadores han cerrado su fichaje correctamente."

        # Enviar correo con el mensaje
        self.enviar_correo_aviso(mensaje)

        # Aceptar el evento de cierre
        event.accept()

    def mostrarInfo(self, mensaje):
        """Muestra un mensaje en el panel de mensajes."""
        self.textEdit_PanelMensajes.setText(mensaje)
        self.textEdit_PanelMensajes.show()

    def mostrarPanelFichar(self):
        
        self.stackedWidget.setCurrentIndex(1)
        self.btn_Imprimir.show()
        self.btn_Fichar.hide()
        self.buttonBox.hide()
        self.update_label()
        self.textEdit_TeclearCodigo.setFocus()

    def mostrarPanelImprimir(self):        
        
        self.stackedWidget.setCurrentIndex(0)
        self.btn_Fichar.show()
        self.btn_Imprimir.hide()
        self.buttonBox.hide()
        self.dateEdit_FechaDesde.setDate(QDate.currentDate())
        self.dateEdit_FechaHasta.setDate(QDate.currentDate())
        self.mostrarListaTrabajadores()

    def mostrarListaTrabajadores(self):
        
        try:
            conexion = Conexion().get_connection()            
            cursor = conexion.cursor() 
            cursor.execute('SELECT Nombre FROM Trabajador')
            nombres = cursor.fetchall()
            self.listWidget_Trabajadores.clear()

            for nombre in nombres:
                item = QtWidgets.QListWidgetItem(nombre[0])
                self.listWidget_Trabajadores.addItem(item)

            conexion.commit()
            cursor.close()
        except sqlite3.Error as e:
            Log.log_error(e)
        finally:
            Conexion().close_connection(conexion)

    def emitirFichaje(self):
        
        codigo = self.textEdit_TeclearCodigo.toPlainText().strip()
                
        if not codigo:
            self.mostrarInfo("Introduzca un código")
            Log.log_error("Código no introducido")
            self.textEdit_TeclearCodigo.setFocus()
            return

        try:
            conexion = Conexion().get_connection()
            cursor = conexion.cursor()

            cursor.execute('SELECT Estado, Nombre FROM Trabajador WHERE idtr = ?', (codigo,))
            resultado = cursor.fetchone()

            if resultado is None:
                self.mostrarInfo("Código no válido")
                Log.log_error("Código no válido")
                self.textEdit_TeclearCodigo.clear()
                self.textEdit_TeclearCodigo.setFocus()
                return
            
            estado, nombre = resultado
            conexion.commit()
            cursor.close()

            self.textEdit_PanelMensajes.setText(f"{nombre} {estado}, ¿Acepta el fichaje?")
            self.buttonBox.show()
            
            try:
                self.buttonBox.accepted.disconnect()
                self.buttonBox.rejected.disconnect()
            except TypeError:
                pass

            self.buttonBox.accepted.connect(lambda: self.confirmar_fichaje(codigo, nombre, estado))
            self.buttonBox.rejected.connect(lambda: self.cancelar_fichaje(codigo, nombre))

        except sqlite3.Error as e:
            Log.log_error(e)
        finally:
            Conexion().close_connection(conexion)

    def confirmar_fichaje(self, codigo, nombre, estado):
        
        try:
            conexion = Conexion().get_connection()
            cursor = conexion.cursor()
            
            nuevo_estado = "OUT" if estado == "IN" else "IN"
            
            cursor.execute('UPDATE Trabajador SET Estado = ? WHERE idtr = ?', (nuevo_estado, codigo,))
            cursor.execute('INSERT INTO Reloj (idtr, Nombre, Fecha, Hora, estado) VALUES (?, ?, ?, ?, ?)',
                           (codigo, nombre, QDate.currentDate().toString("yyyy-MM-dd"), QTime.currentTime().toString("HH:mm:ss"), nuevo_estado))

            Log.log_fichaje(codigo, nuevo_estado, nombre)
            self.mostrarInfo("Fichaje realizado")
            self.buttonBox.hide()
            self.textEdit_TeclearCodigo.clear()
            self.textEdit_TeclearCodigo.setFocus()

            conexion.commit()
            cursor.close()
        except sqlite3.Error as e:
            Log.log_error(e)
        finally:
            Conexion().close_connection(conexion)
            self.buttonBox.accepted.disconnect()
            self.buttonBox.rejected.disconnect()

    def cancelar_fichaje(self, codigo, nombre):
        
        Log.log_fichaje_rechazado(codigo, nombre)
        self.mostrarInfo("Fichaje cancelado")
        self.buttonBox.hide()
        self.textEdit_TeclearCodigo.clear()
        self.textEdit_TeclearCodigo.setFocus()

    def imprimir(self):
        
        trabajadores = self.listWidget_Trabajadores.selectedItems()

        if not trabajadores:
            self.mostrarInfo("No se han seleccionado trabajadores")
            Log.log_error("No se han seleccionado trabajadores")
            return
        
        fecha_desde = self.dateEdit_FechaDesde.date()
        fecha_hasta = self.dateEdit_FechaHasta.date()

        if fecha_desde > fecha_hasta:
            self.mostrarInfo("Las fechas no son coherentes")
            Log.log_error("Las fechas no son coherentes")
            return

        self.crear_PDF(trabajadores, fecha_desde, fecha_hasta)

    def crear_PDF(self, trabajadores, fecha_desde, fecha_hasta):
        
        try:
            conexion = Conexion().get_connection()
            cursor = conexion.cursor()

            idtrs = []
            for trabajador in trabajadores:
                cursor.execute('SELECT idtr FROM Trabajador WHERE nombre = ?', (trabajador.text(),))
                resultado = cursor.fetchone()
                if resultado:
                    idtrs.append(resultado[0])

            Impresion_PDF().crear(fecha_desde, fecha_hasta, trabajadores=idtrs)
            self.mostrarInfo("PDF creado")
            cursor.close()
        except sqlite3.Error as e:
            Log.log_error(e)
        finally:
            Conexion().close_connection(conexion)

    def update_label(self):
        """Actualiza la hora y fecha cada segundo."""
        self.textEdit_Fecha.setText(QDate.currentDate().toString("dd/MM/yy"))
        self.textEdit_Hora.setText(QTime.currentTime().toString("HH:mm:ss"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Main()
    ventana.show()
    sys.exit(app.exec())