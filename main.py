# I - Import and Initialize
import pygame as pg
from createRay import *

pg.init()

# D - Display configuration
def draw_circles(background,coordinates):
    for i in range(len(coordinates)):
        pg.draw.circle(background,(0,0,0),coordinates[i],5)

# A - Action (broken into ALTER steps)
def main(height_object=80,distance_object=120,focal_length1=50,focal_length2=40,distance_ocular=150,distance_objective=450):
    # A - Assign values to key variables
    screen = pg.display.set_mode((1000,900), pg.RESIZABLE)
    pg.display.set_caption("Refracting Telescope")
    pg.font.init()
    font = pg.font.Font('freesansbold.ttf',15)
    object_ = pg.image.load("tree.png")
    object_ = pg.transform.scale(object_, [height_object,height_object])
    object_ = object_.convert()  
    distance_ocular+=450

    rays = []
    center_curvature1 = [distance_objective+12, 450]
    center_curvature2 = [distance_ocular+12, 450]
    focal_objective1 = [distance_objective-focal_length1,450]
    focal_objective2 = [distance_objective+25+focal_length1,450] 
    focal_ocular1 = [distance_ocular-focal_length2,450] 
    focal_ocular2 = [distance_ocular+25+focal_length2,450] 
    real_image_drawn = False    

    distance_image1 = (1/focal_length1 - 1/distance_object)**-1 
    height_image1 = (distance_image1*height_object/distance_object)
    
    distance_image2 = (1/focal_length2 - 1/(distance_ocular-distance_image1-450))**-1
    height_image2 = (distance_image2*height_image1/(distance_ocular-distance_image1-450))

    magnefication1 = -distance_image1/distance_object
    magnefication2 = -height_image2/height_image1
    magnefication3 = -distance_image2/distance_object
# E - Entities
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((210 , 180 , 140))   
    clock = pg.time.Clock()

    pg.draw.line(background,(0,0,0),[100,450],[900, 450],3)# Boundary/Plane

    objective = pg.draw.ellipse(background,(135, 206, 235),[distance_objective,450-int(350*.5),25,350],0)
    ocular = pg.draw.ellipse(background,(135, 206, 235),[distance_ocular,450-int(250*.5),25,250],0)
    draw_circles(background,[center_curvature1,center_curvature2,focal_objective1,focal_objective2,focal_ocular1,focal_ocular2])

    slope_ray1 = [((focal_objective2[0])-(center_curvature1[0]))/60, ((focal_objective2[1])-(450-height_object))/60]
    x_ray1 = center_curvature2[0]
    y_ray1 = 450-height_object+(slope_ray1[1]*((center_curvature2[0]-center_curvature1[0])/slope_ray1[0]))

    slope_ray3 = [((center_curvature1[0])-(450-distance_object-round(height_object/4)))/60, ((center_curvature1[1])-(450-height_object))/60]
    x_ray3 = 450-distance_object-round(height_object/4)
    y_ray3 = 450-height_object
    while x_ray3 <= center_curvature2[0]:
        x_ray3 += slope_ray3[0]
        y_ray3 += slope_ray3[1]

    rays.append( Rays( [450-distance_object-round(height_object/4),450-height_object] , [center_curvature1[0],450-height_object] , [x_ray1,y_ray1] , focal_ocular2 ) )
    rays.append( Rays( [450-distance_object-round(height_object/4),450-height_object] , [center_curvature1[0],450+height_image1] , [center_curvature2[0],450+height_image1] ,focal_ocular2) )
    rays.append( Rays( [450-distance_object-round(height_object/4),450-height_object] , [x_ray3,y_ray3],focal_ocular2))
    # L - Loop
    while True:
        # T - Timer to set frame rate
        clock.tick(60)     

        for ray in rays: ray.run(background)
        y1 = rays[0].y
        y2 = rays[1].y
        y3 = rays[2].y
        x1 = rays[0].x
        x2 = rays[1].x
        x3 = rays[2].x 

        """if y1 >= 450 and y2 >= 450 and y3 >= 450:
            if x1 >= center_curvature2[0] and x2 >= center_curvature2[0] and x3 >= center_curvature2[0] and real_image_drawn: break"""

        # E - Event handling
        for event in pg.event.get():
            if event.type == pg.QUIT:   break
        # R - Refresh display
        screen.blit(background, (0,0))
        screen.blit(object_, (450-distance_object-round(height_object/2), 450-height_object))

        if real_image_drawn == False and x1 >= center_curvature2[0] and x2 >= center_curvature2[0] and x3 >= center_curvature2[0]:
            virtual_image = pg.image.load("tree.png")
            virtual_image = pg.transform.rotate(virtual_image, 180)
            virtual_image = pg.transform.scale(virtual_image, [round(height_image2),round(height_image2)])
            virtual_image.convert()
            real_image_drawn = True
            real_image = pg.image.load("tree.png")
            real_image = pg.transform.rotate(real_image, 180)
            real_image = pg.transform.scale(real_image, [round(height_image1),round(height_image1)])
            real_image.convert()
            intersection = 'The size of the real image is {:.2f}cm and is {:.2f}cm away from the ocular lens.'.format(height_image1,distance_ocular-distance_image1-450)
            magnefication1 = 'The magnefication of the real image is {:.2f}.'.format(magnefication1)
            intersection1 = 'The size of the virtual image is {:.2f}cm and is {:.2f}cm away from the ocular lens.'.format(height_image2,distance_image2)
            magnefication2 = "The magnefication of the virtual image is {:.2f}.".format(magnefication2)
            magnefication3 = "The magnefication of the virtual image to the real image is {:.2f}.".format(magnefication3)
            magnefication3 = font.render(magnefication3, True, [0,0,0])
            intersection = font.render(intersection, True, [0,0,0])
            magnefication1 = font.render(magnefication1, True, [0,0,0])
            intersection1 = font.render(intersection1, True, [0,0,0])
            magnefication2 = font.render(magnefication2, True, [0,0,0])
        elif real_image_drawn: 
            pg.draw.line(background,(255,255,0),[round(distance_ocular-distance_image2)+height_image2/8,450+height_image2] , [x_ray1,y_ray1],3)
            pg.draw.line(background,(255,255,0),[round(distance_ocular-distance_image2)+height_image2/8,450+height_image2] , [x_ray3,y_ray3],3)
            pg.draw.line(background,(255,255,0),[round(distance_ocular-distance_image2)+height_image2/8,450+height_image2] , [center_curvature2[0],450+height_image1],3)
            screen.blit(real_image,[round(450+distance_image1+height_image1/8),round(450)])
            screen.blit(virtual_image,[round(distance_ocular-distance_image2-height_image2/8),450])
            screen.blit(intersection,[100,100])
            screen.blit(magnefication1,[100,130])
            screen.blit(intersection1,[100,160])
            screen.blit(magnefication2,[100,190])
            screen.blit(magnefication3,[100,220])

        pg.display.flip()
# Close the game window
pg.quit()
main()
