import win32com.client as win32

outlook = win32.Dispatch("Outlook.Application")
mail = outlook.CreateItem(0)  # 0 = Email

mail.To = "omar.moazzam@bssuniversal.com"
mail.Subject = "Test Email from Python"
mail.Body = "Hello,\n\nThis email was sent using Python pywin32.\n\nRegards,\nPython Script"

# Add attachment (optional)
mail.Attachments.Add(r"C:\Users\Public\pywin32_word_demo.docx")
mail.Attachments.Add(r"C:\Users\Public\pywin32_excel_demo.xlsx")

mail.Send()

print("Email sent!")


# import win32com.client as win32
# outlook = win32.Dispatch("Outlook.Application")
# print(outlook)
