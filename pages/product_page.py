from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def check_add_to_cart_test(self):
        self.add_item_to_cart()
        self.solve_quiz_and_get_code()
        self.check_item_price()
        self.check_item_name()

    # Проверяем промо
    def check_promo(self):
        assert "?promo=newYear" in self.browser.current_url, "Promo code is not activated"

    # Добавляем товар в корзину
    def add_item_to_cart(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN), "The add to cart button was not found"
        basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        basket_btn.click()

    # Проверяем цену товара
    def check_item_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.PRICE_ITEM)
        item_add_price = self.browser.find_element(*ProductPageLocators.PRICE_ADD_ITEM)
        assert item_price.text == item_add_price.text, "The price on the product card and in the notification does not match"
        print(f"Price {item_price.text} correct")

    # Проверяем имя товара
    def check_item_name(self):
        item_name = self.browser.find_element(*ProductPageLocators.NAME_ITEM)
        item_add_name = self.browser.find_element(*ProductPageLocators.NAME_ADD_ITEM)
        assert item_name.text == item_add_name.text, "The name on the card and in the notification do not match"
        print(f"Name \"{item_name.text}\" correct")

    # 
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "The message has not disappeared!"
    
    # 
    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "The message has not disappeared!"