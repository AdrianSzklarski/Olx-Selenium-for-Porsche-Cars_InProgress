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
        self.get_driver()

    def get_window(self):
        self.root.title('Porsche Cars')
        self.root.wm_attributes('-zoomed', True)

    def get_dir(self):
        save_dir = os.path.dirname(__file__)
        os.chdir(save_dir)

    def get_driver(self):
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.option)
        driver.get('https://www.olx.pl/d/motoryzacja/samochody/porsche/')
        driver.maximize_window()
        driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
        driver.find_element(By.CLASS_NAME, 'css-mf5jvh').click()
        driver.find_element(By.XPATH,
                            '//*[@id="root"]/div[1]/div[2]/form/div[3]/div[1]/div/div[3]/div/div/div[2]/div/div[7]/label/input').click()


if __name__ == '__main__':
    root = tk.Tk()
    app = OlxPage(root)
    root.mainloop()

