import win32com.client as win32

# Open Excel
excel = win32.Dispatch("Excel.Application")
excel.Visible = True

# Create Workbook
wb = excel.Workbooks.Add()
sheet = wb.ActiveSheet

# Write Data
sheet.Cells(1, 1).Value = "Name"
sheet.Cells(1, 2).Value = "Marks"
sheet.Cells(2, 1).Value = "Laraib"
sheet.Cells(2, 2).Value = 95

# Save Excel File
wb.SaveAs(r"C:\Users\Public\pywin32_excel_demo.xlsx")
wb.Close()
excel.Quit()
