# imports for scrapping to olx page
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import tkinter as tk
import time, os

class OlxPage:
    def __init__(self, root):
        self.root = root


if __name__ == '__main__':
    root = tk.Tk()
    app = OlxPage(root)
    root.mainloop()
