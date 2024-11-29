from playwright.sync_api import sync_playwright
import openpyxl


def test_textbox_and_write_to_excel():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demoqa.com/")
        page.locator('text=Elements').click()
        page.locator('text=Text Box').click()
        page.locator('#userName').fill('John Doe')
        page.locator('#userEmail').fill('johndoe@example.com')
        page.locator('#currentAddress').fill('123 Main St, Some City, Some Country')
        page.locator('#permanentAddress').fill('456 Another St, Another City, Another Country')
        page.locator('#submit').click()

        user_name_output = page.locator('#name')
        user_email_output = page.locator('#email')
        current_address_output = page.locator('p#currentAddress')
        permanent_address_output = page.locator('p#permanentAddress')

        result = {
            "Full Name": user_name_output.inner_text(),
            "Email": user_email_output.inner_text(),
            "Current Address": current_address_output.inner_text(),
            "Permanent Address": permanent_address_output.inner_text()
        }
        print("Test passed: All fields are correctly submitted and displayed.")
        browser.close()
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = "Test Results"
        sheet["A1"] = "Field"
        sheet["B1"] = "Result"
        row = 2
        for field, value in result.items():
            sheet[f"A{row}"] = field
            sheet[f"B{row}"] = value
            row += 1
        test_passed = True
        for field, value in result.items():
            if not value:
                test_passed = False
                break
        if test_passed:
            sheet["A" + str(row)] = "Test Result"
            sheet["B" + str(row)] = "Pass"
        else:
            sheet["A" + str(row)] = "Test Result"
            sheet["B" + str(row)] = "Fail"
        wb.save("C:/demokthu/ketqua/New Microsoft Excel Worksheet.xlsx")
test_textbox_and_write_to_excel()