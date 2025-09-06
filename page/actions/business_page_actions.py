import allure
from playwright.sync_api import expect
from page.ui.business_page import BusinessPage
from config.links import Links

class BusinessPageActions:

    def __init__(self, page):
        self.bp = BusinessPage(page)

    @allure.step("Click 'Personal' radio button and verify URL")
    def open_radio_personal(self):
        self.bp.element_click(self.bp.header.button_radio_personal)
        expect(self.bp.page).to_have_url(f'{Links.PERSONAL_PAGE}')
        return self

    @allure.step("Click 'Pricing' link and verify URL")
    def open_pricing(self):
        self.bp.element_click(self.bp.header.button_pricing)
        expect(self.bp.page).to_have_url(f'{Links.PRICING_PAGE}')
        return self

    @allure.step("Click 'Sign In' link and verify URL")
    def open_sign_in(self):
        self.bp.element_click(self.bp.header.button_sign_in)
        expect(self.bp.page).to_have_url(f'{Links.LOGIN_PAGE}')
        return self
    
    @allure.step("Click 'Open an account' and verify URL")
    def open_account(self):
        self.bp.element_click(self.bp.button_open_an_account)
        expect(self.bp.page).to_have_url(f'{Links.BUSINESS_REGISTER}')
        return self

    @allure.step("Click 'Request the demo' and verify Calendly iframe is visible")
    def open_requests(self):
        self.bp.element_click(self.bp.button_request_the_demo)
        iframe = self.bp.page.frame_locator("iframe[title=\"Calendly Scheduling Page\"]")
        expect(iframe.locator(".Pl9F4D0kOr1s0KUQ1VhD")).to_be_visible()
        return self

    @allure.step("Click 'Send an e-mail' and verify mailto link")
    def open_send_email(self):
        self.bp.element_click(self.bp.button_send_an_email)
        expect(self.bp.button_send_an_email).to_have_attribute("href", r"^mailto:.*@example\.com")
        return self

    @allure.step("Click 'Terms of Service' link and verify PDF URL")
    def open_terms(self):
        self.bp.element_click(self.bp.footer.button_terms)
        expect(self.bp.page).to_have_url(r".*/terms_and_conditions\.pdf$")
        return self

    @allure.step("Click 'Refund Policy' link and verify PDF URL")
    def open_refund(self):
        self.bp.element_click(self.bp.footer.button_refund)
        expect(self.bp.page).to_have_url(r".*/refund_policy\.pdf$")
        return self

    @allure.step("Click 'Complaint Policy' link and verify PDF URL")
    def open_complaint(self):
        self.bp.element_click(self.bp.footer.button_complaint)
        expect(self.bp.page).to_have_url(r".*/complaint_policy\.pdf$")
        return self