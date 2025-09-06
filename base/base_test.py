import pytest

from page.actions.business_page_actions import BusinessPageActions



class BaseTest():

    business_page_actions: BusinessPageActions


    @pytest.fixture(autouse=True)
    def setup(self, request, page):
        request.cls.page = page
        request.cls.business_page_actions = BusinessPageActions(page)

