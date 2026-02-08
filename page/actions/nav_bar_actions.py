import allure 

from playwright.sync_api import expect
from config.links import Links
from page.ui.nav_bar import NavBar


class NavBarActions:

    def __init__(self,page):
        self.navbar = NavBar(page)

    @allure.step('Open Send Money in Nav Bar')
    def open_send_money(self):
        self.navbar.button_send_money.click()
        expect(self.navbar.page).to_have_url(f"{Links.SEND_MONEY_TRANSFER_PAGE}")
        return self
    
    @allure.step('Open Accounts in Nav Bar')
    def open_accounts(self):
        self.navbar.button_accounts.click()
        expect(self.navbar.page).to_have_url(f'{Links.ACCOUNTS_PAGE}')
        return self
    
    @allure.step('Open Recipients in Nav Bar')
    def open_recipients(self):
        self.navbar.button_recipients.click()
        expect(self.navbar.page).to_have_url(f'{Links.RECIPIENTS_PAGE}')
        return self
    
    @allure.step('Open Transactions in Nav Bar')
    def open_transactions(self):
        self.navbar.button_transaction.click()
        expect(self.navbar.page).to_have_url(f'{Links.TRANSACTIONS_PAGE}')
        return self
    
    @allure.step('Open Accounts in Nav Bar')
    def copy_id(self):
        self.navbar.button_unovay_id.click()
        expect(self.navbar.pop_up_window).to_be_visible()
        return self
    
    @allure.step("Click 'Terms of Service' link and verify PDF URL")
    def open_terms(self):
        expect(self.navbar.button_terms).to_have_attribute("href", "https://s-stage.unovay.com/docs/terms_and_conditions.pdf")
        with self.navbar.page.context.expect_page() as new_page_info:
            self.navbar.button_terms.click()
        new_page = new_page_info.value
        assert new_page.url == "https://s-stage.unovay.com/docs/terms_and_conditions.pdf"
        return self

    @allure.step("Click 'Privacy Policy' link and verify PDF URL")
    def open_privacy(self):
        expect(self.navbar.button_privacy).to_have_attribute("href", "https://s-stage.unovay.com/docs/privacy_policy.pdf")
        with self.navbar.page.context.expect_page() as new_page_info:
            self.navbar.button_privacy.click()
        new_page = new_page_info.value
        assert new_page.url == "https://s-stage.unovay.com/docs/privacy_policy.pdf"
        return self

    @allure.step("Click 'Legal' link and verify PDF URL")
    def open_legal(self):
        expect(self.navbar.button_legal).to_have_attribute("href", "https://s-stage.unovay.com/docs/other_policies.pdf")
        with self.navbar.page.context.expect_page() as new_page_info:
            self.navbar.button_legal.click()
        new_page = new_page_info.value
        assert new_page.url == "https://s-stage.unovay.com/docs/other_policies.pdf"
        return self
    
    @allure.step('Open unovay.com')
    def open_host(self):
        self.navbar.button_unovay_com.click()
        expect(self.navbar.page).to_have_url(f'{Links.HOST}/')
        return self
    
    @allure.step('Open mailto')
    def open_email(self):
        expect(self.navbar.button_mail_unovay).to_have_attribute('href', 'mailto:team@unovay.com')
        return self