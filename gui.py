import tkinter as tk
from tkinter import *
from tkinter import font
from camera import Camera
from settings import Settings

class GUI:

    def createWindow(self):
        root = tk.Tk()

        root.title("THIS IS WINDOW, HELLO!!")

        root.geometry('800x600')

        settings_frame = tk.Frame(root, bg='black', width=200, height=600)
        window_frame = tk.Frame(root, bg='white', width=600, height=600)

        settings_frame.grid(column=0, row=0)
        window_frame.grid(column=1, row=0)

        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

        lbl = Label(window_frame, text="SETTINGS")
        lbl.grid(column=0, row=0, )
        lbl.config(bg='white', fg='black')
        f = font.Font(size=20)
        lbl.config(font=f)
        val = IntVar()
        val.set(0)

        #options = Camera.getCameraIndexes()

        options = [1,2,3,4,5]

        dropdown = OptionMenu(settings_frame, val, *options)
        dropdown.pack()
        dropdown.grid(column=0, row=0)

        dropdown.config(width=10, height=1)

        settings_frame.grid_propagate(False)
        window_frame.grid_propagate(False)

        btn = Button(root, text="Save settings", command=root.destroy,
                     fg="red")
        btn.grid(column=0, row=0)

        btn.place(x=30, y=150)

        root.mainloop()
        print(val.get())

