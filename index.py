import pygame as pg
import math

"""
I am too tired to explain
what this class does
but read through it and try to revert
it back to how it originally was if
you mess around with it


But to make it short all it does is draw that second
line you see when you run the program
"""
class Rays:
    rays = []
    
    def __init__(self,location,destination):
        self.location = location
        self.destination = destination
        self.movement = [(destination[0]-location[0])/60,(destination[1]-location[1])/60]
        self.x = location[0]
        self.y = location[1]

    def change_course(self,background,focal_point):
        Rays.rays.append(Rays(self.destination,focal_point))
        for ray in Rays.rays:
            ray.run(background,focal_point)
    
    def run(self,background,focal_point):
        pg.draw.line(background,(0,0,0),self.location,[self.x,self.y],3)
        if self.x < self.destination[0]: 
            self.x += self.movement[0]
            self.y += self.movement[1]
        else:   self.change_course(background,focal_point)
        
    def run2(self,background,focal_point):
        pg.draw.line(background,(0,0,0),self.location,[self.x,self.y],3)
        if self.x < self.destination[0]:
            self.x += self.movement[0]
            self.y -= self.movement[1]
        else:   self.change_course(background,focal_point)
    

def main():
    screen = pg.display.set_mode((1000,900), pg.RESIZABLE)

    pg.display.set_caption("Refracting Telescope")

    height_object = 70
    distance_object = 140
    center = [510, 450]
    clock = pg.time.Clock()
    tree = pg.image.load("tree.png")
    tree = pg.transform.scale(tree, [height_object,height_object])
    tree = tree.convert()

    ray1 = Rays([distance_object+height_object/2,450-height_object],[500,450-height_object])
    ray2 = Rays([0, 350],[500,232])
    
    
    
    while True:
        clock.tick(60)
        background = pg.Surface(screen.get_size())
        background = background.convert()
        background.fill((136, 204, 226))        

        for event in pg.event.get():
            if event.type == pg.QUIT:   break

        pg.draw.line(background,(0,0,0),[100,450],[900, 450],3) # Boundary/Plane

        focal_objective1 = [500-75,450]
        focal_objective2 = [500+100,450]
        focal_ocular1 = [700-50,450] 
        focal_ocular2 = [700+75,450]

        pg.draw.circle(background,(0,0,0),focal_objective1,5)
        pg.draw.circle(background,(0,0,0),focal_objective2,5)
        pg.draw.circle(background,(0,0,0),focal_ocular1,5)
        pg.draw.circle(background,(0,0,0),focal_ocular2,5)

        objective_distance = []
        objective_height = []
        ocular_distance = []
        ocular_height = []

        objective = pg.draw.ellipse(background,(255,255,0),[500,300+75,25,150],0)
        ocular = pg.draw.ellipse(background,(255,255,0),[700,350+50,25,100],0)
        pg.draw.circle(background,(0,0,0),center,5)

        ray1.run1(background,focal_objective2)
        ray2.run2(background,focal_objective2)

        screen.blit(background, (0,0))
        screen.blit(tree, (distance_object, 450-height_object))
        pg.display.flip()

main()

pg.quit()
