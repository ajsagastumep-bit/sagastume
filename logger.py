 from datetime import datetime

def log(mensaje, nivel="INFO"):
    try:
        with open("log.txt", "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] {nivel}: {mensaje}\n")

    except Exception as e:
        print("Error al escribir log:", e)


def log_error(mensaje):
    log(mensaje, nivel="ERROR")


def leer_logs(filtro=None):
    try:
        with open("log.txt", "r") as f:
            for linea in f:
                if filtro is None or filtro in linea:
                    print(linea.strip())

    except FileNotFoundError:
        print("No hay logs aún.")

import logger

logger.log("Programa iniciado")
logger.log("Todo funcionando bien")

logger.log_error("Este es un error de prueba")

print("\n--- TODOS LOS LOGS ---")
logger.leer_logs()

print("\n--- SOLO ERRORES ---")
logger.leer_logs("ERROR")
