import pywhatkit

try:
  #  pywhatkit.sendwhatmsg("+524442511343", "hola mundo", 18, 50)
  # pywhatkit.sendwhatmsg("+524442511343", "hola desde Python")
    pywhatkit.sendwhatmsg_to_group_instantly ("HMSd7sLfFPy4ivP0YtAqvE", "Holi", 10 ,True,3)
    print("Mensaje enviado")
except:
    print("Error")
    
    
    