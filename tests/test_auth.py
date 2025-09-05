from playwright.sync_api import sync_playwright
from config.links import Links

def test_run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) 
        context = browser.new_context()
        page = context.new_page()

        # Открываем страницу логина Grafana
        page.goto(f"{Links.HOST}")

        print("👉 Авторизуйся руками в открывшемся браузере, потом вернись в консоль и нажми Enter")
        input()

        # Сохраняем состояние в state.json
        context.storage_state(path="state.json")

        browser.close()

if __name__ == "__main__":
    test_run()