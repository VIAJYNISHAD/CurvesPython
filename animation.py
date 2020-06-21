from PIL import ImageGrab, ImageOps 
import pyautogui 
import time 
import numpy as np   

Uppercorner =(6,152)
Lowercorner =(506,652)
m=50
def origin(a,b,c,d):   
    neworigin=(Uppercorner[0],Lowercorner[1])
    return neworigin

def convert(x,y):
    Point=(Uppercorner[0]+x+50,Lowercorner[1]-y-50)
    return Point
def color(i):
    pyautogui.click(320,115)
    pyautogui.click(320,115)
    time.sleep(0.1)
    pyautogui.click(400+25*i,160)
def axis():   
    pyautogui.mouseDown(6+50,652-50)
    pyautogui.mouseUp(6+50,152)

    pyautogui.mouseDown(6+50,652-50)
    pyautogui.mouseUp(6+500,652-50)
    time.sleep(0.5)
def cordinate(n):
    for i in range(1,n):
        pyautogui.mouseDown(6+50+(25*i),652-35-5)
        pyautogui.mouseUp(6+50+(25*i),652-65+5)
        time.sleep(0.01)
        pyautogui.mouseDown(6+35+5,625-50-(25*i))
        pyautogui.mouseUp(6+65-5,625-50-(25*i))


def parabola():
    x=0.1
    for i in range(m):
        y=x*2+2
        print(x)
        print(y)
        x=x+0.1
        a=int(x/0.01)
        b=int(y/0.01)
        if a<450 and b<450:
            pyautogui.mouseUp(convert(a,b))
            pyautogui.mouseDown(convert(a,b))
    pyautogui.mouseUp()

def easyerase(q):
    pyautogui.keyDown('ctrl')
    pyautogui.click(x=100, y=500)
    for i in range(q):
        pyautogui.press('z') 
    pyautogui.keyUp('ctrl')


color(3)
#axis()
#cordinate(18)
parabola()
#easyerase()

