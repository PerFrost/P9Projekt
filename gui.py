from tkinter import *
from tkinter import font

from camera import Camera
from settings import Settings

from PIL import ImageTk, Image, ImageDraw
import screeninfo

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

        self.camera_resolution_options = ["640x480", "1280x720", "1920x1080"]
        self.camera_resolution_var = StringVar()
        self.camera_resolution_var.set(self.camera_resolution_options[0])

        self.calibration_points = []

        self.monitor_options = [str(x) for x in screeninfo.get_monitors()]
        print(self.monitor_options)
        self.monitor_var = StringVar()
        self.monitor_var.set(self.monitor_options[0])

        self.model_options = ["MediaPipe", "MMPose", "MMPose2"]
        self.model_var = StringVar()
        self.model_var.set(self.model_options[0])

        self.camera = Camera()
        self.camera.change_camera(self.camera_var.get())
        self.camera.change_resolution(*[int(x) for x in self.camera_resolution_var.get().split("x")])

    def createWindow(self):
        self.createSettingsFrame()
        self.createWindowFrame()
        self.root.mainloop()
        return Settings(self.camera_var.get(), self._calculateCalibrationPoints(), self.camera_resolution_var.get(), self._getMonitor(), self.model_var.get())

    def _getMonitor(self):
        monitors = screeninfo.get_monitors()
        monitors_string_list = [str(x) for x in monitors]
        index = monitors_string_list.index(self.monitor_var.get())

        return monitors[index]

    def _calculateCalibrationPoints(self):
        if len(self.calibration_points) == 4:
            xs = [point["x"] for point in self.calibration_points]
            ys = [point["y"] for point in self.calibration_points]

            return {"x_max": max(xs), "x_min": min(xs), "y_max": max(ys), "y_min": min(ys)}
        else:
            max_x, max_y = self.camera_resolution_var.get().split("x")
            return {"x_max": int(max_x), "x_min": 0, "y_max": int(max_y), "y_min": 0}

    def createSettingsFrame(self):
        settings_frame = self.settings_frame

        settings_frame.columnconfigure(0, weight=1)
        settings_frame.rowconfigure(0, weight=1)
        settings_frame.rowconfigure(1, weight=1)
        settings_frame.rowconfigure(2, weight=1)
        settings_frame.rowconfigure(3, weight=1)
        settings_frame.rowconfigure(4, weight=1)
        settings_frame.rowconfigure(5, weight=10)
        settings_frame.rowconfigure(6, weight=1)
        settings_frame.rowconfigure(7, weight=1)

        btn = Button(settings_frame, text="Screen", command=self.show_monitor_settings)
        btn.grid(row=0, column=0, sticky="NSEW")

        btn = Button(settings_frame, text="Camera", command=self.show_camera_settings)
        btn.grid(row=1, column=0, sticky="NSEW")

        btn = Button(settings_frame, text="Calibration", command=self.show_calibration_settings)
        btn.grid(row=2, column=0, sticky="NSEW")

        btn = Button(settings_frame, text="Model", command=self.show_model_settings)
        btn.grid(row=3, column=0, sticky="NSEW")

        btn = Button(settings_frame, text="Save settings", command=self.root.destroy)
        btn.grid(row=6, column=0, sticky="NSEW")

    def createWindowFrame(self):
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
        presentation_frame.rowconfigure(0, weight=1)
        presentation_frame.grid_propagate(False)

        return title_frame, presentation_frame

    def show_camera_settings(self):
        title_frame, presentation_frame = self.createWindowFrame()

        presentation_frame.columnconfigure(1, weight=3)

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

        dropdown = OptionMenu(selection_frame, self.camera_var, *self.camera_options, command=lambda x: (self.camera.change_camera(x), self.make_camera_image_label(image_frame)))
        dropdown.grid(column=1, row=0, sticky="EW")

        lbl = Label(selection_frame, text="Select Resolution")
        lbl.grid(column=0, row=1, sticky="EW")
        lbl.config(bg='white', fg='black')

        dropdown = OptionMenu(selection_frame, self.camera_resolution_var, *self.camera_resolution_options, command=lambda x: (self.camera.change_camera(self.camera_var.get()), self.camera.change_resolution(*[int(i) for i in x.split("x")]), self.make_camera_image_label(image_frame)))
        dropdown.grid(column=1, row=1, sticky="EW")

        self.make_camera_image_label(image_frame)

        print(self.camera_var.get())

    def show_calibration_settings(self):
        title_frame, presentation_frame = self.createWindowFrame()

        presentation_frame.rowconfigure(1, weight=10)

        guide_frame = Frame(presentation_frame, bg='white')
        guide_frame.grid(row=0, column=0, sticky="NSEW")
        guide_frame.columnconfigure(0, weight=1)
        guide_frame.rowconfigure(0, weight=1)
        guide_frame.grid_propagate(False)

        image_frame = Frame(presentation_frame, bg='white')
        image_frame.grid(row=1, column=0, sticky="NSEW")
        image_frame.columnconfigure(0, weight=1)
        image_frame.rowconfigure(0, weight=1)
        image_frame.grid_propagate(False)

        lbl = Label(title_frame, text="Calibration Settings")
        lbl.grid(column=0, row=0, sticky="EW")
        lbl.config(bg='green', fg='black', font=font.Font(size=20))

        lbl = Label(guide_frame, text="Calibrate the camera by selecting the corners")
        lbl.grid(column=0, row=0, sticky="EW")
        lbl.config(bg='white', fg='black', font=font.Font(size=16))

        lbl = self.make_camera_image_label(image_frame)

        lbl.bind("<Button-1>", self.calibration_click)

        print(self.camera_var.get())

    def calibration_click(self, event):
        if len(self.calibration_points) >= 4:
            self.calibration_points.clear()
            image = self.camera.getFrame()
            event.widget.image = ImageTk.PhotoImage(Image.fromarray(image))
        else:
            self.calibration_points.append({"x": event.x, "y": event.y})
            print(self.calibration_points)

        img = ImageTk.getimage(event.widget.image)
        self.draw_calibration_points(img)
        img2 = ImageTk.PhotoImage(img)
        event.widget.configure(image=img2)
        event.widget.image = img2

    def make_camera_image_label(self, frame):
        self.clear_frame(frame)
        image = self.camera.getFrame()

        pilImage = Image.fromarray(image)

        self.draw_calibration_points(pilImage)

        image2 = ImageTk.PhotoImage(pilImage)
        lbl = Label(frame, image=image2)
        lbl.grid(column=0, row=0)
        lbl.image = image2

        return lbl

    def draw_calibration_points(self, image, r=5):
        image_canvas = ImageDraw.Draw(image)
        for point in self.calibration_points:
            image_canvas.ellipse((point["x"] - r, point["y"] - r, point["x"] + r, point["y"] + r), fill='skyblue', outline='skyblue')

        return image_canvas

    def show_monitor_settings(self):
        title_frame, presentation_frame = self.createWindowFrame()

        selection_frame = Frame(presentation_frame, bg='white')
        selection_frame.grid(row=0, column=0, sticky="NSEW")
        selection_frame.columnconfigure(0, weight=1)
        selection_frame.columnconfigure(1, weight=1)
        selection_frame.columnconfigure(2, weight=1)
        selection_frame.rowconfigure(0, weight=1)
        selection_frame.rowconfigure(1, weight=1)
        selection_frame.rowconfigure(2, weight=10)
        selection_frame.grid_propagate(False)

        lbl = Label(title_frame, text="Monitor Settings")
        lbl.grid(column=0, row=0, sticky="EW")
        lbl.config(bg='green', fg='black', font=font.Font(size=20))

        lbl = Label(selection_frame, text="Select Monitor")
        lbl.grid(column=0, row=0, sticky="EW")
        lbl.config(bg='white', fg='black')

        dropdown = OptionMenu(selection_frame, self.monitor_var, *self.monitor_options)
        dropdown.grid(column=1, row=0, sticky="EW")

    def show_model_settings(self):
        title_frame, presentation_frame = self.createWindowFrame()

        selection_frame = Frame(presentation_frame, bg='white')
        selection_frame.grid(row=0, column=0, sticky="NSEW")
        selection_frame.columnconfigure(0, weight=1)
        selection_frame.columnconfigure(1, weight=1)
        selection_frame.columnconfigure(2, weight=1)
        selection_frame.rowconfigure(0, weight=1)
        selection_frame.rowconfigure(1, weight=1)
        selection_frame.rowconfigure(2, weight=10)
        selection_frame.grid_propagate(False)

        lbl = Label(title_frame, text="Model Settings")
        lbl.grid(column=0, row=0, sticky="EW")
        lbl.config(bg='green', fg='black', font=font.Font(size=20))

        lbl = Label(selection_frame, text="Select Model")
        lbl.grid(column=0, row=0, sticky="EW")
        lbl.config(bg='white', fg='black')

        dropdown = OptionMenu(selection_frame, self.model_var, *self.model_options)
        dropdown.grid(column=1, row=0, sticky="EW")


    def clear_window_frame(self):
            self.clear_frame(self.window_frame)

    def clear_frame(self, frame):
            for element in frame.winfo_children():
                element.destroy()


if __name__ == "__main__":
    gui = GUI()
    gui.createWindow()
