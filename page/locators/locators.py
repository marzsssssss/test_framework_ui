from base.base_page import BasePage
from config.links import Links


class NavBar(BasePage):

    PAGE_URL = Links.ACCOUNTS_PAGE

    def __init__(self, page):
        super().__init__(page)

        self.button_send_money = self.page.get_by_role('link', name = "Send Money")

        self.button_accounts = self.page.get_by_role('link', name = "Accounts")
        self.button_recipients = self.page.get_by_role('link', name = "Recipients")
        self.button_transaction= self.page.get_by_role('link', name = "Transactions")

        self.button_unovay_id = self.page.locator('.unovay-mr_1')
        self.pop_up_window = self.page.get_by_text('Unovay ID copied to clipboard', exact = True)

        self.button_terms = self.page.get_by_role('link', name = 'Terms of Service')
        self.button_privacy = self.page.get_by_role('link', name = 'Privacy Policy')
        self.button_legal= self.page.get_by_role('link', name = 'Legal')
        self.button_unovay_com = self.page.get_by_role('link', name = 'unovay.com', exact = True)
        self.button_mail_unovay = self.page.get_by_role('link', name = 'team@unovay.com', exact = True)

