from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/")
    page.wait_for_load_state("load")
    elements = page.get_by_text("Elements")
    elements.click()
    print("Elements: ", page.url)
    page.close()
