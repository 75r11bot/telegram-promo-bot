from telethon import TelegramClient, events
from bot.config import API_ID, API_HASH, PHONE_NUMBER, SESSION_NAME
from bot.promo_extractor import extract_promo_codes

async def main():
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    await client.start(phone=PHONE_NUMBER)

    @client.on(events.NewMessage)
    async def handler(event):
        codes = extract_promo_codes(event.raw_text)
        if codes:
            print('Extracted codes:', codes)
            # TODO: Send to Playwright processor

    print('Bot is running...')
    await client.run_until_disconnected()

def start_bot():
    import asyncio
    asyncio.run(main())