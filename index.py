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
        background.fill((38,1,1))

        for event in pg.event.get():
            if event.type == pg.QUIT:   break
        
        screen.blit(background, (0,0))
        pg.display.flip()

main()
pg.quit()

print("HELLO WORLD!")