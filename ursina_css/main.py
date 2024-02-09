from ursina import *
from controller import * # ursina's PlatformerController

app = Ursina()

entities=[]
for i in range(-5,6):
    entities.append(Entity(model="quad",texture="sky",scale=(0.15,0.15),position=(i/(6+2/3),0.375)))
for i in range(-5,6):
    entities.append(Entity(model="quad",texture="sky",scale=(0.15,0.15),position=(i/(6+2/3),0.225)))
for i in range(-5,6):
    entities.append(Entity(model="quad",texture="sky",scale=(0.15,0.15),position=(i/(6+2/3),0.075)))
for i in range(-5,6):
    entities.append(Entity(model="quad",texture="sky",scale=(0.15,0.15),position=(i/(6+2/3),-0.075)))
for i in range(-5, 6):
    entities.append(Entity(model="quad", texture="grass", scale=(0.15, 0.15), position=(i/(6+2/3),-0.225)))
for i in range(-5, 6):
    entities.append(Entity(model="quad", texture="dirt", scale=(0.15, 0.15), position=(i/(6+2/3),-0.375)))
for i in range(-5, 6):
    entities.append(Entity(model="quad", texture="stone", scale=(0.15, 0.15), position=(i/(6+2 / 3),-0.525)))

player=Entity(model="quad",texture="steve",scale=(0.15,0.3))


def right():
    player.x+=0.15
def left():
    player.x-=0.15

def break_():
    for entity in entities:
        if round((player.y - 0.225)*(6+1/6))==round(entity.y*(6+1/6)) and round(entity.x * (6 + 1 / 6))==round(player.x * (6 + 1 / 6)):
            entity.texture = "sky"

def place():
    for entity in entities:
        if round((player.y + 0.225)*(6+1/6)) == round(entity.y*(6+1/6)) and round(entity.x * (6 + 1 / 6)) == round(player.x * (6 + 1 / 6)):
            entity.texture = "dirt"

def down():
    player.y -= 0.15 / 20

def up():
    player.y += 0.15 / 20

Button(text="Up",scale=0.15,x=0.8125,y=0.45,on_click=up)
Button(text="Right",scale=0.15,x=0.8125,y=-0.225,on_click=right)
Button(text="Left",scale=0.15,x=-0.8125,y=-0.225,on_click=left)
Button(text="Break",scale=0.15,x=-0.8125,y=0,on_click=break_)
Button(text="Place",scale=0.15,x=0.8125,y=0,on_click=place)
Button(text="Down",scale=0.15,x=-0.8125,y=0.45,on_click=down)

def update():
    if held_keys["d"]:
        player.x+=0.15/20
    if held_keys["a"]:
        player.x-=0.15/20
    if held_keys["shift"]:
        break_()
    if held_keys["space"]:
        place()
def input(key):
    if key=="w" or key=="w hold":
        player.y+=0.15/20
    if key=="s" or key=="s hold":
        player.y-=0.15/20
app.run()