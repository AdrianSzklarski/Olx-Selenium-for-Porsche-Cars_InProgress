import tkinter as tk
from PIL import Image, ImageTk
from module.myGallery import MyGalleryOfCars
import glob


class Icons:
    def __init__(self, root):
        self.root = root

        self.frame = tk.Frame(self.root)
        self.frame.grid()

        self.my_canvas = tk.Canvas(self.frame, width=900, height=900, bg='#d8d8d9')
        self.my_canvas.grid()

        sickPaths = glob.glob(
            r'/home/adrian/Pulpit/selenium_olx/work_dir/*.png')
        self.tableCars = []
        [self.tableCars.append(cars) for cars in sickPaths]
        self.number = len(self.tableCars)

        self.get_icons()

    def get_icons(self):
        '''Method to add a mini gallery'''

        link = f'/home/adrian/Pulpit/selenium_olx/Start_Page.png'
        image = Image.open(link).resize((150, 100), Image.ANTIALIAS)
        image.save(fp=f'/home/adrian/Pulpit/selenium_olx/Start_Porsche2.png')
        link = f'/home/adrian/Pulpit/selenium_olx/Start_Porsche2.png'

        if self.number <= 5:
            for i in range(1, self.number + 1):
                load = Image.open(link)
                render = ImageTk.PhotoImage(load)
                img = tk.Label(self.root, image=render)
                img.image = render
                self.my_canvas.create_image(-165 + i * 180, 10, image=render, anchor="nw")
        elif self.number > 5:
            y = int()
            for j in range(1, 6):
                for i in range(1, self.number + 1):
                    if i % 5 == 0:  # switch to a new line
                        y = i
                    load = Image.open(link)
                    render = ImageTk.PhotoImage(load)
                    img = tk.Label(self.root, image=render)
                    img.image = render
                    self.my_canvas.create_image(-165 + j * 180, 10 + y * 25, image=render, anchor="nw")
        else:
            tk.Label(self.root, text='Wrong Value').place(x=1000, y=156)
