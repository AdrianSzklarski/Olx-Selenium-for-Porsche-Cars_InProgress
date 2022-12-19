# import tkinter as tk
class MyGalleryOfCars:
    def __init__(self, root):
        self.root = root
        self.root.config(width=300, height=200)
        self.root.title("Secondary Window")
        self.root.focus()

        self.root.mainloop()

    def get_next(self):
        print('Next')

    def get_prev(self):
        print('Prev')




# root = tk.Tk()
# MyGalleryOfCars(root).get_run()


