# imports for scrapping to olx page
from selenium import webdriver
from selenium.webdriver.common.by import By
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

        # Calling up methods
        self.get_window()
        self.get_dir()
        self.get_selection_model()

    def get_window(self):
        ''' Main window settings '''
        self.root.title('Porsche Cars')
        self.root.wm_attributes('-zoomed', True)

    def get_dir(self):
        ''' Setting the root directory '''
        save_dir = os.path.dirname(__file__)
        os.chdir(save_dir)

    def get_selection_model(self):
        ''' Addition of car model selection buttons for analysis '''
        tk.Label(self.root, text="Select of model's Porsche: ").place(x=60, y=60)

        self.radioValue = tk.IntVar(self.root, 0)
        tk.Radiobutton(self.root, text="All", variable=self.radioValue, value=1, command=self.get_driver).place(x=50, y=100)
        tk.Radiobutton(self.root, text="Cayenne", variable=self.radioValue, value=2, command=self.get_driver).place(x=50, y=140)
        tk.Radiobutton(self.root, text="911", variable=self.radioValue, value=3, command=self.get_driver).place(x=50, y=180)
        tk.Radiobutton(self.root, text="Cayenne S", variable=self.radioValue, value=4, command=self.get_driver).place(x=50, y=220)
        tk.Radiobutton(self.root, text="Panamera", variable=self.radioValue, value=5, command=self.get_driver).place(x=50, y=260)
        tk.Radiobutton(self.root, text="Boxter", variable=self.radioValue, value=6, command=self.get_driver).place(x=50, y=300)
        tk.Radiobutton(self.root, text="944", variable=self.radioValue, value=7, command=self.get_driver).place(x=50, y=340)
        tk.Radiobutton(self.root, text="Cayenne Turbo", variable=self.radioValue, value=8, command=self.get_driver).place(x=50, y=380)
        tk.Radiobutton(self.root, text="More", variable=self.radioValue, value=9, command=self.get_driver).place(x=50, y=420)

    def get_driver(self):
        ''' Scrapping the olx page for Porsche '''
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.option)
        driver.get('https://www.olx.pl/d/motoryzacja/samochody/porsche/')
        driver.maximize_window()
        driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
        driver.find_element(By.CLASS_NAME, 'css-mf5jvh').click()

        driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[2]/form/div[3]/div[1]/div/div[3]/div/div/div[2]/div/div[' + str(self.radioValue.get()) + ']/label/input').click()

if __name__ == '__main__':
    root = tk.Tk()
    app = OlxPage(root)
    root.mainloop()
