from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time
import pytest
'''

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser,browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
'''
@pytest.mark.parametrize('link', ['?promo=offer0','?promo=offer1','?promo=offer2','?promo=offer3','?promo=offer4',
                                    '?promo=offer5','?promo=offer6',
                                  pytest.param('?promo=offer7', marks=pytest.mark.xfail),'?promo=offer8',
                                  '?promo=offer9'])
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link}"
    print (link)
    page = ProductPage(browser, link)
    page.open()

    page.add_to_basket()



