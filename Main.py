import pygame as pyg
import random
from effector import Effector

pyg.init()


clock = pyg.time.Clock()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 1080

effectors = []
screen = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def update_forces():
    for eff in effectors:
        eff.add_forces(effectors)

run = True
while run:
    clock.tick(60)
    screen.fill((0,0,0))
    update_forces()
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False
        elif event.type == pyg.MOUSEBUTTONDOWN:
            copy = False
            for eff in effectors:
                if (pyg.math.Vector2(pyg.mouse.get_pos()).distance_to(eff.coords) < eff.radius):
                    eff.grow(20)
                    copy = True
            if not copy:
                effectors.append(Effector(screen, pyg.math.Vector2(pyg.mouse.get_pos())))
                print("new effector!, new length: " + str(len(effectors)))
                new = effectors[len(effectors)-1]
    for eff in effectors:
        eff.move(clock.get_rawtime())
        pyg.draw.circle(screen, eff.color, eff.coords, eff.radius)
       # eff.show_all_forces(screen)
    pyg.display.update()


pyg.quit()


