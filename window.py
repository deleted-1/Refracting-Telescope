from tkinter import *
from main import main

def set_parameters():

    root = Tk()
    root.title("Telescope Simulation")
    root.geometry("640x640+0+0")

    Label(root, text="Enter the height of the object(cm)", font=("time new roman",10)).place(x=20,y=20)
    Label(root, text="Enter the object distance from the objective lens(cm)", font=("time new roman",10)).place(x=20,y=45)
    Label(root, text="Enter the height of the objective lens(cm)", font=("time new roman",10)).place(x=20,y=70)
    Label(root, text="Enter the height of the ocular lens(cm)", font=("time new roman",10)).place(x=20,y=95)
    Label(root, text="Enter the distance between the two lens(cm)",font=("time new roman",10)).place(x=20,y=120)
    Label(root, text="Enter the distance of the object from the beginning of the line(cm)",font=("time new roman",10)).place(x=20,y=145)

    height_object=Entry(root)
    distance_object=Entry(root)
    distance_objective=Entry(root)
    height_objective=Entry(root)
    height_ocular=Entry(root)
    len_distance=Entry(root)

    def show_diagram():
        try:
            height_object = int(height_object.get())
            distance_object = int(distance_object.get())
            height_objective = int(height_objective.get())
            height_ocular = int(height_ocular.get())
            distance_objective = distance_object
            distance_ocular = ''
            main()
        except ZeroDivisionError:
            set_parameters()
    
    

    height_object.place(x=225,y=20)
    distance_object.place(x=340, y=45)
    height_objective.place(x=275,y=70)
    height_ocular.place(x=250,y=95)
    len_distance.place(x=300,y=120)
    distance_objective.place(x=390,y=145)
 
    Button(root, text='Quit', width = 5,command=root.quit).place(x=20,y=170)
    Button(root, text='Submit',width=5, command=show_diagram).place(x=100,y=170)

    mainloop()

 

set_parameters()