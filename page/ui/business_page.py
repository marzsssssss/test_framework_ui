import allure

from base.base_page import BasePage
from config.links import Links
from page.ui.components.pre_auth.header import HeaderPreAuth
from page.ui.components.pre_auth.footer import FooterPreAuth

class BusinessPage(BasePage):

    PAGE_URL = Links.BUSINESS_PAGE

    def __init__(self, page):
        super().__init__(page)

        self.header = HeaderPreAuth(page)
        
        self.button_open_an_account = self.page.get_by_role("link", name="Open an account")
        self.button_request_the_demo = self.page.get_by_role("button", name="Request the demo")
        self.button_send_an_email = self.page.get_by_role("link", name="Send an e-mail")
        
        self.footer = FooterPreAuth(page)
    
    def element_click(self,element):
        element.click()