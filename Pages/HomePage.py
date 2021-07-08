from selenium import webdriver
from selenium.webdriver import ActionChains


class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.phone_pda_option_xpath = "//a[normalize-space()='Phones & PDAs']"
        self.laptop_notebook_xpath = "//a[normalize-space()='Laptops & Notebooks']"
        self.show_all_laptop_notebook_xpath = "//a[normalize-space()='Show All Laptops & Notebooks']"
        self.cart_button_xpath = "//span[@id='cart-total']"
        self.checkout_button_xpath = "//strong[normalize-space()='Checkout']"

    def click_phone_pda_option(self):
        self.driver.find_element_by_xpath(self.phone_pda_option_xpath).click()

    def hover_laptop_notebook_option(self):
        laptops = self.driver.find_element_by_xpath(self.laptop_notebook_xpath)
        self.action.move_to_element(laptops).perform()

    def click_show_all_laptop_notebook_option(self):
        self.driver.find_element_by_xpath(self.show_all_laptop_notebook_xpath).click()

    def click_cart_button(self):
        self.driver.find_element_by_xpath(self.cart_button_xpath).click()

    def click_checkout_cart_button(self):
        self.driver.find_element_by_xpath(self.checkout_button_xpath).click()
