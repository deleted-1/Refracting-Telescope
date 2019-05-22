from tkinter import *
from main import main



def set_parameters():

    root = Tk()
    root.title("Telescope Simulation")
    root.geometry("500x225+0+0")

    Label(root, text="Enter the height of the object(cm)", font=("time new roman",10)).place(x=20,y=20)
    Label(root, text="Enter the object distance from the objective lens(cm)", font=("time new roman",10)).place(x=20,y=45)
    Label(root, text="Enter the focal point of the objective lens(cm)", font=("time new roman",10)).place(x=20,y=70)
    Label(root, text="Enter the focal point of the ocular lens(cm)", font=("time new roman",10)).place(x=20,y=95)
    Label(root, text="Enter the distance between the two lens(cm)",font=("time new roman",10)).place(x=20,y=120)

    height_object=Entry(root)
    distance_object=Entry(root)
    focal_objective=Entry(root)
    focal_ocular=Entry(root)
    len_distance=Entry(root) 
    image = None 

    def show_diagram():
        try:
            main(int(height_object.get()),int(distance_object.get()),int(focal_objective.get()),int(focal_ocular.get()),int(len_distance.get()),image)
        except ValueError:
            Label(root, text="*Please use integer values.", font=("time new roman",10), fg='red').place(x=225,y=145)

    def images():
        list_image = Tk()
        list_image.title("Images")
        list_image.geometry("500x225+300+0")
        def tree(): 
            list_image.destroy()
            image="tree"
        def tomato():
            list_image.destroy()
            image="tomato"
                        
        Button(list_image, text="tree", width=5, command=tree).place(x=20,y=20)
        Button(list_image, text="tomato", width=5, command=tomato).place(x=20,y=45)
        
        "will make it so it can create multiple images"
    
    height_object.place(x=225,y=20)
    distance_object.place(x=340, y=45)
    focal_objective.place(x=300,y=70)
    focal_ocular.place(x=275,y=95)
    len_distance.place(x=295,y=120)
 
    Button(root, text='Quit', width = 5,command=root.quit).place(x=20,y=170)
    Button(root, text='Submit',width=5, command=show_diagram).place(x=100,y=170)
    Button(root, text='Images', width=5, command=images).place(x=180,y=170)

    mainloop()

 

set_parameters()