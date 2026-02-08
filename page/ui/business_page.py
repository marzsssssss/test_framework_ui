import allure

from base.base_page import BasePage
from config.links import Links

class BusinessPage(BasePage):

    PAGE_URL = Links.BUSINESS_PAGE

    def __init__(self, page):
        super().__init__(page)

        #HEADER
        self.button_radio_personal = self.page.get_by_role("radio", name="Personal")
        self.button_pricing = self.page.get_by_role("link", name="Pricing")
        self.button_sign_in = self.page.get_by_role("link", name="Sign In")

        #CALCULATOR
        #SEND
        self.button_send = self.page.get_by_text('You send')
        self.option_send = self.page.get_by_role("option", name="United States dollar USD")
        self.input_send = self.page.locator("input[name=\"currencyFrom\"]")

        #GETS
        self.button_gets = self.page.get_by_text('Recipient gets')
        self.option_gets = self.page.get_by_role("option", name="Euro EUR Euro")
        self.input_gets = self.page.locator("input[name=\"currencyTo\"]")

        #FEE

        self.floating_rate = self.page.get_by_text("Floating rate")
        self.transfer_fee= self.page.get_by_text("Transfer fee")
        self.exchange_fee = self.page.get_by_text("Exchange fee")
        
        self.button_open_an_account = self.page.get_by_role("link", name="Open an account")
        self.button_request_the_demo = self.page.get_by_role("button", name="Request the demo")
        self.button_send_an_email = self.page.get_by_role("link", name="Send an e-mail")
        
        # FOOTER
        self.email = self.page.get_by_text('team@unovay.com')
        self.button_terms = self.page.get_by_role("link", name="Terms of Service")
        self.button_refund = self.page.get_by_role("link", name="Refund Policy")
        self.button_complaint = self.page.get_by_role("link", name="Complaint Policy")
    
    def element_click(self,element):
        element.click()