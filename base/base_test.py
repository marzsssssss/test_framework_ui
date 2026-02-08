import pytest

from page.actions.pre_auth.business_page_actions import BusinessPageActions
from page.actions.nav_bar_actions import NavBarActions

class BaseTest():

    business_page_actions: BusinessPageActions
    navbar_actions: NavBarActions


    @pytest.fixture(autouse=True)
    def setup(self, request, page):
        request.cls.page = page
        request.cls.business_page_actions = BusinessPageActions(page)
        request.cls.navbar_actions = NavBarActions(page)
