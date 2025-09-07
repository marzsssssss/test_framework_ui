import allure
import pytest

from base.base_test import BaseTest


@allure.feature('Test NavBar after auth')
class TestNavBar(BaseTest):

    @allure.title('Test Navbar')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_navbar(self):
        self.nav_bar_actions.navbar.open()
        self.nav_bar_actions.open_send_money()
        self.nav_bar_actions.navbar.open()