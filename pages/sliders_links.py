import time

import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DemoSlider:

    #URL
    URL_SLIDER = "https://www.snapdeal.com/products/mens-tshirts-polos?sort=plrty&utm_source=earth_semnonbrand&utm_medium=disp&utm_content=TShirts&utm_campaign=menapparel&utm_term=24101418888&gclid=Cj0KCQjwyMiTBhDKARIsAAJ-9VsHirTiaacBcFZQa5sTkth3Nzy0hxe-ZAXU9uBlpTg4nuppyLRMObAaAm-eEALw_wc"
    URL_LINKS = "https://www.opticaeugen.ro/"


    #Locators
    SLIDER_LEFT = (By.CSS_SELECTOR, '.filter-price-slider.ui-slider.ui-slider-horizontal.ui-widget.ui-widget-content.ui-corner-all :nth-child(1)')
    SLIDER_RIGHT = (By.XPATH, '//*[@id="content_wrapper"]/div[9]/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[1]/a[2]')
    COOKIES_BUTTON = (By.CSS_SELECTOR, '.col-xs-12.col-sm-5.col-md-4.col-lg-3.cookie-banner-buttons button.btn.btn-primary.js-accept.gtm_h76e8zjgoo.btn-block')
    NO_LINKS = (By.TAG_NAME, 'a')
    PAGE = (By.CSS_SELECTOR, '.layout-fullwidth.header-style-1.ls-overflow-visible')


    #Initializer
    def __init__(self, browser):         # constructor, sets the initial state of an object and it is called every time a new object is created
        self.browser = browser           # instance attributes

    # Instances Interaction methods
    def loadPage(self):
        self.browser.get(self.URL_SLIDER)

    def get_DoubleSlider(self):
        try:
            self.browser.implicitly_wait(5)
        except:
            None

        self.browser.maximize_window()

        slider_left = self.browser.find_element(*self.SLIDER_LEFT)
        slider_right = self.browser.find_element(*self.SLIDER_RIGHT)

        print("\nInitial position of the left slider: ", slider_left.location)
        print("Initial position of the right slider: ", slider_right.location)

        actions = ActionChains(self.browser)
        actions.drag_and_drop_by_offset(slider_left, 80, 0).perform()
        time.sleep(2)
        actions.drag_and_drop_by_offset(slider_right, -75, 0).perform()

        print("\nFinal position of the left slider: ", slider_left.location)
        print("Final position of the right slider: ", slider_right.location)

        time.sleep(2)

        self.browser.quit()

    def get_SlidersLinks(self):
        try:
            self.browser.implicitly_wait(10)
        except:
            None

        self.browser.maximize_window()
        self.browser.get(self.URL_LINKS)

        links = self.browser.find_elements(*self.NO_LINKS)
        self.browser.find_element(*self.PAGE)

        print(f'\n\nTile of the page:\n\n {self.browser.title} : \n\n links = {len(links)}')

        print("\n All the links on the page: \n")

        total_broken, total_ok = 0, 0
        for i in links:
            print_links = i.get_attribute('href')

            try:
                request = requests.head(print_links)
            except:
                None

            if request.status_code >= 400:
                print('   The link is broken:   ', i.text, "                              ",print_links)
                total_broken += 1
            else:
                print('   The link is ok:   ', i.text, "                              ", print_links)
                total_ok += 1

        print("----------------------------------------------------------------------------------------------")
        print("Total no. of broken links: ", total_broken)
        print("Total no. of ok links: ", total_ok)


        self.browser.quit()