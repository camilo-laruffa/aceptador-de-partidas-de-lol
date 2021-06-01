import pyautogui as gui
#Te pregunta que tan grande es tu cliente 7u7
gui.FAILSAFE = False
print("Que tan grande es tu cliente?1:Chico, 2:Mediano, 3:Grande")
ans = None
while not (ans == str(1) or ans == str(2) or ans == str(3)):
    ans = input("Escriba una de las opciones(1,2,3):")
#Una vez que define que tan grande es el cliente puede definir que "aceptar" va a usar
aceptar = None
while True:
    while aceptar == None:
        aceptar = gui.locateCenterOnScreen("boton" + str(ans) + ".png")
        if aceptar == None:
            print("Esperando partida..")
        else:
            print("Se encontro partida")
    gui.click(aceptar)
    aceptar = None
