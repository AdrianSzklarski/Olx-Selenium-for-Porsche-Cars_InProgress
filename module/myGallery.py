# import tkinter as tk
class MyGalleryOfCars:
    def __init__(self, root):
        self.root = root
        self.root.config(width=300, height=200)
        self.root.title("Secondary Window")
        self.root.focus()
    def get_run(self):
        self.root.mainloop()

# root = tk.Tk()
# MyGalleryOfCars(root).get_run()


