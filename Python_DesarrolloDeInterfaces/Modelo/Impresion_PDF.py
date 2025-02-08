from fpdf import FPDF

from ..DAO.Conexion import Conexion

class Impresion_PDF(FPDF):
    
    def header(self):
    #    self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Fichajes', 0, 1, 'C')
    
    def footer(self):
        self.set_y(-15)
    #    self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Pagina %s' % self.page_no(), 0, 0, 'C')
    
    def chapter_title(self, title):
    #    self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)
    
    def chapter_body(self, body):
    #    self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()
        
    def aniadir_fila(self, nombre, fecha, hora, estado):
                       
    #    self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Nombre: {nombre}', 0, 1)
        self.cell(0, 10, f'Fecha: {fecha}', 0, 1)
        self.cell(0, 10, f'Hora: {hora}', 0, 1)
        self.cell(0, 10, f'Estado: {estado}', 0, 1)
        self.ln(10)

  
    def crear(self, fecha_desde, fecha_hasta, trabajadores):
                
        file = 'fichajes_' + fecha_desde.toString("yyyy-MM-dd") + '_' + fecha_hasta.toString("yyyy-MM-dd") + '.pdf'
        
        pdf = FPDF()
        
        pdf.add_page()
    #    pdf.set_font('Arial', 'B', 16)
        pdf.header()
        self.chapter_title('Fichajes')
          
        self.obtener_fichajes(fecha_desde, fecha_hasta, trabajadores)
        
        self.footer()
        self.output(file)

    def obtener_fichajes(self, fecha_desde, fecha_hasta, idtrs, pdf):
        conexion = Conexion().get_connection()                       
        cursor = conexion.cursor()
                        
        query_nombre = 'SELECT nombre FROM Reloj WHERE idtr = ? WHERE fecha BETWEEN ? AND ?'
        query_fecha = 'SELECT fecha FROM Reloj WHERE idtr = ? WHERE fecha BETWEEN ? AND ?'
        query_hora = 'SELECT hora FROM Reloj WHERE idtr = ? WHERE fecha BETWEEN ? AND ?'
        query_estado = 'SELECT estado FROM Reloj WHERE idtr = ? WHERE fecha BETWEEN ? AND ?'
        
        cursor.execute(query_nombre, (idtr, fecha_desde, fecha_hasta))
        nombres = cursor.fetchall()
        
        cursor.execute(query_fecha, (idtr, fecha_desde, fecha_hasta))
        fechas = cursor.fetchall()
        
        cursor.execute(query_hora, (idtr, fecha_desde, fecha_hasta))
        horas = cursor.fetchall()
        
        cursor.execute(query_estado, (idtr, fecha_desde, fecha_hasta))
        estados = cursor.fetchall()
        
        for idtr in idtrs:
            
            pdf.anidar_fila(nombres[idtr], fechas[idtr], horas[idtr], estados[idtr])
            
        
        cursor.close()
        conexion.close()