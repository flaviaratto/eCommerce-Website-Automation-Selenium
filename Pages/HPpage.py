
class HPpage():
    def __init__(self, driver):
        self.driver = driver
        self.delivery_date_calendar_xpath = "//i[@class='fa fa-calendar']"
        self.add_to_cart_button_xpath = "//button[normalize-space()='Add to Cart']"

        self.cal_month_year_xpath = "//th[@class='picker-switch']"
        self.cal_right_arrow_xpath = "//div[@class='datepicker-days']//th[@class='next'][contains(text(),'›')]"
        self.cal_date_xpath = "//td[normalize-space()="

    def scroll_to_add_to_cart_button(self):
        self.driver.find_element_by_xpath(self.add_to_cart_button_xpath).location_once_scrolled_into_view

    def click_delivery_date_calendar(self):
        self.driver.find_element_by_xpath(self.delivery_date_calendar_xpath).click()

    def change_delivery_date_calendar(self, date, month_year):
        cal_my = self.driver.find_element_by_xpath(self.cal_month_year_xpath).text
        while month_year != cal_my:
            self.driver.find_element_by_xpath(self.cal_right_arrow_xpath).click()
            cal_my = self.driver.find_element_by_xpath(self.cal_month_year_xpath).text
        cal_date_xpath = self.cal_date_xpath+"'"+date+"']"
        self.driver.find_element_by_xpath(cal_date_xpath).click()

    def click_add_to_cart_button(self):
        self.driver.find_element_by_xpath(self.add_to_cart_button_xpath).click()


