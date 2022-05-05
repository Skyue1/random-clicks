from pyautogui import click
from random import randint
from time import sleep

while True:
    numb = randint(1,100)

    if numb == 100:
        print("click")
        click()

    else:
        sleep(0.05)
        print(numb)
        continue    