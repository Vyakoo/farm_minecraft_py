import pyautogui
import keyboard

from time import sleep

on = False


def main():
    while True:
        if keyboard.is_pressed("p"):
            IsOn()
        elif keyboard.is_pressed("o"):
            quit()
        elif on == True:
            sleep(1)
            click()



def click(): #Клик
     pyautogui.mouseDown()
     pyautogui.mouseUp()


def IsOn():
    global on 
    if on == False:
        on = True
    else:
        on = False



if __name__ == "__main__":
    main()