import allure
import pytest

from base.base_test import BaseTest


@allure.feature('Test NavBar after auth')
class TestNavBar(BaseTest):

    @allure.title('Test Navbar')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_navbar(self):
        self.navbar_actions.navbar.open()
        self.navbar_actions.open_send_money()
        self.navbar_actions.navbar.open()
        self.navbar_actions.open_recipients()
        self.navbar_actions.navbar.open()
        self.navbar_actions.open_transactions()
        self.navbar_actions.navbar.open()
        self.navbar_actions.copy_id()
        self.navbar_actions.open_email()
        self.navbar_actions.open_host()
        self.navbar_actions.navbar.open()
        self.navbar_actions.open_legal()
        self.navbar_actions.open_terms()
        self.navbar_actions.open_privacy()
