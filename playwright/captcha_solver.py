# playwright/captcha_solver.py

import time
from playwright.async_api import Page

async def solve_captcha_if_present(page: Page) -> bool:
    try:
        # ตรวจสอบว่า CAPTCHA ปรากฏหรือไม่
        captcha_element = await page.query_selector('img.captcha')
        if captcha_element:
            print("🔐 CAPTCHA detected. Manual solve required.")
            # รอให้ผู้ใช้กรอก CAPTCHA เอง
            while True:
                value = await page.locator('input[name="captcha"]').input_value()
                if value.strip() != "":
                    break
                print("⏳ Waiting for CAPTCHA input...")
                time.sleep(1)
            return True
        else:
            print("✅ No CAPTCHA detected.")
            return False
    except Exception as e:
        print(f"⚠️ Error while checking CAPTCHA: {e}")
        return False
