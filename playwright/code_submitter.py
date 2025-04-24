# playwright/code_submitter.py

import asyncio
import json
from playwright.async_api import Page
from playwright.async_api import Browser

async def submit_code(
    browser: Browser,
    player_id: str,
    promo_code: str,
    endpoint: str,
    site: str,
    key: str,
    token: str,
    host_url: str
):
    context = await browser.new_context()
    page = await context.new_page()

    url = f"{host_url}/client?player_id={player_id}&promo_code={promo_code}&site={site}"
    payload = {"key": key}
    headers = {
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Authorization": token,
        "Origin": host_url,
        "Referer": f"{host_url}/",
    }

    print(f"🚀 Sending request for player {player_id} with code {promo_code} to {endpoint}")
    await page.goto("about:blank")
    await page.evaluate(
        """async ({ url, payload, headers }) => {
            const res = await fetch(url, {
                method: "POST",
                headers,
                body: JSON.stringify(payload)
            });
            const data = await res.json();
            console.log("✅ Response:", data);
        }""",
        {
            "url": url,
            "payload": payload,
            "headers": headers
        }
    )
    await page.close()
    await context.close()
