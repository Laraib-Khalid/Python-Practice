import win32com.client as win32

# Open Word
word = win32.Dispatch("Word.Application")
word.Visible = True

# Create new document
doc = word.Documents.Add()

# Write text
doc.Content.Text = "Hello from Python using pywin32!\nThis is an automated Word document."

# Save document
doc.SaveAs(r"C:\Users\Public\pywin32_word_demo.docx")
doc.Close()
word.Quit()
