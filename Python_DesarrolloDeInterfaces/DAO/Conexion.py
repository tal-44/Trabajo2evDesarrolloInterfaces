import sqlite3

class Conexion:
    
    """
    Conexion con la base de datos de DB Browser SQLite
    """
    
    __db__path = "BBDDTrabajadoresYReloj.db"
    
    def get_connection(self):
        """
        Devuelve una conexion con la base de datos
        """
        try:
            self.conexion = sqlite3.connect(Conexion.__db__path)
            print("Conexion establecida")
            return self.conexion
        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None