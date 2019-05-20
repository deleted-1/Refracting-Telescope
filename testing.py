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


work 
root.mainloop()