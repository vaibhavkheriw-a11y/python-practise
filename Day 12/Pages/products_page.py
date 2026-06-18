from selenium.webdriver.common.by import By


class ProductsPage:

    products_title = (By.CLASS_NAME, "title")
    backpack_add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    backpack_remove_button = (By.ID, "remove-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, my_page_driver):
        self.my_page_driver = my_page_driver

    def get_products_title(self):
        return self.my_page_driver.get_text_of_element(self.products_title)

    def add_backpack_to_cart(self):
        self.my_page_driver.click_on_element(self.backpack_add_to_cart_button)

    def remove_backpack_from_cart(self):
        self.my_page_driver.click_on_element(self.backpack_remove_button)

    def get_cart_badge_text(self):
        return self.my_page_driver.get_text_of_element(self.cart_badge)

    def get_backpack_button_text(self):
        return self.my_page_driver.get_text_of_element(self.backpack_add_to_cart_button)

    def open_cart(self):
        self.my_page_driver.click_on_element(self.cart_link)
