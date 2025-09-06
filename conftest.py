import pytest
from playwright.sync_api import sync_playwright


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
            }
        )
        page = context.new_page()
        request.cls.page = page
        yield page
        context.close()
        browser.close()
