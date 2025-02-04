import logging

class Log:
    
    @staticmethod
    def log_fichaje(codigo, estado, nombre):
        logging.info(f'Fichaje realizado: Codigo={codigo}, Nombre={nombre}, Estado={estado}')
                
    @staticmethod
    def log_fichaje_rechazado(codigo, nombre):
        logging.info(f'Fichaje rechazado: Codigo={codigo}, Nombre={nombre}')

    @staticmethod
    def log_error(error_message):
        logging.error(f'{error_message}')