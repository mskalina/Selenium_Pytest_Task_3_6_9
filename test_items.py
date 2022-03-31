import pytest
import time

link=" http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#link="http://google.com/bla"
    
def test_add_button_is_present(browser):
    browser.get(link) 
    browser.implicitly_wait(10)
    button1 = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    btn_len=len(button1)
    assert btn_len > 0, "Add button is not displayed" 
    time.sleep(8)