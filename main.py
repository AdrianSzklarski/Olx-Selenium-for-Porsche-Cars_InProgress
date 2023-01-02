from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import tkinter as tk
import time
from os.path import join
from PIL import Image, ImageTk

from module.clearDir import get_clear_dir
from module.myGallery import MyGalleryOfCars
from module.small_icons import Icons


class OlxPage:
    def __init__(self, root, *args, **kwargs):
        self.root = root
        self.option = Options()
        self.total = None


        # controll of interface of user
        self.option.headless = False

        # Calling up methods
        self.get_set_window()
        self.get_selection_model()
        self.get_start_photo()
        self.get_small_icons()

        #Iimport of external files
        get_clear_dir()

    def get_set_window(self):
        ''' Main window settings '''
        self.root.title('Porsche Cars, Program Created by Adrian Szklarski, 12.2022')
        self.root.wm_attributes('-zoomed', True)

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

        driver.find_element(By.XPATH,
                            '//*[@id="root"]/div[1]/div[2]/form/div[3]/div[1]/div/div[3]/div/div/div[2]/div/div[' + str(self.radioValue.get()) + ']/label/input').click()

        # print(driver.page_source)
        link = r'?search%5Bfilter_enum_model%5D%5B0%5D'
        if True:
            if self.radioValue.get() == 1:
                self.link = None
                self.name = 'All'
            elif self.radioValue.get() == 2:
                self.link = f'{link}=cayenne'
                self.name = 'Cayenne'
            elif self.radioValue.get() == 3:
                self.link = f'{link}=911'
                self.name = '911'
            elif self.radioValue.get() == 4:
                self.link = f'{link}=cayenne-s'
                self.name = 'Cayenne-S'
            elif self.radioValue.get() == 5:
                self.link = f'{link}=panamera'
                self.name = 'Panamera'
            elif self.radioValue.get() == 6:
                self.link = f'{link}=boxster'
                self.name = 'Boxter'
            elif self.radioValue.get() == 7:
                self.link = f'{link}=944'
                self.name = '944'
            elif self.radioValue.get() == 8:
                self.link = f'{link}=cayenne-turbo'
                self.name = 'Cayenne-Turbo'
            elif self.radioValue.get() == 9:
                self.link = f'{link}=inny'
                self.name = 'Another'
            else:
                pass

        #  Link-up for selected car model
        driver.get(f'https://www.olx.pl/d/motoryzacja/samochody/porsche/{self.link}')
        #  Information on the number of cars found
        elements = driver.find_elements(By.XPATH,
                                        '//*[@id="root"]/div[1]/div[2]/form/div[4]/div[2]/h3/div')

        #  Unpacking the text and downloading the number
        for element in elements:
            number = element.text
            oneNumber = []
            for iterationNumber in number:
                try:
                    oneNumber.append(str(int(iterationNumber)))
                except ValueError:
                    pass

            self.total = ''
            for unpackList in range(0, len(oneNumber)):
                self.total = self.total + oneNumber[unpackList]

            answer = f'{self.total} Porsche {self.name} models found'
            tk.Label(self.root, text=answer).place(x=60, y=460)

        #  Downloading thumbnail images of cars
        counter = 1
        while True:
            try:
                div = driver.find_element(By.XPATH, f'//*[@id="root"]/div[1]/div[2]/form/div[5]/div/div[2]/div[{counter}]').text
                resultPath = join(r'/home/adrian/Pulpit/selenium_olx/work_dir', f'Porsche{counter}.png')

                if div and counter != 9:
                    link = f'//*[@id="root"]/div[1]/div[2]/form/div[5]/div/div[2]/div[{counter}]/a/div/div/div[1]/div[1]/div'
                    with open(resultPath, 'ab') as file:
                        time.sleep(0.5)
                        file.write(driver.find_element(By.XPATH, link).screenshot_as_png)
                else:
                    pass
            except:
                break
            counter += 1

    def get_start_photo(self):
        link = f'/home/adrian/Pulpit/selenium_olx/Start_Page.png'
        image = Image.open(link).resize((600, 400), Image.ANTIALIAS)
        image.save(fp=f'/home/adrian/Pulpit/selenium_olx/Start_Porsche.png')
        link = f'/home/adrian/Pulpit/selenium_olx/Start_Porsche.png'
        load = Image.open(link)
        render = ImageTk.PhotoImage(load)
        img = tk.Label(self.root, image=render)
        img.image = render
        img.place(x=300, y=60)

    def get_small_icons(self):
        self.new_icons = tk.Toplevel(self.root)
        Icons(self.new_icons)
        self.new_icons.geometry("+%d+%d" % (1000, 156))

        self.new_icons.overrideredirect(True)

class Gallery(OlxPage):
    '''Gallery window'''

    def __init__(self, *args, **kwargs):
        OlxPage.__init__(self, root, *args, **kwargs)
        self.gallery = root
        self.counterUp = 0
        self.counterDown = 0

        menu = tk.Menu(self.gallery)
        file_menu = tk.Menu(menu)
        self.gallery.config(menu=file_menu)
        empty = tk.Menu(file_menu, tearoff=0)  # empty dock
        file_menu.add_cascade(label='                       '
                                    '                       '
                                    '                       '
                                    '                       ', menu=empty)

        filemenu = tk.Menu(file_menu, tearoff=0)
        helpmenu = tk.Menu(file_menu, tearoff=0)

        file_menu.add_cascade(label="File", menu=filemenu)

        # File
        filemenu.add_command(label="New")
        filemenu.add_command(label="Save")
        filemenu.add_command(label="Save as...")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)

        # Next & prev
        file_menu.add_command(label="Next >>", command=self.get_next_photo)
        file_menu.add_command(label="Prev <<", command=self.get_prev_photo)

        # Help
        file_menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About program")
        helpmenu.add_command(label="About...")

    def get_next_photo(self):
        self.lenght = MyGalleryOfCars(self.root).get_read_photo()
        self.counterUp += 1
        if self.counterUp <= self.lenght:
            link = f'/home/adrian/Pulpit/selenium_olx/work_dir_scale/Porsche_{self.counterUp}.png'
            load = Image.open(link)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(self.root, image=render)
            img.image = render
            img.place(x=300, y=60)
        elif self.get_prev_photo():
            self.counterDown = self.counterUp
        else:
            self.counter = 0

    def get_prev_photo(self):
        self.lenght = MyGalleryOfCars(self.root).get_read_photo()
        self.counterDown -= 1
        calc = self.lenght + self.counterDown + 1
        if calc >= 1:
            link = f'/home/adrian/Pulpit/selenium_olx/work_dir_scale/Porsche_{calc}.png'
            load = Image.open(link)
            render = ImageTk.PhotoImage(load)
            img = tk.Label(self.root, image=render)
            img.image = render
            img.place(x=300, y=60)
        elif self.get_next_photo():
            self.counterUp = self.counterDown
        else:
            self.counter = 0

if __name__ == '__main__':
    root = tk.Tk()
    app = Gallery()
    root.mainloop()
