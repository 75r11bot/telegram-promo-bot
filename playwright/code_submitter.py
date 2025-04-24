# playwright/code_submitter.py

import os
import time
from playwright.sync_api import sync_playwright

def submit_promo_code(code: str, url: str = "https://example.com/promo") -> str:
    """
    เปิดเว็บที่กำหนด, กรอกรหัสโปรโมชัน, ส่งฟอร์ม และบันทึกวิดีโอ
    คืน path ของวิดีโอ
    """
    video_dir = "videos"
    os.makedirs(video_dir, exist_ok=True)
    timestamp = int(time.time())
    video_path = os.path.join(video_dir, f"{code}_{timestamp}.webm")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir=video_dir,
            record_video_size={"width": 1280, "height": 720},
        )
        page = context.new_page()

        page.goto(url)

        # 🔁 ปรับ selector ให้ตรงกับเว็บจริง
        page.fill('input[name="promo_code"]', code)
        page.click('button[type="submit"]')

        page.wait_for_timeout(5000)  # รอให้โหลดหรือ show result

        context.close()
        browser.close()

    return os.path.abspath(video_path)
