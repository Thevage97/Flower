# Archivo: prueba.py

# Importamos la biblioteca de tiempo para obtener la fecha y hora actual
import datetime

# Definimos una función que devuelve un mensaje de bienvenida
def bienvenida():
    ahora = datetime.datetime.now()
    mensaje = f"Hola, mundo! La fecha y hora actual es {ahora.strftime('%Y-%m-%d %H:%M:%S')}"
    return mensaje

# Llamamos a la función y imprimimos el resultado
print(bienvenida())
