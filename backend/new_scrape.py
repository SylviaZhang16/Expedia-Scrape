
from playwright.sync_api import sync_playwright
import time
from urllib.parse import quote_plus
from datetime import datetime


def fetch_hotels(destination, start_date, end_date):
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)  
        page = browser.new_page() 
        from urllib.parse import quote_plus
        destination_encoded = quote_plus(destination)
        url = f"https://www.expedia.com/Hotel-Search?destination={destination_encoded}&flexibility=0_DAY&d1={start_date}&startDate={start_date}&d2={end_date}&endDate={end_date}&adults=2&rooms=1"
        page.goto(url)
        time.sleep(2) 

        try:
            show_more = page.locator("text='Show More'")
            while show_more.is_visible():
                show_more.click()
                page.wait_for_load_state('networkidle')
        except Exception as e:
            print(f"Error clicking 'Show More': {e}")

        hotels = []
        cards = page.locator('[data-stid="lodging-card-responsive"]').all()
        print(f"Found {len(cards)} cards.")

        for card in cards:
            title = card.locator('h3:not(.is-visually-hidden)').text_content()  
            price_locator = card.locator('div[data-test-id="price-summary-message-line"] div.uitk-type-200:has-text("total")')
            price= price_locator.text_content() if price_locator.is_visible() else 'N/A'
            image_locator = card.locator("figure.uitk-image img.uitk-image-media").first
            # image_url = image_locator.get_attribute('src') if image_locator.is_visible() else 'default-image.jpg'
            if image_locator.is_visible():
                image_url = image_locator.get_attribute('src')
            else:
                image_locator.wait_for(state="visible")
                image_url = image_locator.get_attribute('src') if image_locator.is_visible() else 'default-image.jpg'

            hotel = {'name': title, 'image_url': image_url, 'price': price}
            # hotel = {'name': title,  'price': price}
            hotels.append(hotel)
            if len(hotels) >= 15:
                break
        for hotel in hotels:
            print(hotel)

        browser.close() 

        return hotels



if __name__ == '__main__':
    fetch_hotels()