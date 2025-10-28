# ⚙️ 1. tell() — Get Current Cursor Position
# Open file in write mode
f = open("demo.txt", "w")

f.write("Hello Python!")
print("Current position after writing:", f.tell())  # ➜ Position after writing

f.close()



# ⚙️ 2. seek(offset, from_where) — Move Cursor to Specific Position
# Open file in read mode
f = open("demo.txt", "r")

print("Initial position:", f.tell())   # Usually 0 (start of file)


f.seek(0, 2)  # Move to end of file
print("Position after seek(0, 2):", f.tell())

# Move cursor to 6th byte (after "Hello ")
f.seek(6)
print("Position after seek(6):", f.tell())

# Read remaining content from current position
print("Remaining text:", f.read())

f.close()



# ⚙️ 3. truncate(size) — Cut the File to a Specific Length
# Open file in write+read mode
# f = open("demo.txt", "r+")

with open("demo.txt","r+") as f:
    print("Original content:", f.read())

    # Truncate the file to 5 bytes only
    f.truncate(5)

    f.seek(0)  # Move cursor to start to read again
    print("After truncate:", f.read())

# f.close()


# 🧰 Combined Example — seek(), tell(), truncate()
# Create file and write text
with open("example.txt", "w+") as f:
    f.write("Python File Handling Example")

    # Move cursor back to start
    f.seek(0)
    print("File content:", f.read())

    # Move cursor to 7th byte
    f.seek(7)
    print("\nCursor moved to position:", f.tell())

    # Truncate file to 12 bytes
    f.truncate(12)
    f.seek(0)
    print("After truncation:", f.read())