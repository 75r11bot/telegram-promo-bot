# placeholder for Playwright automation logic
# playwright/promo_apply.py

from playwright.sync_api import sync_playwright
import os
from datetime import datetime
from playwright.code_submitter import submit_promo_code
path = submit_promo_code("WgeUm7COufW", "https://example.com/promo")
print("Video saved to:", path)


def apply_promo_code(code: str, url: str = "https://example.com/promo"):
    video_dir = "videos"
    os.makedirs(video_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    video_path = os.path.join(video_dir, f"promo_{code}_{timestamp}.webm")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(record_video_dir=video_dir)
        page = context.new_page()

        try:
            page.goto(url)

            # รอจนกว่าฟอร์มรหัสโปรโมชั่นจะโหลด
            page.wait_for_selector('input[name="promo_code"]')

            # กรอกรหัสโปรโมชั่น
            page.fill('input[name="promo_code"]', code)

            # คลิกปุ่มส่งรหัสโปรโมชั่น
            page.click('button[type="submit"]')

            # รอให้แสดงผลลัพธ์ เช่นข้อความยืนยัน หรือผลลัพธ์อื่น
            page.wait_for_timeout(3000)

        except Exception as e:
            print(f"Error applying promo code {code}: {e}")
        finally:
            context.close()
            browser.close()

            print(f"✅ Promo code '{code}' processed and video saved to: {video_path}")
            return video_path
