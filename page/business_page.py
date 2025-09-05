import allure
from base.base_page import BasePage
from config.links import Links
from playwright.sync_api import expect

class BusinessPage(BasePage):

    PAGE_URL = Links.BUSINESS_PAGE

    def __init__(self, page):
        super().__init__(page)
        # Header
        self.button_radio_personal = self.page.get_by_role("radio", name="Personal")
        self.button_pricing = self.page.get_by_role("link", name="Pricing")
        self.button_sign_in = self.page.get_by_role("link", name="Sign In")


        self.button_open_an_account = self.page.get_by_role("link", name="Open an account")
        self.button_request_the_demo = self.page.get_by_role("button", name="Request the demo")
        self.button_send_an_email = self.page.get_by_role("link", name="Send an e-mail")


        #Footer
        self.button_terms = self.page.get_by_role("link", name="Terms of Service")
        self.button_refund = self.page.get_by_role("link", name="Refund Policy")
        self.button_complaint = self.page.get_by_role("link", name="Complaint Policy")
    
    
    def open_radio_personal(self):
        self.button_radio_personal.click()
        self.page.wait_for_url(f'{Links.PERSONAL_PAGE}')

    def open_pricing(self):
        self.button_pricing.click()
        self.page.wait_for_url(f'{Links.PRICING_PAGE}')

    def open_sign_in(self):
        self.button_sign_in.click()
        self.page.wait_for_url(f'{Links.LOGIN_PAGE}')
    
    def open_account(self):
        self.button_open_an_account.click()
        self.page.wait_for_url(f'{Links.BUSINESS_REGISTER}')

    def open_requests(self):
        self.button_request_the_demo.click()
        iframe = self.page.frame_locator("iframe[title=\"Calendly Scheduling Page\"]")
        expect(iframe.locator(".Pl9F4D0kOr1s0KUQ1VhD")).to_be_visible()
    
