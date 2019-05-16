import pygame as pg
import math

class Rays:
    def __init__(self,location=[],destination=[]):
        self.location = location
        self.destination = destination

def main(object_x, object_y):
    screen = pg.display.set_mode((640,480))
    pg.display.set_caption("Refracting Telescope")

    height_object = 10
    distance_object = 5
    clock = pg.time.Clock()

    tree = pg.image.load("tree.jpg")
    tree = tree.convert()

    
    while True:
        clock.tick(60)
        background = pg.Surface(screen.get_size())
        background = background.convert()
        background.fill((136, 204, 226))

        for event in pg.event.get():
            if event.type == pg.QUIT:   break

        pg.draw.line(background,(0,0,0),[100,165],[360, 165],3)
        pg.draw.line(background,(0,0,0),[360,165],[440, 270],3)
        pg.draw.line(background,(0,0,0),[100,240],[540, 240],3)
        pg.draw.ellipse(background,(255,255,0),[350,90+70,25,150],0)
        pg.draw.ellipse(background,(255,255,0),[450,140+50,25,100],0)
        
        screen.blit(background, (0,0))
        screen.blit(tree, (object_x, object_y))
        pg.display.flip()

print("Type 1 for the object to be past 2 times the focal point")
print("Type 2 for the object to be at 2 times the focal point")
print("Type 3 for the object to be between 2 times the focal point and the focal point")
print("Type 4 for the object to be at the focal point")


location = int(input("Where would you like the object to be located? "))

if location == 1:
    main(50, 100)
elif location == 2:
    main(100, 100)
elif location == 3:
    main(150, 100)

pg.quit()
