import logging

# Configuración del log
logging.basicConfig(
    filename='sistema.log',      # Nombre del archivo
    filemode='a',                # 'a' para añadir (append), 'w' para sobreescribir
    level=logging.INFO,          # Nivel mínimo que se registrará
    format='%(asctime)s - %(levelname)s - %(message)s', # Formato del mensaje
    datefmt='%Y-%m-%d %H:%M:%S'
)

def realizar_operacion(x, y):
    logging.info(f"Iniciando operación con valores: {x} y {y}")
    try:
        resultado = x / y
        logging.info("Operación exitosa")
        return resultado
    except ZeroDivisionError:
        # logging.exception registra el error con el rastreo (stack trace) completo
        logging.exception("Se intentó dividir por cero")
    except Exception as e:
        logging.error(f"Error inesperado: {e}")

# Pruebas
realizar_operacion(10, 2)
realizar_operacion(10, 0)
