import sqlite3

class Conexion:
    
    """
    Conexion con la base de datos de DB Browser SQLite
    """
    
    __db__path = "C:\Users\juanm_ccji0p9\repos-git\Trabajo2evDesarrolloInterfaces\Python_DesarrolloDeInterfaces\BBDDTrabajadoresYReloj.db"
    
    def get_connection(self):
        """
        Devuelve una conexion con la base de datos
        """
        try:
            conexion = sqlite3.connect(Conexion.__db__path)
            print("Conexion establecida")
            return conexion
        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None
        
    def close_connection(self, conexion):
        
        try:
            conexion.close()
            print("Conexion cerrada")
            
        except sqlite3.Error as e:
            print(f"Error al cerrar la conexion: {e}")