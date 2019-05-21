from tkinter import *
from main import *

def set_parameters():

    def show_diagram():
        try:
            main(int(focal1.get()), int(focal2.get()), int(object_distance.get()), int(object_height.get()))
        except ZeroDivisionError:
            set_parameters()
    
    root = Tk()
    root.title("Telescope Simulation")
    root.geometry("640x640+0+0")

    Label(root, text="Enter the focal length of the objective lens(cm)", font=("time new roman",15)).grid(row=0,coloumn=0)
    Label(root, text="Enter the focal length of the ocular lens(cm)", font=("time new roman",15)).grid(row=2,coloumn=0)
    Label(root, text="Enter the distance of the object(cm)", font=("time new roman",15)).grid(row=4,coloumn=0)
    Label(root, text="Enter the height of the object(cm)", font=("time new roman",15)).grid(row=6,coloumn=0)

    focal1 = Entry(root)
    focal2 = Entry(root)
    object_distance = Entry(root)
    object_height = Entry(root)

    focal1.grid(row=0, column=1)
    focal2.grid(row=1, column=1)
    object_distance.grid(row=2, column=1)
    object_height.grid(row=3, column=1)
 
    Button(root, text='Quit', command=root.quit).grid(row=4, column=0, sticky=W, pady=4)
    Button(root, text='Enter', command=show_diagram).grid(row=4, column=1, sticky=W, pady=4)

    mainloop()

set_parameters()