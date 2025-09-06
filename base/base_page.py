import allure

from playwright.sync_api import sync_playwright, expect
from allure_commons.types import AttachmentType

class BasePage:

    def __init__(self, page):
        self.page = page

    def open(self):
         with allure.step(f'Open {self.PAGE_URL} page'):
            self.page.goto(self.PAGE_URL, timeout = 10000)

    def make_screenshot(self, screenshot_name: str):
        allure.attach(
            body = self.page.screenshot(),
            name = screenshot_name,
            attachment_type=AttachmentType.PNG
        )