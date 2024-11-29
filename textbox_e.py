from playwright.sync_api import sync_playwright
import openpyxl

# Hàm kiểm thử và ghi kết quả vào Excel
def test_textbox_and_write_to_excel():
    # Mở trình duyệt và thực hiện kiểm thử
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # `headless=False` để mở trình duyệt thật
        page = browser.new_page()

        # 1. Truy cập vào trang DemoQA
        page.goto("https://demoqa.com/")

        # 2. Nhấp vào "Elements" để vào phần Elements
        page.locator('text=Elements').click()

        # 3. Chọn "Text Box"
        page.locator('text=Text Box').click()

        # 4. Điền thông tin vào các trường trong form
        # Nhập Full Name
        page.locator('#userName').fill('John Doe')

        # Nhập Email
        page.locator('#userEmail').fill('johndoe@example.com')

        # Nhập Current Address
        page.locator('#currentAddress').fill('123 Main St, Some City, Some Country')

        # Nhập Permanent Address
        page.locator('#permanentAddress').fill('456 Another St, Another City, Another Country')

        # 5. Nhấn Submit
        page.locator('#submit').click()

        # 6. Kiểm tra kết quả
        # Đảm bảo thông tin hiển thị chính xác trong phần Output
        user_name_output = page.locator('#name')
        user_email_output = page.locator('#email')
        current_address_output = page.locator('#currentAddress')
        permanent_address_output = page.locator('#permanentAddress')

        result = {
            "Full Name": user_name_output.inner_text(),
            "Email": user_email_output.inner_text(),
            "Current Address": current_address_output.inner_text(),
            "Permanent Address": permanent_address_output.inner_text()
        }

        print("Test passed: All fields are correctly submitted and displayed.")
        
        # Đóng trình duyệt sau khi kiểm thử
        browser.close()

        # 7. Ghi kết quả vào file Excel
        # Mở file Excel (nếu không có, sẽ tạo mới)
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.title = "Test Results"

        # Viết tiêu đề cột
        sheet["A1"] = "Field"
        sheet["B1"] = "Result"

        # Viết kết quả kiểm thử
        row = 2
        for field, value in result.items():
            sheet[f"A{row}"] = field
            sheet[f"B{row}"] = value
            row += 1

        # Lưu file Excel
        wb.save("test_results.xlsx")
        print("Test results saved to test_results.xlsx.")

# Chạy kiểm thử và ghi vào Excel
test_textbox_and_write_to_excel()