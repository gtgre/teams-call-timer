import time
import pynput
from pynput.keyboard import Key, Controller
import guizero
from guizero import App, Text, TextBox, PushButton, Box

keyboard = Controller()

def esc():
    t = int(delay.value)*60
    time.sleep(t)
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press("b")
    keyboard.release(Key.ctrl)
    keyboard.release(Key.shift)
    keyboard.release("b")
    app.warn(title="belina", text="sei stato dissconnesso")


app = App(title="auto call-ender", width=177, height=103, layout="grid")
box = Box(app, layout="grid", grid=[0,3], align="bottom", border=1)
title = Text(box, text="auto call-ender", size=20, font="Times New Roman", color="red", grid=[0,2])
delay = TextBox(box,grid=[0,1])
remove = PushButton(box, command=esc, text="launch", grid=[0,0])

app.display()
