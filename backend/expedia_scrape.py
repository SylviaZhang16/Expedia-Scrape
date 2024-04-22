# Chinh Nguyen

# Importing required modules: time for delays and playwright for automated web interactions.
import time
from playwright.sync_api import sync_playwright

# Initiating a playwright context to automate browser-related tasks.
with sync_playwright() as pw:
    # Launching a Firefox browser in headless mode (without a visible UI).
    browser = pw.chromium.launch(headless=True)

    # Opening a new browser page/tab.
    page = browser.new_page()
    # Navigating to the Expedia hotel search URL with specific search parameters.
    page.goto('https://www.expedia.com/Hotel-Search?destination=Boston%20(and%20vicinity),%20Massachusetts,%20United%20States%20of%20America&regionId=178239&latLong=42.359355,-71.059785&flexibility=0_DAY&d1=2024-04-23&startDate=2024-04-23&d2=2024-04-27&endDate=2024-04-27&adults=2&rooms=1')
    
    # Pausing the script for 2 seconds to allow the page to load.
    time.sleep(2)

    # Locating the "Show More" button on the page.
    show_more = page.locator("button", has_text="Show More")

    # Continuously clicking the "Show More" button as long as it is visible, with a 5-second pause after each click to load more content.
    while show_more.is_visible() is True:
        show_more.click()
        time.sleep(5)

    # Locating all hotel card elements on the page using their data attribute.
    cards = page.locator('[data-stid="lodging-card-responsive"]').all()
    # Initializing a list to store hotel data.
    hotels = []

    # Looping through each card element to extract hotel details.
    for card in cards: 
        # Locating the content section within each hotel card.
        content = card.locator('div.uitk-card-content-section')
        # Extracting the hotel name.
        title = content.locator('h3').text_content()

        # Checking visibility of the price element and extracting it if present.
        if content.locator('div.uitk-type-500').is_visible():
            price = content.locator('div.uitk-type-500').text_content()
        else:
            price = False  # Assigning False if price is not available.

        # Creating a dictionary for each hotel with its name and price.
        hotel = {
            'name': title,
            'price': price
        }
      
        # Adding the dictionary to the hotels list.
        hotels.append(hotel)
    
    # Printing the list of hotels with their names and prices.
    print(hotels)

    # Closing the browser after the task completion.
    browser.close()