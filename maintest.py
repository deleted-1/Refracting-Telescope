from tkinter import *

root=Tk()

url = Label(root,text="Enter Url")
url.grid(row=0,padx=10,pady=10)

entry_url = Entry(root,width="50")
entry_url.grid(row=0,column=1,padx=5,pady=10,ipady=3)

root.geometry("600x300+150+150")

root.mainloop()