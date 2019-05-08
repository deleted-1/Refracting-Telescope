import pygame as pg
from math import *

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

        pg.draw.arc(background,(0,0,0),[200,150,350,300],  pi/2,     pi, 2)
        pg.draw.arc(background,(255,0,0),[100,100,200,200],     1,   -1, 2)     
        screen.blit(background, (0,0))
        pg.display.flip()

main()
pg.quit()