import asyncio

from playwright.async_api import async_playwright, Playwright


async def run(playwright: Playwright):
    browser = await playwright.chromium.launch(headless=False)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/automation-practice-form",timeout=60000)
    await page.wait_for_load_state("load")
    await page.locator("#firstName").fill("Van")
    await page.locator("#lastName").fill("A")
    await page.locator("#userEmail").fill("nguyenvana@gmail.com")
    await page.locator('label[for="gender-radio-1"]').click()
    await page.locator("#userNumber").fill("0123456789")
    await page.locator("#dateOfBirthInput").click()
    await page.locator(".react-datepicker__month-select").select_option("7")
    await page.locator(".react-datepicker__year-select").select_option("1990")
    await page.locator('.react-datepicker__day--015').click()
    await page.locator("#subjectsInput").type("E")
    await page.locator(".subjects-auto-complete__menu").locator("text=English").click()
    await page.locator('label[for="hobbies-checkbox-1"]').click()
    await page.locator('label[for="hobbies-checkbox-2"]').click()
    await page.locator("#currentAddress").fill("xuanPhuong St, TuLiem")
    await page.locator("#submit").click()
    assert page.locator(".modal-title").text_content() == "Thanks for submitting the form"
    await page.close()


async def main():
    async with async_playwright() as p:
        await run(p)

asyncio.run(main())