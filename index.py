import pygame as pg
import math

class Rays:
    def __init__(self,location=[],destination=[]):
        self.location = location
        self.destination = destination

def main():
    screen = pg.display.set_mode((640,480))
    pg.display.set_caption("Refracting Telescope")

    height_object = 10
    distance_object = 5
    clock = pg.time.Clock()

    tree = pygame.image.load("download.jpg")
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
        
        #screen.blit(tree, (290, 190))
        screen.blit(background, (0,0))
        pg.display.flip()



main()
pg.quit()
