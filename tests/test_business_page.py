import allure
import pytest

from base.base_test import BaseTest

@allure.feature('Business Page')
class TestBusinessPage(BaseTest):
    
    @allure.title('Switch radio personal')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_radio_personal(self):
        self.business_page_actions.bp.open()
        self.business_page_actions.open_radio_personal()