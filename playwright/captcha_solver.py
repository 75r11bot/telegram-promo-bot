# Placeholder for CAPTCHA solving logic
# playwright/captcha_solver.py

import base64
import requests
from playwright.sync_api import Page

OCR_API_URL = "http://localhost:8000/api/solve"  # ปรับ URL ให้ตรงกับ API OCR ที่ใช้งาน

def solve_captcha(page: Page, captcha_selector: str, input_selector: str) -> str:
    """
    ถ่ายภาพ CAPTCHA จาก selector ที่กำหนด, ส่งไป OCR API, แล้วกรอกค่าที่ได้
    """
    # ดึง base64 จาก CAPTCHA <img src="data:image/svg+xml;base64,...">
    captcha_element = page.query_selector(captcha_selector)
    src_data_url = captcha_element.get_attribute("src")

    if not src_data_url or not src_data_url.startswith("data:image/svg+xml;base64,"):
        raise ValueError("ไม่พบ CAPTCHA หรือ format ไม่ถูกต้อง")

    base64_data = src_data_url.split(",", 1)[1]

    # ส่งไปยัง OCR API
    response = requests.post(OCR_API_URL, json={"image_base64": base64_data})
    result = response.json()

    if "text" not in result:
        raise ValueError("OCR API ไม่สามารถอ่าน CAPTCHA ได้")

    captcha_text = result["text"]

    # กรอก CAPTCHA ที่ช่อง input ที่กำหนด
    page.fill(input_selector, captcha_text)

    return captcha_text
