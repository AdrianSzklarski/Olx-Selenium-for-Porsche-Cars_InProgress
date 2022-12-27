import tkinter as tk
from PIL import Image, ImageTk
import glob


class MyGalleryOfCars:
    def __init__(self, root):
        self.root = root
        self.root.config(width=300, height=200)
        self.root.title("Secondary Window")
        self.root.focus()

    def get_read_photo(self):
        '''Created a "work_dir_scale" directory'''
        sickPaths = glob.glob(
            r'/home/adrian/Pulpit/selenium_olx/work_dir/*.png')
        self.tableCars = []
        [self.tableCars.append(cars) for cars in sickPaths]

        # This is numeration only, save cars to dir
        for i in range(0, len(self.tableCars)):
            load = Image.open(sickPaths[i])
            image = load.resize((600, 400), Image.ANTIALIAS)
            image.save(fp=f'/home/adrian/Pulpit/selenium_olx/work_dir_scale/Porsche_{i+1}.png')

        return len(self.tableCars)



    # def get_next(self):
    #     # interior loop
    #     from main import Gallery
    #     from main import OlxPage
    #     counter = OlxPage(self.root)
    #     print(counter)
    #     # -------------

        # for cars in range(0, len(self.tableCars)):
        # link = f'/home/adrian/Pulpit/selenium_olx/work_dir_scale/Porsche_{1}.png'
        # load = Image.open(link)
        # render = ImageTk.PhotoImage(load)
        # img = tk.Label(self.root, image=render)
        # img.image = render
        # img.place(x=300, y=50)

    def get_prev(self):
        pass
        # self.counter -= 1
        # print(self.counter)
        # for cars in range(0, len(self.tableCars)):
        #     link = f'/home/adrian/Pulpit/selenium_olx/work_dir_scale/Porsche_{cars}.png'
        #     load = Image.open(link)
        #     render = ImageTk.PhotoImage(load)
        #     img = tk.Label(self.root, image=render)
        #     img.image = render
        #     img.place(x=300, y=50)


