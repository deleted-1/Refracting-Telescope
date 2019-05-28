import pygame as pg
from createRay import *

pg.init()

def draw_circles(background,coordinates):
    for i in range(len(coordinates)):   pg.draw.circle(background,(0,0,0),coordinates[i],5)

def main(height_object=70,distance_object=120,focal_length1=50,focal_length2=40,distance_ocular=150,distance_objective=450):
    screen = pg.display.set_mode((1000,900), pg.RESIZABLE)
    pg.display.set_caption("Refracting Telescope")
    pg.font.init()
    font = pg.font.Font('freesansbold.ttf',15)
    object_ = pg.image.load("tree.png")
    object_ = pg.transform.scale(object_, [height_object,height_object])
    object_ = object_.convert()  
    distance_ocular+=450

    rays = []
    center_curvature1 = [ distance_objective+12 , 450 ]
    center_curvature2 = [ distance_ocular+12 , 450 ]
    focal_objective1 = [ distance_objective-focal_length1 , 450 ]
    focal_objective2 = [ distance_objective+25+focal_length1 , 450 ] 
    focal_ocular1 = [ distance_ocular-focal_length2 , 450] 
    focal_ocular2 = [ distance_ocular+25+focal_length2 , 450 ] 
    real_image_drawn = False
    virtual_image_drawn = False

    distance_image1 = (1/focal_length1 - 1/distance_object)**-1 
    height_image1 = (distance_image1*height_object/distance_object)
    
    distance_image2 = (1/focal_length2 - 1/(distance_ocular-distance_image1-450))**-1
    height_image2 = (distance_image2*height_image1/(distance_ocular-distance_image1-450))

    magnefication1 = -distance_image1/distance_object
    magnefication2 = -distance_image2/(distance_ocular-distance_image1-450)

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((210 , 180 , 140))   
    clock = pg.time.Clock()

    objective = pg.draw.ellipse(background,(135, 206, 235),[distance_objective,450-int(350*.5),25,350],0)
    ocular = pg.draw.ellipse(background,(135, 206, 235),[distance_ocular,450-int(250*.5),25,250],0)
    draw_circles(background,[center_curvature1,center_curvature2,focal_objective1,focal_objective2,focal_ocular1,focal_ocular2])    

    slope_ray1 = [((focal_objective2[0])-(center_curvature1[0]))/60, ((focal_objective2[1])-(450-height_object))/60]
    x_ray1 = center_curvature2[0]
    y_ray1 = 450-height_object+(slope_ray1[1]*((center_curvature1[0]-center_curvature2[0])/slope_ray1[0]))
    


    
main()
pg.quit()