from tkinter import *
from main import *

def set_parameters():

    def show_diagram():
        try:
            distance_objective
            distance_ocular
            main(int(focal1.get()), int(focal2.get()), int(object_distance.get()), int(object_height.get()))
        except ZeroDivisionError:
            set_parameters()
    
    root = Tk()
    root.title("Telescope Simulation")
    root.geometry("640x640+0+0")

    Label(root, text="Enter the height of the object(cm)", font=("time new roman",10)).place(x=20,y=20)
    Label(root, text="Enter the object distance from the objective lens(cm)", font=("time new roman",10)).place(x=20,y=45)
    Label(root, text="Enter the height of the objective lens(cm)", font=("time new roman",10)).place(x=20,y=70)
    Label(root, text="Enter the height of the ocular lens(cm)", font=("time new roman",10)).place(x=20,y=95)
    Label(root, text="Enter the distance between the two lens(cm)",font=("time new roman",10)).place(x=20,y=120)

    height_object=Entry(root)
    distance_object=Entry(root)
    height_objective=Entry(root)
    height_ocular=Entry(root)
    

    height_object.place()
 
    Button(root, text='Quit', command=root.quit).grid(row=4, column=0, sticky=W, pady=4)
    Button(root, text='Enter', command=show_diagram).grid(row=4, column=500, sticky=W, pady=4)

    mainloop()

set_parameters()