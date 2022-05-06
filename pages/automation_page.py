import time
from datetime import datetime

import requests         # for links
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException    # for explicit wait - ignored
from selenium.webdriver import ActionChains                         # for mouse actions
from selenium.webdriver.common.by import By                         # for locators
from selenium.webdriver.support.select import Select                # for selections ex dropdowns
from selenium.webdriver.support.wait import WebDriverWait           # for explicit wait
from selenium.webdriver.support import expected_conditions as EC    # for explicit wait


class AutomTestPracticePage:

    #URL
    URL = "https://testautomationpractice.blogspot.com/"
    URL2 = "https://www.emag.ro/"
    URL3 = "https://www.amazon.com/"

    #Locators
    SEARCH_CSS = (By.CSS_SELECTOR, 'input.wikipedia-search-input')
    SEARCH_TEXT = (By.XPATH, '//input[@id="Wikipedia1_wikipedia-search-input"]')
    SEARCH_FULLXPATH = (By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[1]/div[1]/form/div/span[2]/span[1]/input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'input.wikipedia-search-button')
    COOKIE_BUTTON = (By.CSS_SELECTOR, 'a#cookieChoiceDismiss')
    ALL_SEARCH_RESULTS = (By.XPATH, '//div[@id="Wikipedia1_wikipedia-search-results"]//a')
    SEARCH_ONE = (By.XPATH, '//a[text()="Blogger"]')
    SEARCH_TWO = (By.XPATH, '//div[@id="Wikipedia1_wikipedia-search-results"]//div[@id="wikipedia-search-result-link"]/a')
    ACTIONS = (By.CSS_SELECTOR, '.widget  h2[class="title"]')
    ALERT_TEXT = (By.CSS_SELECTOR, '.column-left-inner .sidebar .widget:nth-child(2) h2')
    ALERT_POPUP = (By.CSS_SELECTOR, 'button[onclick="myFunction()"]')
    ALERT_MSG = (By.CSS_SELECTOR, 'p#demo')
    DATE_PICKER = (By.XPATH, '//input[@id="datepicker"]')
    DATE_SELECT = (By.CSS_SELECTOR, 'td a.ui-state-default.ui-state-highlight')
    DATE_MONTH = (By.CSS_SELECTOR, '.ui-datepicker-month')
    DATE_YEAR = (By.CSS_SELECTOR, '.ui-datepicker-year')
    DATE_NEW = (By.LINK_TEXT, '25')
    LINKS_PAGE = (By.XPATH, "//div[@class='div a']//a")
    IFRAME_TAG = (By.TAG_NAME, "iframe")
    FIRST_NAME = (By.CSS_SELECTOR, '#RESULT_TextField-1')
    LAST_NAME = (By.CSS_SELECTOR, '#RESULT_TextField-2')
    PHONE_NO = (By.NAME, 'RESULT_TextField-3')
    COUNTRY = (By.NAME, 'RESULT_TextField-4')
    CITY = (By.NAME, 'RESULT_TextField-5')
    EMAIL = (By.NAME, 'RESULT_TextField-6')
    MALE_BUTTON = (By.XPATH, '//label[@for="RESULT_RadioButton-7_0"]')
    FEMALE_BUTTON = (By.XPATH, '//label[@for="RESULT_RadioButton-7_1"]')
    VOLUNTEER = (By.CSS_SELECTOR, '#q19 h1')
    CATEGORY = (By.CSS_SELECTOR, 'div .q .question.top_question')
    DAYS = (By.CSS_SELECTOR, '#q15.q  td label')
    BEST_TIME = (By.CSS_SELECTOR, '#RESULT_RadioButton-9')
    SUBMIT = (By.XPATH, '//input[@id="FSsubmit"]')
    TABLE_HEAD = (By.XPATH, '//table[@name="BookTable"]/tbody/tr[1]/th')
    FIRST_ROW = (By.XPATH, '//table[@name="BookTable"]/tbody/tr[2]/td')
    SECOND_ROW = (By.XPATH, '//table[@name="BookTable"]/tbody/tr[3]/td')
    THIRD_ROW = (By.XPATH, '//table[@name="BookTable"]/tbody/tr[4]/td')
    TABLE_ROWS = (By.XPATH, '//table[@name="BookTable"]//tr')
    TABLE_COL = (By.XPATH, '//table[@name="BookTable"]//tr[1]/th')
    ALL_CELLS = (By.XPATH, '//table[@name="BookTable"]/tbody/tr["+str(i)+"]/td["+str(j)+"]')
    DOUBLE_CLICK_ONE = (By.XPATH, '//input[@id="field1"]')
    DOUBLE_CLICK_TWO = (By.XPATH, '//input[@id="field2"]')
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[ondblclick="myFunction1()"]')
    DRAG_ELEM = (By.ID, 'draggable')
    DROP_ELEM = (By.ID, 'droppable')
    SLIDER = (By.CSS_SELECTOR, 'span.ui-slider-handle.ui-corner-all.ui-state-default')
    AMAZON_SEARCH = (By.CSS_SELECTOR, 'input#twotabsearchtextbox')
    AMAZON_CLICK = (By.CSS_SELECTOR, '#nav-search-submit-button')
    ALL_IMG_AMAZON = (By.TAG_NAME, 'img')


    #Initializer
    def __init__(self, browser):            # constructor, sets the initial state of an object and it is called every time a new object is created
        self.browser = browser              # instance attributes

    # Instance Interaction methods
    def loadPage(self):
        self.browser.get(self.URL)
        self.browser.find_element(*self.COOKIE_BUTTON).click()

    def getSearch_Click(self):
        self.browser.find_element(*self.SEARCH_BUTTON).click()
        print("\n ---", self.browser.title)
        print(" ---", self.browser.current_url)

    def getTitle(self):
        print("\n", self.browser.title)
        assert self.browser.title == 'Automation Testing Practice', 'Title of the page was changed'

    def getWindowId(self):
        # it returns the current page id
        windowId = self.browser.current_window_handle
        print(f'\nThe ID of the page {self.browser.title} is:   {windowId}')
        self.browser.close()

    def getSearch_ByCSS(self):
        self.browser.find_element(*self.SEARCH_CSS).send_keys("Turism")
        obiect = AutomTestPracticePage
        obiect.getSearch_Click(self)

        self.browser.maximize_window()

        all_search_results = self.browser.find_elements(*self.ALL_SEARCH_RESULTS)
        print(f'\nNo. of search results on \'{self.browser.title}\' page:  {len(all_search_results)}\n')

        # all the elements and hiperlinks received after searching
        for i in all_search_results:
            print(i.text, " - ", i.get_attribute('href'))

        time.sleep(2)

        self.browser.close()

    def getSearch_winID(self):
        self.browser.maximize_window()
        self.browser.find_element(*self.SEARCH_ONE).click()

        # it returns the id's of multiple browser windows
        windowId = self.browser.window_handles

        parent = windowId[0]
        child = windowId[1]

        # we have two windows only
        self.browser.switch_to.window(parent)
        print("\n   ID   ---  ", parent, "Title of the parent browser: ", self.browser.title)
        self.browser.switch_to.window(child)
        print("   ID   ---  ", child, "Title of the child browser: ", self.browser.title)

        time.sleep(2)

        self.browser.quit()

    def getSearch_ByXPATH(self):
        self.browser.find_element(*self.SEARCH_TEXT).send_keys("Selenium")
        obiect = AutomTestPracticePage
        obiect.getSearch_Click(self)

        self.browser.maximize_window()

        elem = self.browser.find_elements(*self.SEARCH_TWO)
        print("Elements on the page: ", len(elem))

        for i in range(len(elem)):
            elem[i].click()
            print(elem[i].text, " --- ", elem[i].get_attribute('href'))
            time.sleep(1)

        self.browser.quit()

    def getAlert_PopUp(self):
        try:
            self.browser.implicitly_wait(10)
        except:
            None

        self.browser.maximize_window()
        alert = self.browser.find_element(*self.ALERT_TEXT).text
        print("\n", alert)

        # we click on the alert button and print the message from it
        alert_click_button = self.browser.find_element(*self.ALERT_POPUP)
        print("The text from the alert click box is: ", alert_click_button.text)
        alert_click_button.click()

        # we go on allert message box
        var_alert = self.browser.switch_to.alert

        # we print the message inside the alert box and click OK to close the alert box
        print("The text from the alert message box is: ", var_alert.text)
        var_alert.accept()
        msg = self.browser.find_element(*self.ALERT_MSG).text
        print("The status of the alert action is : ", msg)

        time.sleep(2)

        self.browser.quit()


    def isDate_Picker(self):
        date = self.browser.find_element(*self.DATE_PICKER)

        # click on date picker
        if date.is_enabled():
            date.click()

        zi = self.browser.find_element(*self.DATE_SELECT)
        zi.click()
        luna = self.browser.find_element(*self.DATE_MONTH)
        an = self.browser.find_element(*self.DATE_YEAR)
        print('\n','The date selected is:   ', luna.text, '-', zi.text, '-', an.text)

        # today
        from datetime import date
        astazi = date.today()
        print("Today's date:", astazi)
        print("Month: ", astazi.month, "/  Day: ", astazi.day, "/  Year: ", astazi.year)

        # now
        current_date = datetime.now()
        print("Today's current date:", current_date)     # complete date and time

        # strftime
        d1 = astazi.strftime("%m/%d/%Y")
        print(d1)


        time.sleep(2)

        self.browser.quit()


    def isDate_PickerNew(self):
        date = self.browser.find_element(*self.DATE_PICKER)

        # click on date picker
        if date.is_enabled():
            date.click()

        self.browser.find_element(*self.DATE_NEW).click()


        time.sleep(2)

        self.browser.quit()


    def get_SignUp(self):
        self.browser.maximize_window()

        parent_frame = self.browser.find_element(*self.IFRAME_TAG)
        self.browser.switch_to.frame(parent_frame)

        # all caterories
        vol = self.browser.find_element(*self.VOLUNTEER)
        print("\nCategory: ", vol.text)

        categ = self.browser.find_elements(*self.CATEGORY)
        print()
        for i in categ:
            print("Category: ", i.text)


        # name and adress
        self.browser.find_element(*self.FIRST_NAME).send_keys("Gica")
        self.browser.find_element(*self.LAST_NAME).send_keys("Hagi")
        self.browser.find_element(*self.PHONE_NO).send_keys("0722000333")
        self.browser.find_element(*self.COUNTRY).send_keys("Spain")
        self.browser.find_element(*self.CITY).send_keys("Sevilla")
        self.browser.find_element(*self.EMAIL).send_keys("gica@yahoo.com")

        # gender
        male = self.browser.find_element(*self.MALE_BUTTON)
        male.click()

        # days available
        print("\nDays available: ")
        zile = self.browser.find_elements(*self.DAYS)
        for i in range(len(zile)-5, len(zile)-2):
            zile[i].click()
            print("     ", zile[i].text.capitalize())


        # best time to contact
        best_time = Select(self.browser.find_element(*self.BEST_TIME))
        best_time.select_by_index(2)

        # submit
        submit = self.browser.find_element(*self.SUBMIT)
        submit.click()

        time.sleep(2)

        self.browser.quit()

    def get_Table(self):
        self.browser.maximize_window()

        rows = self.browser.find_elements(*self.TABLE_ROWS)
        col = self.browser.find_elements(*self.TABLE_COL)
        print(f'\nThere are \'{len(rows)}\' rows, \'{len(col)}\' columns and a total no. of \'{len(rows) * len(col)}\' cells in our table')

        table_head = self.browser.find_elements(*self.TABLE_HEAD)
        print()
        for i in table_head:
            print(i.text, end="                   ")
        print("\n--------------------------------------------------------------------------------------")

        first_row = self.browser.find_elements(*self.FIRST_ROW)
        print()
        for i in first_row:
            print(i.text, end="              ")

        second_row = self.browser.find_elements(*self.SECOND_ROW)
        print()
        for i in second_row:
            print(i.text, end="                  ")

        third_row = self.browser.find_elements(*self.THIRD_ROW)
        print()
        for i in third_row:
            print(i.text, end="                    ")

        # ro = len(rows)
        # co = len(col)

        # for i in range(2, ro + 1):
        #     for j in range(1, co + 1):
        #         cell = self.browser.find_element(*self.ALL_CELLS)
        #         print(cell.text, end="   ")
        #     print()

        self.browser.quit()


    def get_doubleClick(self):
        self.browser.maximize_window()
        d_click_one = self.browser.find_element(*self.DOUBLE_CLICK_ONE)
        d_click_one.clear()
        d_click_one.send_keys("Good morning!")

        d_click_button = self.browser.find_element(*self.DOUBLE_CLICK_BUTTON)

        actions = ActionChains(self.browser)
        actions.double_click(d_click_button).perform()

        time.sleep(3)

        self.browser.quit()

    def get_DragAndDrop(self):
        self.browser.maximize_window()
        drag = self.browser.find_element(*self.DRAG_ELEM)
        drop = self.browser.find_element(*self.DROP_ELEM)

        actions = ActionChains(self.browser)
        actions.drag_and_drop(drag, drop).perform()

        time.sleep(3)

        self.browser.quit()

    def get_Slider(self):
        self.browser.maximize_window()
        slider = self.browser.find_element(*self.SLIDER)

        print("\nInitial position of the slider: ", slider.location)

        actions = ActionChains(self.browser)
        actions.drag_and_drop_by_offset(slider, 150, 0).perform()

        print("Final position of the slider: ", slider.location)

        time.sleep(3)

        self.browser.quit()

    def get_Navi(self):
        self.browser.maximize_window()

        self.browser.get(self.URL2)
        self.browser.get(self.URL3)

        self.browser.back()
        self.browser.forward()

        self.browser.find_element(*self.AMAZON_SEARCH).send_keys("pet")

        timp = WebDriverWait(self.browser, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, Exception])
        timp.until(EC.presence_of_element_located(self.AMAZON_CLICK)).click()

        time.sleep(3)

        self.browser.refresh()
        time.sleep(2)

        self.browser.quit()


    def get_Links(self):
        self.browser.maximize_window()

        self.browser.get(self.URL3)

        all_img = self.browser.find_elements(*self.ALL_IMG_AMAZON)
        print("\nTotal no. of img on amazon: ", len(all_img))

        broken, ok = 0, 0
        for img in range(len(all_img)):
            url = all_img[img].get_attribute('src')

            try:
                cerere = requests.head(url)
            except:
                None

            if cerere.status_code >= 400:
                print(f'Link {img} broken: ', url)
                broken += 1
            else:
                print(f'Link {img} ok: ', url)
                ok += 1

        print("Total no. of broken amazon links: ", broken)
        print("Total no. of ok amazon links: ", ok)

        self.browser.quit()


class DemoNopCommerce:

    #URL
    URL_NOP = "https://demo.nopcommerce.com/"

    #Locators
    LOGIN_TEXT = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a')
    USER_FIELD = (By.CSS_SELECTOR, '#Email')
    PASS_FIELD = (By.NAME, 'Password')
    LOGIN_BUTTON = (By.XPATH, '//div/button[@type="submit"]')
    APPAREL = (By.XPATH, '/html/body/div[6]/div[2]/ul[1]/li[3]/a')
    SHOES = (By.XPATH, '/html/body/div[6]/div[2]/ul[1]/li[3]/ul/li[1]/a')
    CLOTHING = (By.XPATH, '/html/body/div[6]/div[2]/ul[1]/li[3]/ul/li[2]/a')
    ACCESSORIES = (By.XPATH, '/html/body/div[6]/div[2]/ul[1]/li[3]/ul/li[3]/a')


    #Initializer
    def __init__(self, browser):        # constructor, sets the initial state of an object and it is called every time a new object is created
        self.browser = browser          # instance attributes

    # Instance Interaction methods
    def loadPage(self):
        self.browser.get(self.URL_NOP)

    def get_InfoLogin(self):
        login_text = self.browser.find_element(*self.LOGIN_TEXT).text
        print("\nAction: ", login_text)
        print("\n ---", self.browser.title)
        print(" ---", self.browser.current_url)
        print(" ---", self.browser.page_source)

        self.browser.quit()

    def getLogin(self):
        self.browser.maximize_window()
        self.browser.find_element(*self.LOGIN_TEXT).click()

        self.browser.find_element(*self.USER_FIELD).send_keys("___@yahoo.com")  # create your own
        self.browser.find_element(*self.PASS_FIELD).send_keys("_____")          # create your own
        self.browser.find_element(*self.LOGIN_BUTTON).click()

        apparel = self.browser.find_element(*self.APPAREL)
        shoes = self.browser.find_element(*self.SHOES)
        clothing = self.browser.find_element(*self.CLOTHING)
        accessories = self.browser.find_element(*self.ACCESSORIES)

        actions = ActionChains(self.browser)
        actions.move_to_element(apparel).move_to_element(shoes).move_to_element(clothing).move_to_element(accessories).click().perform()

        time.sleep(3)

        self.browser.quit()

