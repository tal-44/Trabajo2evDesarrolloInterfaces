from fpdf import FPDF
import os
from DAO.Conexion import Conexion

class Impresion_PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.unifontsubset = False
    
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Fichajes', 0, 1, 'C')
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')
    
    def aniadir_fila(self, fecha, hora, estado):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Fecha: {fecha}    Hora: {hora}    Estado: {estado}', 0, 1)
        self.ln(1)
        self.set_draw_color(0, 0, 0)
        self.line(10, self.get_y(), 200, self.get_y())
  
    def crear(self, fecha_desde, fecha_hasta, trabajadores):
        directorio = 'pdfs_fichajes'
        os.makedirs(directorio, exist_ok=True)
        
        file = os.path.join(directorio, f'fichajes_{fecha_desde.toString("yyyy-MM-dd")}_{fecha_hasta.toString("yyyy-MM-dd")}.pdf')
        
        self.add_page()
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Fichajes', 0, 1, 'L')
        self.ln(4)
          
        self.obtener_fichajes(fecha_desde, fecha_hasta, trabajadores)
        
        self.output(file)

    def obtener_fichajes(self, fecha_desde, fecha_hasta, idtrs):
        conexion = None
        cursor = None
        
        try:
            conexion = Conexion().get_connection()
            cursor = conexion.cursor()

            query_fichajes = 'SELECT fecha, hora, estado FROM Reloj WHERE idtr = ? AND fecha BETWEEN ? AND ?'
            query_nombre = 'SELECT nombre FROM Trabajador WHERE idtr = ?'

            for idtr in idtrs:
                cursor.execute(query_nombre, (idtr,))
                resultado_nombre = cursor.fetchone()
                nombre = resultado_nombre[0] if resultado_nombre else 'Desconocido'
                
                cursor.execute(query_fichajes, (idtr, fecha_desde.toString("yyyy-MM-dd"), fecha_hasta.toString("yyyy-MM-dd")))
                fichajes = cursor.fetchall()
                
                self.ln(4)
                self.set_font('Arial', 'B', 14)
                self.cell(0, 10, f'Trabajador ID: {idtr}, Nombre: {nombre}', 0, 1)
                self.ln(4)
                
                if fichajes:
                    self.set_draw_color(0, 0, 0)
                    self.line(10, self.get_y(), 200, self.get_y())
                    
                    for fecha, hora, estado in fichajes:
                        self.aniadir_fila(fecha, hora, estado)
                else:
                    self.cell(0, 10, 'No hay fichajes', 0, 1)
                    self.ln(10)
        
        except Exception as e:
            print(f'Error obteniendo fichajes: {e}')
        
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
