import random as rnd
import pyautogui as pg
import time

time.sleep(5)
vid_X = rnd.randrange(200, 950)
vid_Y = rnd.randrange(120, 400)

vids=1

while vids < 30:
    vids=vids+1
    time.sleep(0.5)
    pg.doubleClick(vid_X,vid_Y)
    vid_X = rnd.randrange(200, 950)
    vid_Y = rnd.randrange(120, 400)
    pg.typewrite(["left"])