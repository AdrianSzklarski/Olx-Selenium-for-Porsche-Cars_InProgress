import tkinter as tk
from PIL import Image, ImageTk


class MyGalleryOfCars:
    def __init__(self, root):
        self.root = root
        self.root.config(width=300, height=200)
        self.root.title("Secondary Window")
        self.root.focus()
        self.get_read_photo()

        self.root.mainloop()

    def get_read_photo(self):
        link = r'/home/adrian/Pulpit/selenium_olx/Test_photo.png'
        load = Image.open(link)
        image = load.resize((600, 400), Image.ANTIALIAS)
        image.save(fp='/home/adrian/Pulpit/selenium_olx/Test_photo_scale.png')

        link = r'/home/adrian/Pulpit/selenium_olx/Test_photo_scale.png'
        load = Image.open(link)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self.root, image=render)
        img.image = render
        img.place(x=300, y=50)


    def get_next(self):
        print('Next')

    def get_prev(self):
        print('Prev')




# root = tk.Tk()
# MyGalleryOfCars(root).get_run()


