import pygame as pg
import math

class Rays:
    def __init__(self):
        pass

def main():
    screen = pg.display.set_mode((640,480))
    pg.display.set_caption("Refracting Telescope")

    clock = pg.time.Clock()
    
    while True:
        clock.tick(60)
        background = pg.Surface(screen.get_size())
        background = background.convert()
        background.fill((136, 204, 226))

        for event in pg.event.get():
            if event.type == pg.QUIT:   break

        pg.draw.line(background,(0,0,0),[100,240],[540, 240],3)    
        pg.draw.arc(background,(255,0,0),[540,150,50,200],     .05,   -.05, 2)    
        screen.blit(background, (0,0))
        pg.display.flip()

main()
pg.quit()

