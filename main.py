# imports for scrapping to olx page
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import tkinter as tk
import time, os


class OlxPage:
    def __init__(self, root):
        self.root = root
        self.option = Options()

        # controll of interface of user
        self.option.headless = False





if __name__ == '__main__':
    root = tk.Tk()
    app = OlxPage(root)
    root.mainloop()
