import allure
import re 
from faker import Faker

from playwright.sync_api import expect
from page.locators.pre_auth.locators import BusinessPage
from config.links import Links

fake = Faker()

class BusinessPageActions:

    def __init__(self, page):
        self.bp = BusinessPage(page)

    @allure.step("Click 'Personal' radio button and verify URL")
    def open_radio_personal(self):
        self.bp.button_radio_personal.click()
        expect(self.bp.page).to_have_url(f'{Links.PERSONAL_PAGE}')
        return self

    @allure.step("Click 'Pricing' link and verify URL")
    def open_pricing(self):
        self.bp.button_pricing.click()
        expect(self.bp.page).to_have_url(f'{Links.PRICING_PAGE}')
        return self

    @allure.step("Click 'Sign In' link and verify URL")
    def open_sign_in(self):
        self.bp.button_sign_in.click()
        expected_urls = f"{Links.LOGIN_PAGE}|{Links.ACCOUNTS_PAGE}"
        expect(self.bp.page).to_have_url(re.compile(expected_urls))
        return self
    
    @allure.step("Click 'Open an account' and verify URL")
    def open_account(self):
        self.bp.button_open_an_account.click()
        expect(self.bp.page).to_have_url(f'{Links.BUSINESS_REGISTER}')
        return self

    @allure.step("Click 'Request the demo' and verify Calendly iframe is visible")
    def open_requests(self):
        self.bp.button_request_the_demo.click()
        iframe = self.bp.page.frame_locator("iframe[title=\"Calendly Scheduling Page\"]")
        expect(iframe.get_by_role("heading", name="Elisa Igumnova")).to_be_visible(timeout = 10000)
        return self
    
    @allure.step("Click 'Send an e-mail' and verify mailto link")
    def open_send_email(self):
        expect(self.bp.button_send_an_email).to_have_attribute("href", "mailto:team@unovay.com")
        return self
    
    @allure.step("Click 'Email' in footer and verify mailto link")
    def open_email_footer(self):
        expect(self.bp.button_send_an_email).to_have_attribute("href", "mailto:team@unovay.com")
        return self

    @allure.step("Click 'Terms of Service' link and verify PDF URL")
    def open_terms(self):
        expect(self.bp.button_terms).to_have_attribute("href", "https://s-stage.unovay.com/docs/terms_and_conditions.pdf")
        with self.bp.page.context.expect_page() as new_page_info:
            self.bp.button_terms.click()
        new_page = new_page_info.value
        assert new_page.url == "https://s-stage.unovay.com/docs/terms_and_conditions.pdf"
        return self

    @allure.step("Click 'Refund Policy' link and verify PDF URL")
    def open_refund(self):
        expect(self.bp.button_refund).to_have_attribute("href", "https://s-stage.unovay.com/docs/refund_policy.pdf")
        with self.bp.page.context.expect_page() as new_page_info:
            self.bp.button_refund.click()
        new_page = new_page_info.value
        assert new_page.url == "https://s-stage.unovay.com/docs/refund_policy.pdf"
        return self

    @allure.step("Click 'Complaint Policy' link and verify PDF URL")
    def open_complaint(self):
        expect(self.bp.button_complaint).to_have_attribute("href", "https://s-stage.unovay.com/docs/complaint_policy.pdf")
        with self.bp.page.context.expect_page() as new_page_info:
            self.bp.button_complaint.click()
        new_page = new_page_info.value
        assert new_page.url == "https://s-stage.unovay.com/docs/complaint_policy.pdf"
        return self
    
    @allure.step("Test Calculator")
    def calculator_operation(self):
        with allure.step("Click Button Send"):
            self.bp.button_send.click()
    
        with allure.step("Select send option"):
            self.bp.option_send.click()
    
        with allure.step("Click Button Gets"):
            self.bp.button_gets.click()
    
        with allure.step("Select gets option"):
            self.bp.option_gets.click()
    
        with allure.step("Fill input with random number digits = 5"):
            self.bp.input_send.fill(f"{fake.random_number(digits=5)}")
    
        with allure.step("Verify fees are visible"):
            expect(self.bp.floating_rate).to_be_visible()
            expect(self.bp.transfer_fee).to_be_visible()
            expect(self.bp.exchange_fee).to_be_visible()
        return self