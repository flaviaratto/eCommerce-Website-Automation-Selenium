class iPhonePage():
    def __init__(self, driver):
        self.driver = driver
        self.iphone_image_xpath = "//ul[@class='thumbnails']//li[1]//a[1]"
        self.next_arrow_xpath = "//button[@title='Next (Right arrow key)']"
        self.close_button_xpath = "//button[normalize-space()='×']"
        self.input_quantity_textbox_xpath = "//input[@id='input-quantity']"
        self.add_to_cart_xpath = "//button[@id='button-cart']"

    def click_iphone_image(self):
        self.driver.find_element_by_xpath(self.iphone_image_xpath).click()

    def click_next_arrow(self):
        self.driver.find_element_by_xpath(self.next_arrow_xpath).click()

    def click_close_button(self):
        self.driver.find_element_by_xpath(self.close_button_xpath).click()

    def input_quantity(self, quantity):
        self.driver.find_element_by_xpath(self.input_quantity_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.input_quantity_textbox_xpath).send_keys(quantity)

    def click_add_to_cart_button(self):
        self.driver.find_element_by_xpath(self.add_to_cart_xpath).click()