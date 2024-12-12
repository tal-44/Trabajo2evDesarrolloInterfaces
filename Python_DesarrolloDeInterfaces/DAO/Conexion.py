class Conexion:
    
    """
    Conexion con la base de datos de DB Browser SQLite
    """
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        
    def conectar(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()