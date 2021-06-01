import pyautogui as gui
#Te pregunta que tan grande es tu cliente 7u7
gui.FAILSAFE = False
print("-----------------------------------------------------------------------------------------------------------------------")
print("Bienvenido al aceptador de partidas de lol")
print("-----------------------------------------------------------------------------------------------------------------------")
print("Para poder usar el programa primero tendras que decirle que tan grande es tu cliente de LoL")
print("Recuerda que para fijarte que tan grande es tu cliente, debes ir a la ruedita y fijarte el tamaño de ventana")
print("Las proporciones que entiende este programa son Chico(1024x576), Mediano(1280x720) o Grande(1600x900)")
print("Asi que dime, que tan grande es tu cliente?1:Chico, 2:Mediano, 3:Grande")
print("-----------------------------------------------------------------------------------------------------------------------")
ans = None
while not (ans == str(1) or ans == str(2) or ans == str(3)):
    ans = input("Escriba una de las opciones(1,2,3):")
#Una vez que define que tan grande es el cliente puede definir que "aceptar" va a usar
aceptar = None
while True:
    print("Esperando partida..")
    while aceptar == None:
        aceptar = gui.locateCenterOnScreen("boton" + str(ans) + ".png")
    print("Se encontro partida")
    gui.click(aceptar)
    aceptar = None
