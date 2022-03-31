import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

link=" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#link="http://google.com/bla"

@pytest.fixture
def browser(request):
    browser = None
    user_language = request.config.getoption("language")
    print("\nstart chrome browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    #---Нужно отредактировать или удалить эту строку для провекри теста, к сожалению, без этого аргумента Хром не запускается, хоть в PATH все добавлено
    options.add_argument(r"C:\Users\wwwma\environments\selenium_course\chromedriver") 
    #---
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
    
def test_add_button_is_present(browser):
    browser.get(link) 
    browser.implicitly_wait(10)
    button1 = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    btn_len=len(button1)
    assert btn_len > 0, "Add button is not displayed" 
    time.sleep(8)