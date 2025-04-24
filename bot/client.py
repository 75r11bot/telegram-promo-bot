from telethon.sync import TelegramClient, events
import os
import re
import asyncio
import requests
from dotenv import load_dotenv
from playwright.async_api import async_playwright

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
SESSION_NAME = os.getenv("SESSION_NAME")
CHAT_TITLES = os.getenv("CHAT_TITLES", "").split("|")

players789bet = [
    "nus9331", "aroon11", "manus9331", "manuchai", "kaimook11",
    "koonogk", "wat3366", "preechar", "tong551122", "hin789bet"
]

playersj88 = [
    "nus9331", "aroon11", "manus9331", "manuchai", "manusj88", "kaimook11",
    "koonogk", "wat3366", "manusvip", "poiy88", "tata5511", "tong234", "goft22", "hunjun88"
]

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def submit_code_flow(code: str, url: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)

        try:
            await page.fill('input[placeholder="Enter code"]', code)
            await page.click("text=Confirm")
            print(f"✅ Submitted code: {code} to {url}")
            await page.wait_for_timeout(3000)
        except Exception as e:
            print(f"❌ Error submitting code '{code}':", e)

        await browser.close()

@client.on(events.NewMessage)
async def handler(event):
    chat_title = event.chat.title if event.chat else ""
    if chat_title not in CHAT_TITLES:
        return

    message = event.message.message
    print(f"📥 Message from {chat_title}: {message}")
    codes = re.findall(r"[A-Za-z0-9]{6,12}", message)

    if "789BET" in chat_title.upper():
        players = players789bet
        url = "https://freecode.06789bet.com/"
    elif "JUN88" in chat_title.upper():
        players = playersj88
        url = "https://freecode.8878388.com/"
    else:
        print("❌ Unsupported chat title")
        return

    for code in codes:
        for player in players:
            print(f"🚀 Submitting code '{code}' for player '{player}' on {url}")
            await submit_code_flow(code, url)


client.start(phone=PHONE_NUMBER)
print("✅ Telegram client started. Waiting for messages...")
client.run_until_disconnected()
