import pywhatkit

try:
    pywhatkit.sendwhatmsg_instantly("+524443483559", "Hola, este es un mensaje de prueba")
    print("Mensaje enviado exitosamente")
except Exception as e:
    print(f"Se produjo un error: {e}")