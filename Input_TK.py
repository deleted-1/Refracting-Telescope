import tkinter
from tkinter import messagebox
class ImageLocationGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        
        self.label1 = tkinter.Label(self.main_window, text="Type 1 for the object to be past 2 times the focal point")
        self.label2 = tkinter.Label(self.main_window, text="Type 2 for the object to be at 2 times the focal point")
        self.label3 = tkinter.Label(self.main_window, text="Type 3 for the object to be between 2 times the focal point and the focal point")
        self.label4 = tkinter.Label(self.main_window, text="Type 4 for the object to be at the focal point")
        self.prompt_label = tkinter.Label(self.top_frame, \
        text="Where would you like the image to be placed? ")
        self.kilo_entry = tkinter.Entry(self.top_frame, \
        width=10)
        
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')
        
        self.calc_button = tkinter.Button(self.bottom_frame, \
        text='Submit', \
        command=self.display)
        self.quit_button = tkinter.Button(self.bottom_frame, \
        text='Quit', \

        command=self.main_window.quit)

        
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()
    
    def display(self):
        pass
    
image_locate = ImageLocationGUI()
