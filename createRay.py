import pygame as pg

class Rays:
    
    def __init__(self,location,destination,destination1=None,destination2=None,destination3=None,destination4=None):
        self.location = location
        self.destination = destination
        self.destination1 = destination1
        self.destination2 = destination2
        self.destination3 = destination3
        self.destination4 = destination4
        self.movement = [(destination[0]-location[0])/60,(destination[1]-location[1])/60]
        self.x = location[0]
        self.y = location[1]

    def change_course(self,background):
        self.location = self.destination
        self.destination = self.destination1
        self.destination1 = self.destination2
        self.destination2 = self.destination3
        self.destination3 = self.destination4
        self.destination4 = None
        if self.destination == None: return
        self.movement = [(self.destination[0]-self.location[0])/60,(self.destination[1]-self.location[1])/60]
        self.x = self.location[0]
        self.y = self.location[1]

    def run(self,background):
        pg.draw.line(background,(255,255,0),[self.location[0],self.location[1]],[self.x,self.y],3)
        if self.x < self.destination[0]-self.movement[0]: 
            self.x += self.movement[0]
            self.y += self.movement[1]
        else:   
            if self.destination1 != None:   self.change_course(background)