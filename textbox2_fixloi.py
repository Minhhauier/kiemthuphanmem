from playwright.sync_api import sync_playwright
import openpyxl


def ktrasualoi():
    with sync_playwright() as p:
        br=p.chromium.launch(headless=False)
        page=br.new_page()
        page.goto("https://demoqa.com")
        page.locator("text=Elements").click()
        page.locator("text=Text Box").click()
        page.locator("#userName").fill("Nv A")
        page.locator('#userEmail').fill("abc@gmail.com")
        page.locator('#currentAddress').fill("Hanoi")
        page.locator('#permanentAddress').fill("Hanam")
        page.locator('text=submit').click()


        out_name = page.locator('#name')
        out_email = page.locator('#email')
        out_curadd = page.locator("p#currentAddress")
        out_peradd = page.locator("p#permanentAddress")

        ketqua = {
            "Name ": out_name.inner_text(),
            "Email": out_email.inner_text(),
            "Current address": out_curadd.inner_text(),
            "Permanent address": out_peradd.inner_text()
        }

        row = 2
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet["A1"] = "Field"
        sheet["B1"] = "Result"
        row = 2
        for field, value in ketqua.items():
            sheet[f"A{row}"] = field
            sheet[f"B{row}"] = value
            row += 1
        test_passed = True
        for field, value in ketqua.items():
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
        br.close()

ktrasualoi()

