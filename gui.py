from tkinter import *
from tkinter import font

from camera import Camera
from settings import Settings

from PIL import ImageTk, Image


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Settings")

        self.root.geometry('1280x720')

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=10)
        self.root.rowconfigure(0, weight=1)

        self.settings_frame = Frame(self.root, bg='black')
        self.settings_frame.grid(row=0, column=0, sticky="NSEW")
        self.settings_frame.grid_propagate(False)

        self.window_frame = Frame(self.root, bg='white')
        self.window_frame.grid(row=0, column=1, sticky="NSEW")
        self.window_frame.grid_propagate(False)

        self.camera_options = Camera.getCameraIndexes()
        self.camera_var = IntVar()
        self.camera_var.set(self.camera_options[0])

        self.camera_resolution_options = ["720p", "1080p"]
        self.camera_resolution_var = StringVar()
        self.camera_resolution_var.set(self.camera_resolution_options[0])

    def createWindow(self):
        self.createSettingsFrame()
        self.createWindowFrame()
        self.root.mainloop()

    def createSettingsFrame(self):
        settings_frame = self.settings_frame

        settings_frame.columnconfigure(0, weight=1)
        settings_frame.rowconfigure(0, weight=1)
        settings_frame.rowconfigure(1, weight=1)
        settings_frame.rowconfigure(2, weight=1)
        settings_frame.rowconfigure(3, weight=1)
        settings_frame.rowconfigure(4, weight=10)
        settings_frame.rowconfigure(5, weight=1)
        settings_frame.rowconfigure(6, weight=1)

        btn = Button(settings_frame, text="Screen", command=self.show_monitor_settings)
        btn.grid(row=0, column=0, sticky="NSEW")

        btn = Button(settings_frame, text="Camera", command=self.show_camera_settings)
        btn.grid(row=1, column=0, sticky="NSEW")

        btn = Button(settings_frame, text="Calibration", command=self.show_calibration_settings)
        btn.grid(row=2, column=0, sticky="NSEW")

        btn = Button(settings_frame, text="Save settings", command=self.root.destroy)
        btn.grid(row=5, column=0, sticky="NSEW")

    def createWindowFrame(self):
        window_frame = self.window_frame

    def show_camera_settings(self):
        self.clear_window_frame()

        window_frame = self.window_frame

        window_frame.columnconfigure(0, weight=1)
        window_frame.rowconfigure(0, weight=1)
        window_frame.rowconfigure(1, weight=14)

        title_frame = Frame(window_frame, bg='green')
        title_frame.grid(row=0, column=0, sticky="NSEW")
        title_frame.columnconfigure(0, weight=1)
        title_frame.rowconfigure(0, weight=1)
        title_frame.grid_propagate(False)

        presentation_frame = Frame(window_frame, bg='white')
        presentation_frame.grid(row=1, column=0, sticky="NSEW")
        presentation_frame.columnconfigure(0, weight=1)
        presentation_frame.columnconfigure(1, weight=3)
        presentation_frame.rowconfigure(0, weight=1)
        presentation_frame.grid_propagate(False)

        selection_frame = Frame(presentation_frame, bg='white')
        selection_frame.grid(row=0, column=0, sticky="NSEW")
        selection_frame.columnconfigure(0, weight=1)
        selection_frame.columnconfigure(1, weight=1)
        selection_frame.rowconfigure(0, weight=1)
        selection_frame.rowconfigure(1, weight=1)
        selection_frame.rowconfigure(2, weight=10)
        selection_frame.grid_propagate(False)

        image_frame = Frame(presentation_frame, bg='white')
        image_frame.grid(row=0, column=1, sticky="NSEW")
        image_frame.columnconfigure(0, weight=1)
        image_frame.rowconfigure(0, weight=1)
        image_frame.grid_propagate(False)

        lbl = Label(title_frame, text="Camera Settings")
        lbl.grid(column=0, row=0, sticky="EW")
        lbl.config(bg='green', fg='black', font=font.Font(size=20))


        lbl = Label(selection_frame, text="Select Camera")
        lbl.grid(column=0, row=0, sticky="EW")
        lbl.config(bg='white', fg='black')

        dropdown = OptionMenu(selection_frame, self.camera_var, *self.camera_options)
        dropdown.grid(column=1, row=0, sticky="EW")

        lbl = Label(selection_frame, text="Select Resolution")
        lbl.grid(column=0, row=1, sticky="EW")
        lbl.config(bg='white', fg='black')

        dropdown = OptionMenu(selection_frame, self.camera_resolution_var, *self.camera_resolution_options)
        dropdown.grid(column=1, row=1, sticky="EW")

        index = self.camera_var.get()

        cam = Camera().change_camera(index)
        image = cam.getFrame()
        del cam
        image2 = ImageTk.PhotoImage(Image.fromarray(image))
        lbl = Label(image_frame, image=image2)
        lbl.grid(column=0, row=0)
        lbl.image = image2

        print(self.camera_var.get())


        # Button(window_frame, text="Camera", command=self.root.destroy).grid(row=0, column=0)


    def show_calibration_settings(self):
        self.clear_window_frame()
        window_frame = self.window_frame

        Button(window_frame, text="Calibration", command=self.root.destroy).grid(row=0, column=0)


    def show_monitor_settings(self):
        self.clear_window_frame()

        window_frame = self.window_frame

        Button(window_frame, text="Monitor", command=self.root.destroy).grid(row=0, column=0)

    def clear_window_frame(self):
        for element in self.window_frame.winfo_children():
            element.destroy()


if __name__ == "__main__":
    gui = GUI()
    gui.createWindow()
