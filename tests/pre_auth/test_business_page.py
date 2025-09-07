import allure
import pytest

from base.base_test import BaseTest

@allure.feature('Business Page')
class TestBusinessPage(BaseTest):
    
    @allure.title('Test Bussiness Page')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_business_page(self):
        self.business_page_actions.bp.open()
        self.business_page_actions.open_radio_personal()
        self.business_page_actions.bp.open()
        self.business_page_actions.open_pricing()
        self.business_page_actions.bp.open()
        self.business_page_actions.open_sign_in()
        self.business_page_actions.bp.open()
        self.business_page_actions.open_account()
        self.business_page_actions.bp.open()
        self.business_page_actions.open_requests()
        self.business_page_actions.bp.open()
        self.business_page_actions.open_send_email()
        self.business_page_actions.bp.open()
        self.business_page_actions.open_email_footer()
        self.business_page_actions.bp.open()
        self.business_page_actions.open_terms()
        self.business_page_actions.bp.open()
        self.business_page_actions.open_refund()
        self.business_page_actions.bp.open()
        self.business_page_actions.open_complaint()

    @allure.title('Test Calculator')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_calculator(self):
        self.business_page_actions.bp.open()
        self.business_page_actions.calculator_operation()