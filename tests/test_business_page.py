from base.base_test import BaseTest


class TestBusinessPage(BaseTest):
    
    def test_radio_presonal(self):
        self.business_page_actions.bp.open()
        self.business_page_actions.open_radio_personal()