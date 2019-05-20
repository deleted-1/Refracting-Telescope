import pygame as pg
import tkinter
import math



"""class TK:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.label1 = tkinter.Label(self.main_window, text="Type 1 for the object to be past 2 times the focal point")
        self.label2 = tkinter.Label(self.main_window, text="Type 2 for the object to be at 2 times the focal point")
        self.label3 = tkinter.Label(self.main_window, text="Type 3 for the object to be between 2 times the focal point and the focal point")
        self.label4 = tkinter.Label(self.main_window, text="Type 4 for the object to be at the focal point")
        self.entry1 = tkinter.Entry(self.main_window, text="Where would you like the image to be placed? ")

        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()
        self.entry1.pack()

        tkinter.mainloop()
        self.entry1.position()
    def position(self):
        if self.entry1 == 1:
            pass
my_gui = TK()"""


class Rays:
    
    def __init__(self,location,destination,destination1=None,destination2=None,destination3=None):
        self.location = location
        self.destination = destination
        self.destination1 = destination1
        self.destination2 = destination2
        self.destination3 = destination3
        self.movement = [(destination[0]-location[0])/60,(destination[1]-location[1])/60]
        self.x = location[0]
        self.y = location[1]

    def change_course(self,background):
        self.location = self.destination
        self.destination = self.destination1
        self.destination1 = self.destination2
        self.destination2 = self.destination3
        self.destination3 = None
        if self.destination == None: return
        self.movement = [(self.destination[0]-self.location[0])/60,(self.destination[1]-self.location[1])/60]
        self.x = self.location[0]
        self.y = self.location[1]

    def run(self,background):
        pg.draw.line(background,(255,255,0),[self.location[0],self.location[1]],[self.x,self.y],3)
        if self.x <= self.destination[0]: 
            self.x += self.movement[0]
            self.y += self.movement[1]
        else:   
            if self.destination1 != None:   self.change_course(background)


def main():
    screen = pg.display.set_mode((1000,900), pg.RESIZABLE)

    pg.display.set_caption("Refracting Telescope")

    height_object = 70
    distance_object = 140
    clock = pg.time.Clock()
    tree = pg.image.load("tree.png")
    tree = pg.transform.scale(tree, [height_object,height_object])
    tree = tree.convert()  
    height_objective = 210
    height_ocular = 150 
    distance_objective  =400
    distance_ocular = 600
    center_curvature1 = [distance_objective+12, 450]
    center_curvature2 = [distance_ocular+12, 450]
    focal_objective1 = [distance_objective-int(height_objective/4),450]
    focal_objective2 = [distance_objective+int(height_objective/4 + 25),450] 
    focal_ocular1 = [distance_ocular-int(height_ocular/4),450] 
    focal_ocular2 = [distance_ocular+int(height_ocular/4+25),450]  

    destination1 = [focal_objective2[0],focal_objective2[1]] 
    destination2 = [focal_ocular2[0],focal_ocular2[1]]

    ray1 = Rays( [distance_object+int(height_object/2),450-height_object] , [center_curvature1[0],450-height_object] , destination1 , destination2)

    destination1 = [focal_objective1[0],focal_objective1[1],center_curvature1[0]]
    ray2 = Rays ([distance_object+int(height_object/2),450-height_object],destination1,[center_curvature2[0],destination1[1]], destination2)
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((210 , 180 , 140))   
    
    pg.draw.line(background,(0,0,0),[100,450],[900, 450],3)# Boundary/Plane
    
    while True:
        clock.tick(60)     

        for event in pg.event.get():
            if event.type == pg.QUIT:   break

         

        objective = pg.draw.ellipse(background,(135, 206, 235),[distance_objective,450-int(height_objective*.5),25,height_objective],0)
        ocular = pg.draw.ellipse(background,(135, 206, 235),[distance_ocular,450-int(height_ocular*.5),25,height_ocular],0)
        pg.draw.circle(background,(0,0,0),center_curvature1,5)
        pg.draw.circle(background,(0,0,0),center_curvature2,5)
        pg.draw.circle(background,(0,0,0),focal_objective1,5)
        pg.draw.circle(background,(0,0,0),focal_objective2,5)
        pg.draw.circle(background,(0,0,0),focal_ocular1,5)
        pg.draw.circle(background,(0,0,0),focal_ocular2,5)


        ray1.run(background)
        ray2.run(background)

        screen.blit(background, (0,0))
        screen.blit(tree, (distance_object, 450-height_object))
        pg.display.flip()


from tkinter import *

root = Tk()
root.title("Refracting Telescope")
root.geometry("640x640+0+0")

heading = Label(root, text="Refracting Telescope Simulating", font=("arial",40,"bold"), fg="steelblue").pack()

name = StringVar()
entry_box = Entry(root, textvariable=name,width=25,bg="lightgreen").place(x=300,y=200)

def Submit():
    print(str(name.get()))

work = Button(root, text="Work",width=30,height=5,bg="lightblue",command=Submit).place(x=250,y=300)

main()
root.mainloop()


pg.quit()
