from telethon import TelegramClient, events
import asyncio
import os
from playwright.promo_apply import apply_promo_code

from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("TELEGRAM_API_ID"))
API_HASH = os.getenv("TELEGRAM_API_HASH")
SESSION_NAME = "promo_session"  # สร้าง session file

# สร้าง client instance
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# รายการโฟลเดอร์หรือชื่อกลุ่มที่ต้องฟัง
titles = os.getenv("CHAT_TITLES", "").split(",")

TARGET_CHAT_TITLES = titles

@client.on(events.NewMessage)
async def handler(event):
    chat = await event.get_chat()
    if hasattr(chat, 'title') and chat.title in TARGET_CHAT_TITLES:
        text = event.raw_text
        print(f"[{chat.title}] New Message:\n{text}")

        # ดึงรหัสโปรโมชั่นจากข้อความ
        promo_codes = extract_promo_codes(text)
        for code in promo_codes:
            print(f"Applying code: {code}")
            await apply_promo_code(code)

def extract_promo_codes(text):
    import re
    return re.findall(r'\b[A-Za-z0-9]{6,12}\b', text)

async def main():
    print("Starting Telegram client...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
