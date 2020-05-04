import random as rnd
import pyautogui as pg
import time

time.sleep(5)

vFX = rnd.randrange(120, 570) #y
vTL = rnd.randrange(510,1890) #x

FX=1

while FX <= 15:
    FX=FX+1
    time.sleep(0.2)
    pg.moveTo (75,vFX)
    pg.dragTo(vTL,700,1)
    vFX = rnd.randrange(120, 570)
    vTL = rnd.randrange(510, 1890)