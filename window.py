from tkinter import *
from main import main

def set_parameters():

    root = Tk()
    root.title("Telescope Simulation")
    root.geometry("500x320+0+0")

    Label(root, text="Enter the height of the object(cm)", font=("time new roman",10)).place(x=20,y=20)
    Label(root, text="Enter the object distance from the objective lens(cm)", font=("time new roman",10)).place(x=20,y=70)
    Label(root, text="Enter the focal point of the objective lens(cm)", font=("time new roman",10)).place(x=20,y=120)
    Label(root, text="Enter the focal point of the ocular lens(cm)", font=("time new roman",10)).place(x=20,y=170)
    Label(root, text="Enter the distance between the two lens(cm)",font=("time new roman",10)).place(x=20,y=220)

    height_object=Entry(root)
    distance_object=Entry(root)
    focal_objective=Entry(root)
    focal_ocular=Entry(root)
    len_distance=Entry(root) 

    def show_diagram():
        try:    
            if int(distance_object.get()) <= int(focal_objective.get())*2:    Label(root, text="Has to be twice focal objective!", font=("time new roman",10), fg='red').place(x=300,y=45)
            elif float((1/float(focal_objective.get())- 1/float(distance_object.get()))**-1)  < float(focal_ocular.get()):   Label(root, text="Please specify other inputs because the real image is beyond the focal of the ocular!", font=("time new roman",10), fg='red').place(x=50,y=145)
            elif int(distance_object.get()) > 200:  Label(root,text="Please choose an integer smaller or equal to 200 for object distance.", font=("time new roman",10), fg='red').place(x=350,y=45)
            elif int(len_distance.get())-int(focal_ocular.get()) <= int(focal_objective.get()) | int(focal_ocular.get()) <= 0: Label(root, text="Please enter a larger focal ocular.", font=("time new roman",10), fg='red').place(x=325,y=95) 
            else:   main(int(height_object.get()),int(distance_object.get()),int(focal_objective.get()),int(focal_ocular.get()),int(len_distance.get()))
        except ValueError:  Label(root, text="*Please use integer values.", font=("time new roman",10), fg='red').place(x=20,y=245)        
    
    height_object.place(x=225,y=20)
    distance_object.place(x=340, y=70)
    focal_objective.place(x=300,y=120)
    focal_ocular.place(x=275,y=170)
    len_distance.place(x=295,y=220)
 
    Button(root, text='Quit', width = 5,command=root.quit).place(x=20,y=270)
    Button(root, text='Submit',width=5, command=show_diagram).place(x=100,y=270)

    mainloop()

set_parameters()
