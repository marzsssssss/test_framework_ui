import os
import pytest
from playwright.sync_api import sync_playwright, expect
from dotenv import load_dotenv

from config.links import Links

load_dotenv()

@pytest.fixture(scope="session", autouse=True)
def auth():
    with sync_playwright() as pl:
        browser = pl.chromium.launch(headless=False) 
        context = browser.new_context(
            locale='en-US',
            timezone_id='America/New_York',
            geolocation={'longitude': -74.006, 'latitude': 40.7128},
            permissions=['geolocation'])
        page = context.new_page()
        page.goto(f"{Links.HOST}")
        page.get_by_role("link", name="Sign In").click()
        page.get_by_role("textbox", name="+60 000 000").click()
        page.get_by_role("textbox", name="+60 000 000").fill(f"{os.getenv('TEST_PHONE')}")
        page.get_by_role("button", name="Send code").click()
        page.get_by_role("textbox", name="Code").fill("999999")
        page.get_by_role("button", name="Submit", exact=True).click()
        expect(page).to_have_url(f"{Links.ACCOUNTS_PAGE}")
        context.storage_state(path="config/auth.json")
        browser.close()

@pytest.fixture(scope='function', autouse=True)
def page(request):
    with sync_playwright() as pl:
        browser = pl.chromium.launch(
            headless=False,
            args=[
                '--no-sandbox',
                '--disable-dev-shm-usage',
            ]
        )
        context = browser.new_context(
            viewport={
                'width':1920,
                'height':1080
            },
            storage_state='config/auth.json',
            locale='en-US',
            timezone_id='America/New_York',
            geolocation={'longitude': -74.006, 'latitude': 40.7128},
            permissions=['geolocation']
        )
        page = context.new_page()
        request.cls.page = page
        yield page
        context.close()
        browser.close()
