from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        product_name, product_price = self.is_product_present()
        self.should_be_add_to_basket_button()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()
        self.should_be_added_procuct(product_name, product_price)




    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

    def is_product_present(self):
        print (self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text)
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text



    def should_be_added_procuct(self, product_name, product_price):
        print(self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_ALERT).text)

        assert self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_ALERT).text == product_name, "Product name is incorrect"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_PRICE).text == product_price, "Product price is incorrect"
        #return self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_ALERT).text, self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_PRICE).text