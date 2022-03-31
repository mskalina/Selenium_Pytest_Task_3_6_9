import pytest
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose browser: ru or en")

