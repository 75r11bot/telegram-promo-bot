# playwright/promo_apply.py

from playwright.sync_api import sync_playwright

chat_url_mapping = {
    "789BET-TH": "https://freecode.06789bet.com/",
    "Jun88TH": "https://freecode.8878388.com/",
}

def run_playwright_flow(code: str, chat_title: str):
    url = chat_url_mapping.get(chat_title)
    if not url:
        print(f"[ERROR] Unknown chat title: {chat_title}")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        print(f"[Playwright] Navigated to: {url}")

        try:
            page.fill("input[name='promo_code']", code)
            page.click("button[type='submit']")
            print(f"[Playwright] Submitted code: {code}")
            page.wait_for_timeout(3000)
        except Exception as e:
            print(f"[Playwright ERROR] {e}")
        finally:
            browser.close()