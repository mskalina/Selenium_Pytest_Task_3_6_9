import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose browser: ru or en")

