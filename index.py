import pygame as pg
import math

class Rays:
    def __init__(self,destination=[]):
        self.destination = destination

    def run():
        pass
    
    def change_course():
        pass

def main():
    screen = pg.display.set_mode((1000,900))
    pg.display.set_caption("Refracting Telescope")

    height_object = 10
    distance_object = 5
    clock = pg.time.Clock()
    background = pg.image.load("epic.jpg")
    tree = pg.image.load("tree.jpg")
    tree = tree.convert()

    rays1 = Rays([33])

    
    while True:
        clock.tick(60)
        """"background = pg.Surface(screen.get_size())
        background = background.convert()
        background.fill((136, 204, 226))"""
        pg.transform.smoothscale(background, (1000,900))

        for event in pg.event.get():
            if event.type == pg.QUIT:   break

        pg.draw.line(background,(0,0,0),[100,165],[360, 165],3)
        pg.draw.line(background,(0,0,0),[360,165],[440, 270],3)
        pg.draw.line(background,(0,0,0),[100,240],[540, 240],3)
        pg.draw.ellipse(background,(255, 255, 255),[350,90+70,25,150],0)
        pg.draw.ellipse(background,(255, 255, 255),[450,140+50,25,100],0)
        
        
        screen.blit(background, (0,0))
        screen.blit(tree, (100, 100))

        pg.display.flip()



main()
pg.quit()
