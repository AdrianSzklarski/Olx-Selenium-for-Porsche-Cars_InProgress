import tkinter as tk
from PIL import Image, ImageTk
from module.myGallery import MyGalleryOfCars


class Icons:
    def __init__(self, root):
        self.root = root

        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0)

        self.my_canvas = tk.Canvas(self.frame, width=150, height=100, bg='white')
        self.my_canvas.grid()

        self.get_icons()

    def get_icons(self):
        '''Method to add a mini gallery'''

        if MyGalleryOfCars(self.root).get_read_photo() == 0:  # Displaying a photo before launching the application
            numberIcons = 1
        else:
            numberIcons = MyGalleryOfCars(self.root).get_read_photo()  # Photos after launching the application

        for i in range(1, numberIcons + 1):
            link = f'/home/adrian/Pulpit/selenium_olx/Start_Page.png'
            image = Image.open(link).resize((150, 100), Image.ANTIALIAS)
            image.save(fp=f'/home/adrian/Pulpit/selenium_olx/Start_Porsche2.png')
            link = f'/home/adrian/Pulpit/selenium_olx/Start_Porsche2.png'
            load = Image.open(link)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(self.root, image=render)
            img.image = render
            self.my_canvas.create_image(0, 0, image=render, anchor="nw")
