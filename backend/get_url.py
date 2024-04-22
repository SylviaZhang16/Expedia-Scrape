from playwright.sync_api import sync_playwright

def get_expedia_url(destination, check_in_date, check_out_date, adults, rooms):
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)  
        page = browser.new_page()
        
        page.goto("https://www.expedia.com/")
        
        page.fill("input[aria-label='Going to']", destination)
        page.press("input[aria-label='Going to']", "Enter")
        
        page.fill("input[id='d1-btn']", check_in_date)
        page.fill("input[id='d2-btn']", check_out_date)
        

        page.click("button[type='submit']") 
        page.wait_for_load_state('networkidle')


        current_url = page.url
        print("Generated URL:", current_url)
        
        browser.close()
        return current_url