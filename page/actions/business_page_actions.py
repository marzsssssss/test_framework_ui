from playwright.sync_api import expect
from page.ui.business_page import BusinessPage
from config.links import Links


class BusinessPageActions():

    def __init__(self, page):
        self.bp = BusinessPage(page)

    def open_radio_personal(self):
        self.bp.element_click(self.bp.button_radio_personal)
        expect(self.bp.page).to_have_url(f'{Links.PERSONAL_PAGE}')
        return self

    def open_pricing(self):
        self.bp.element_click(self.bp.button_pricing)
        expect(self.bp.page).to_have_url(f'{Links.PRICING_PAGE}')
        return self

    def open_sign_in(self):
        self.bp.element_click(self.bp.button_sign_in)
        expect(self.bp.page).to_have_url(f'{Links.LOGIN_PAGE}')
        return self
    
    def open_account(self):
        self.bp.element_click(self.bp.button_open_an_account)
        expect(self.bp.page).to_have_url(f'{Links.BUSINESS_REGISTER}')
        return self

    def open_requests(self):
        self.bp.element_click(self.bp.button_request_the_demo)
        iframe = self.bp.page.frame_locator("iframe[title=\"Calendly Scheduling Page\"]")
        expect(iframe.locator(".Pl9F4D0kOr1s0KUQ1VhD")).to_be_visible()
        return self

    def open_send_email(self):
        self.bp.element_click(self.bp.button_send_an_email)
        expect(self.bp.button_send_an_email).to_have_attribute("href", r"^mailto:.*@example\.com")
        return self

    def open_terms(self):
        self.bp.element_click(self.bp.button_terms)
        expect(self.bp.page).to_have_url(r".*/terms_and_conditions\.pdf$")
        return self

    def open_refund(self):
        self.bp.element_click(self.bp.button_refund)
        expect(self.bp.page).to_have_url(r".*/refund_policy\.pdf$")
        return self

    def open_complaint(self):
        self.bp.element_click(self.bp.button_complaint)
        expect(self.bp.page).to_have_url(r".*/complaint_policy\.pdf$")
        return self