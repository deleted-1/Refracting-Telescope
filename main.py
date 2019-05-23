import pygame as pg
import math
from createRay import Rays

pg.font.init()

def draw_circles(background,coordinates):
    for i in range(len(coordinates)):
        pg.draw.circle(background,(0,0,0),coordinates[i],5) 

def main(height_object=70,distance_object=140,focal_length1=50,focal_length2=20,distance_ocular=100,image=None,distance_objective=450):
    screen = pg.display.set_mode((1000,900), pg.RESIZABLE)
    if image == None: image = "tree"
    pg.display.set_caption("Refracting Telescope")
    height_objective=300
    height_ocular=150
    distance_ocular+=450
    clock = pg.time.Clock()
    object_ = pg.image.load(image+".png")
    object_ = pg.transform.scale(object_, [height_object,height_object])
    object_ = object_.convert()  
    
    
    center_curvature1 = [distance_objective+12, 450]
    center_curvature2 = [distance_ocular+12, 450]
    focal_objective1 = [distance_objective-focal_length1,450]
    focal_objective2 = [distance_objective+25+focal_length1,450] 
    focal_ocular1 = [distance_ocular-focal_length2,450] 
    focal_ocular2 = [distance_ocular+25+focal_length2,450]  

    final_destination = [focal_ocular2[0],focal_ocular2[1]]

    slope = [(focal_objective2[0]-center_curvature1[0])/60,(450-450-height_object)/60]
    slope1 = [(center_curvature1[0]-distance_object-int(height_object/2))/60 , (450-450-height_object)/60]
    slope2 = [(center_curvature1[0]-distance_object+int(height_object/2))/60,(center_curvature1[1]-(450-height_object))/60]

    

    x = focal_objective2[0]
    y = 450
    x1 = focal_objective1[0]
    y1 = 450
    x2 = center_curvature1[0]
    y2 = 450

    while x < center_curvature2[0]-slope[0] :
        if  x < center_curvature2[0]-slope[0]:
            x += slope[0]
            y -= slope[1]


    while x1 < center_curvature1[0]-slope1[0]:
        x1 += slope1[0]
        y1 -= slope1[1]

    while x2 < center_curvature2[0]-slope2[0]:
        x2 += slope2[0]
        y2 += slope2[1]

    second_x = x
    second_x2 = x2
    second_y = y
    second_y2 = y2

    while second_y <= second_y2 and second_x <= second_x2:
        second_x -= slope[0]
        second_y -= slope[1]
        second_y2 -= slope2[1]
        second_x2 -= slope2[0]

    ray1 = Rays( [distance_object+int(height_object/2),450-height_object] , [center_curvature1[0],450-height_object] , [x,y] , final_destination)
    ray2 = Rays ([distance_object+int(height_object/2),450-height_object],[x1,y1],[center_curvature2[0],y1],final_destination)
    ray3 = Rays ([distance_object+int(height_object/2),450-height_object],[x2,y2],final_destination)

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((210 , 180 , 140))   
    
    #BigSystemFont = pg.font.SysFont("Arial", 30)
    #SmallSystemFont = pg.font.SysFont("Arial", 15)
    #label1 = BigSystemFont.render("F", 1, (255, 255, 0))
    #label2 = SmallSystemFont.render("O", 1, (255, 255, 0))
    pg.draw.line(background,(0,0,0),[100,450],[900, 450],3)# Boundary/Plane
    is_real_image = False

    objective = pg.draw.ellipse(background,(135, 206, 235),[distance_objective,450-int(height_objective*.5),25,height_objective],0)
    ocular = pg.draw.ellipse(background,(135, 206, 235),[distance_ocular,450-int(height_ocular*.5),25,height_ocular],0)
    draw_circles(background,[center_curvature1,center_curvature2,focal_objective1,focal_objective2,focal_ocular1,focal_ocular2])

    while True:
        clock.tick(60)     

        for event in pg.event.get():
            if event.type == pg.QUIT:   break

        ray1.run(background)
        ray2.run(background)
        ray3.run(background)
        

        if ray1.x >= float(final_destination[0])-slope[0] and ray2.x >= float(final_destination[0])-slope1[0] and ray3.x >= float(final_destination[0])-slope2[0]: break

        screen.blit(background, (0,0))
        screen.blit(object_, (450-distance_object, 450-height_object))
        if ray1.y <= ray2.y and is_real_image == False and ray1.y>450 and ray1.x <= ray2.x: 
            intersection = [int(ray1.x),int(ray2.y)]
            virutal_image = pg.image.load(image+".png")
            virutal_image = pg.transform.rotate(virutal_image,180)
            virutal_image = pg.transform.scale(virutal_image, [intersection[1]-450,intersection[1]-450])
            intersection_sentence = 'The real image is at a height of {}cm and {}cm away from the ocular lens.'.format(intersection[1]-450,distance_ocular-intersection[0])
            print(intersection_sentence)
            virutal_image.convert()
            screen.blit(virutal_image, [intersection[0]+height_object,intersection[1]-height_object])
            is_real_image = True
        elif is_real_image:  screen.blit(virutal_image, [intersection[0]+(intersection[1]-450)/2,intersection[1]-(intersection[1]-450)])
        #screen.blit(label1, (350, 460))
        #screen.blit(label2, (360, 475))
        pg.display.flip()

pg.quit()