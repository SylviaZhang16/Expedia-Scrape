from playwright.async_api import async_playwright
import asyncio
from urllib.parse import quote_plus
from datetime import datetime
from random import randint
from fake_useragent import UserAgent

DEFAULT_IMAGE_URL = 'https://t3.ftcdn.net/jpg/04/60/01/36/360_F_460013622_6xF8uN6ubMvLx0tAJECBHfKPoNOR5cRa.jpg'

async def fetch_hotels(destination, start_date, end_date):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        width = randint(1024, 1920)
        height = randint(768, 1080)
        ua = UserAgent()
        random_user_agent = ua.random
        context = await browser.new_context(
            user_agent=random_user_agent,
            # viewport={'width': width, 'height': height},
            permissions=["notifications"],
            extra_http_headers={"Accept-Language": "en-US,en;q=0.9"}
        )
        page = await context.new_page()

        destination_encoded = quote_plus(destination)
        url = f"https://www.expedia.com/Hotel-Search?destination={destination_encoded}&d1={start_date}&startDate={start_date}&d2={end_date}&endDate={end_date}&adults=2&rooms=1"
        await page.goto(url)
        await asyncio.sleep(8)

        # try:
        #     show_more = page.locator("text='Show More'")
        #     await show_more.click()
        #     # await page.wait_for_load_state('networkidle')
        #     await asyncio.sleep(5)
        # except Exception as e:
        #     print(f"Error clicking 'Show More': {e}")

        hotels = []
        cards = await page.locator('[data-stid="lodging-card-responsive"]').element_handles()
        print(f"Found {len(cards)} cards.")

        for card in cards[:100]:
            title_element = await card.query_selector('h3:not(.is-visually-hidden)')
            title = await title_element.text_content() if title_element else "No title"
            price_locator = await card.query_selector('div[data-test-id="price-summary-message-line"] div.uitk-type-200:has-text("total")')
            price = await price_locator.text_content() if price_locator else 'N/A'
            image_locator = await card.query_selector("figure.uitk-image img.uitk-image-media")
            image_url = await image_locator.get_attribute('src') if image_locator else DEFAULT_IMAGE_URL

            hotel = {'name': title, 'image_url': image_url, 'price': price}
            hotels.append(hotel)
            # if len(hotels) >= 15:
            #     break
        for hotel in hotels:
            print(hotel)

        await browser.close()
        return hotels

if __name__ == '__main__':
    asyncio.run(fetch_hotels('New York', '2024-04-23', '2024-04-27'))