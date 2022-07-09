import pyautogui as pg
from time import sleep

n = input("Name: ")
input("Press ENTER to start")
sleep(3)
txt = open('animals.txt')
no = 0
a = n + " is "
for i in txt:
    no = no + 1
    print("printed: " + a + i + no)
    pg.write(a + i)
    pg.press("Enter")
    sleep(0.8)

input("Press ENTER to exit")
