from playwright.sync_api import sync_playwright, expect


class BasePage:

    def __init__(self, page):
        self.page = page


    def open(self):
         self.page.goto(self.PAGE_URL, timeout = 10000)
