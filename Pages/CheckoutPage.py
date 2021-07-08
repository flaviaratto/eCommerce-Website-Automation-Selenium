import time

from selenium.webdriver.support.select import Select


class CheckoutPage():
    def __init__(self, driver):
        self.driver = driver
        self.guest_checkout_radiobutton_xpath = "//input[@value='guest']"
        self.continue1_xpath = "//input[@id='button-account']"
        self.firstname_xpath = "//input[@id='input-payment-firstname']"
        self.lastname_xpath = "//input[@id='input-payment-lastname']"
        self.email_xpath = "//input[@id='input-payment-email']"
        self.telephone_xpath = "//input[@id='input-payment-telephone']"
        self.address1_xpath = "//input[@id='input-payment-address-1']"
        self.city_xpath = "//input[@id='input-payment-city']"
        self.postcode_xpath = "//input[@id='input-payment-postcode']"
        self.country_xpath = "//select[@id='input-payment-country']"
        self.region_xpath = "//select[@id='input-payment-zone']"
        self.continue2_xpath = "//input[@id='button-guest']"
        self.continue4_xpath = "//input[@id='button-shipping-method']"
        self.tnc_xpath = "//input[@name='agree']"
        self.continue5_xpath = "//input[@id='button-payment-method']"
        self.total_xpath = "//table[@class='table table-bordered table-hover']/tfoot/tr[3]/td[2]"
        self.confirmorder_xpath = "//input[@id='button-confirm']"

    def complete_checkout_options(self):
        self.driver.find_element_by_xpath(self.guest_checkout_radiobutton_xpath).click()
        self.driver.find_element_by_xpath(self.continue1_xpath).click()

    def enter_billing_details(self, fname, lname, email, tele, add1, city, pcode, country, state):
        self.driver.find_element_by_xpath(self.firstname_xpath).clear()
        self.driver.find_element_by_xpath(self.firstname_xpath).send_keys(fname)
        self.driver.find_element_by_xpath(self.lastname_xpath).clear()
        self.driver.find_element_by_xpath(self.lastname_xpath).send_keys(lname)
        self.driver.find_element_by_xpath(self.email_xpath).clear()
        self.driver.find_element_by_xpath(self.email_xpath).send_keys(email)
        self.driver.find_element_by_xpath(self.telephone_xpath).clear()
        self.driver.find_element_by_xpath(self.telephone_xpath).send_keys(tele)
        self.driver.find_element_by_xpath(self.address1_xpath).clear()
        self.driver.find_element_by_xpath(self.address1_xpath).send_keys(add1)
        self.driver.find_element_by_xpath(self.city_xpath).clear()
        self.driver.find_element_by_xpath(self.city_xpath).send_keys(city)
        self.driver.find_element_by_xpath(self.postcode_xpath).clear()
        self.driver.find_element_by_xpath(self.postcode_xpath).send_keys(pcode)

        country_val = self.driver.find_element_by_xpath(self.country_xpath)
        dropdown1 = Select(country_val)
        dropdown1.select_by_visible_text(country)

        state_val = self.driver.find_element_by_xpath(self.region_xpath)
        dropdown2 = Select(state_val)
        dropdown2.select_by_visible_text(state)

    def complete_billing_details(self, fname, lname, email, tele, add1, city, pcode, country, state):
        self.enter_billing_details(fname, lname, email, tele, add1, city, pcode, country, state)
        self.driver.find_element_by_xpath(self.continue2_xpath).click()

    def complete_delivery_method(self):
        self.driver.find_element_by_xpath(self.continue4_xpath).click()

    def complete_payment_method(self):
        self.driver.find_element_by_xpath(self.tnc_xpath).click()
        self.driver.find_element_by_xpath(self.continue5_xpath).click()

    def confirm_order_method(self):
        #self.total_amount = self.driver.find_element_by_xpath(self.total_xpath)
        #print("Total amount is: "+self.total_amount.text)
        self.driver.find_element_by_xpath(self.confirmorder_xpath).click()

