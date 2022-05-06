from pages.automation_page import AutomTestPracticePage
from pages.automation_page import DemoNopCommerce
from pages.sliders_links  import DemoSlider


def test_getSearch_Click(browser):
    new_test = AutomTestPracticePage(browser)
    new_test.loadPage()
    new_test.getSearch_Click()

def test_getTitle(browser):
    new_test = AutomTestPracticePage(browser)
    new_test.loadPage()
    new_test.getTitle()

def test_getWindowId(browser):
    new_test = AutomTestPracticePage(browser)
    new_test.loadPage()
    new_test.getWindowId()

def test_getSearch_ByCSS(browser):
    new_test = AutomTestPracticePage(browser)
    new_test.loadPage()
    new_test.getSearch_ByCSS()

def test_getSearch_winID(browser):
    new_test = AutomTestPracticePage(browser)
    new_test.loadPage()
    new_test.getSearch_winID()

def test_getSearch_MuxWinID(browser):
    new_test = AutomTestPracticePage(browser)
    new_test.loadPage()
    new_test.getSearch_winID()

def test_getSearch_ByXPATH(browser):
    new_test = AutomTestPracticePage(browser)
    new_test.loadPage()
    new_test.getSearch_ByXPATH()

def test_getAlert_PopUp(browser):
    new_test = AutomTestPracticePage(browser)
    new_test.loadPage()
    new_test.getAlert_PopUp()

def test_isDate_Picker(browser):
    new_test = AutomTestPracticePage(browser)
    new_test.loadPage()
    new_test.isDate_Picker()

def test_isDate_PickerNew(browser):
    new_test = AutomTestPracticePage(browser)
    new_test.loadPage()
    new_test.isDate_PickerNew()

def test_get_SignUp(browser):
    new_test = AutomTestPracticePage(browser)
    new_test.loadPage()
    new_test.get_SignUp()

def test_get_Table(browser):
    new_test = AutomTestPracticePage(browser)
    new_test.loadPage()
    new_test.get_Table()

def test_get_doubleClick(browser):
    new_test = AutomTestPracticePage(browser)
    new_test.loadPage()
    new_test.get_doubleClick()

def test_get_DragAndDrop(browser):
    new_test = AutomTestPracticePage(browser)
    new_test.loadPage()
    new_test.get_DragAndDrop()

def test_get_Slider(browser):
    new_test = AutomTestPracticePage(browser)
    new_test.loadPage()
    new_test.get_Slider()

def test_get_Navi(browser):
    new_test = AutomTestPracticePage(browser)
    new_test.get_Navi()

def test_get_Links(browser):
    new_test = AutomTestPracticePage(browser)
    new_test.get_Links()


# class OrangeHRM

def test_get_InfoLogin(browser):
    new_test = DemoNopCommerce(browser)
    new_test.loadPage()
    new_test.get_InfoLogin()

def test_getLogin(browser):
    new_test = DemoNopCommerce(browser)
    new_test.loadPage()
    new_test.getLogin()


# class DemoQueryui

def test_get_DoubleSlider(browser):
    new_test = DemoSlider(browser)
    new_test.loadPage()
    new_test.get_DoubleSlider()

def test_get_SlidersLinks(browser):
    new_test = DemoSlider(browser)
    new_test.get_SlidersLinks()