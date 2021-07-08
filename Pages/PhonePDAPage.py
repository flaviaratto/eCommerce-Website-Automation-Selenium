class PhonePDAPage():
    def __init__(self, driver):
        self.driver = driver
        self.iphone_xpath = "//a[normalize-space()='iPhone']"

    def click_iphone_option(self):
        self.driver.find_element_by_xpath(self.iphone_xpath).click()

