from selenium import webdriver
import time
import random
import unittest
import HtmlTestRunner
from Pages.HomePage import HomePage
from Pages.PhonePDAPage import PhonePDAPage
from Pages.iPhonePage import iPhonePage
from Pages.LaptopPage import LaptopPage
from Pages.HPpage import HPpage
from Pages.CheckoutPage import CheckoutPage
from Pages.SuccessPage import SuccessPage

class EcomTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # initialize webdriver
        cls.driver = webdriver.Chrome("C:/Users/flavi/PycharmProjects/eCommerceAutomationProject/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01(self):
        #Initialize driver and open URL
        driver = self.driver
        driver.get('http://tutorialsninja.com/demo/')

        #Initialize Home Page Object and click phone and pda option
        home = HomePage(driver)
        home.click_phone_pda_option()
        time.sleep(2)

        #Select iphone - quantity 2
        phone_pda = PhonePDAPage(driver)
        phone_pda.click_iphone_option()
        time.sleep(2)
        #See all images
        iphone = iPhonePage(driver)
        iphone.click_iphone_image()
        time.sleep(2)
        #Click next arrow 5 times
        for i in range(5):
            iphone.click_next_arrow()
            time.sleep(2)
        #Take screenshot of last image and close image
        driver.save_screenshot('C:/Users/flavi/PycharmProjects/eCommerceAutomationProject/Screenshots/'+'screenshot#'+str(random.randint(0,101))+'.png')
        iphone.click_close_button()
        time.sleep(2)
        #Add input quantity and add to cart
        iphone.input_quantity(2)
        time.sleep(2)
        #iphone.click_add_to_cart_button()
        #time.sleep(2)

        #Select laptop - quantity 1
        home.hover_laptop_notebook_option()
        home.click_show_all_laptop_notebook_option()
        time.sleep(2)
        #Select hp
        lap = LaptopPage(driver)
        lap.click_hp_option()
        #Once in hp page, scroll down
        hp = HPpage(driver)
        hp.scroll_to_add_to_cart_button()
        #Click calendar and choose date and add to cart
        hp.click_delivery_date_calendar()
        hp.change_delivery_date_calendar("31", "December 2022")
        hp.click_add_to_cart_button()

        #Checkout Process
        #Click cart and view cart
        home.click_cart_button()
        home.click_checkout_cart_button()
        #Completing checkout details
        cp = CheckoutPage(driver)
        cp.complete_checkout_options()
        cp.complete_billing_details('fname', 'lname', 'test@email.com', '5555555555', '123 ABC', 'TestCity', '12342', 'India', 'Goa')
        cp.complete_delivery_method()
        cp.complete_payment_method()
        cp.confirm_order_method()
        #Final Message
        sp = SuccessPage(driver)
        sp.print_message()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
        #HtmlTestRunner.HTMLTestRunner(output="C:/Users/flavi/PycharmProjects/eCommerceAutomationProject/Reports")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/flavi/PycharmProjects/eCommerceAutomationProject/Reports"))

