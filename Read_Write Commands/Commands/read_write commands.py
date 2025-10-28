# ✍️ 1. write() — Write Text to a File
# Open a file in write mode ('w')
# If file does not exist → it will be created
# If file already exists → it will be overwritten

f = open("sample.txt", "w")

# Write a single string to file
f.write("Hello Python!\n")
f.write("This is a file write example.\n")

f.close()  # Always close after writing


# 🧾 2. writelines() — Write Multiple Lines at Once
# Open file in write mode
f = open("lines.txt", "w")

# Create a list of strings
lines = ["First line\n", "Second line\n", "Third line\n"]

# Write all lines at once (must include '\n' manually)
f.writelines(lines)

f.close()



# 📖 3. read() — Read Entire File
# Open file in read mode
f = open("lines.txt", "r")

# Reads the entire content as a single string
content = f.read()
print(content)

f.close()




# 📜 4. readline() — Read One Line at a Time
f = open("lines.txt", "r")

line1 = f.readline()  # Reads first line
print("Line 1:", line1)

line2 = f.readline()  # Reads next line
print("Line 2:", line2)

f.close()


# 📚 5. readlines() — Read All Lines as a List
f = open("lines.txt", "r")

# Reads all lines and returns a list
lines = f.readlines()
print(lines)

f.close()



# 🧰 6. Using with open() — Automatic File Handling

# Using with is best practice (no need for close()):

with open("lines.txt", "r") as f:
    # You can use any method here
    for line in f:
        print(line.strip())  # strip() removes \n


# f = open('myfile.txt', 'w')

#         Harry Code
f = open('myfile.txt', 'r')
i = 0
while True:
  i = i + 1
  line = f.readline()
  if not line:
    break
  m1 = int(line.split(",")[0])
  m2 = int(line.split(",")[1])
  m3 = int(line.split(",")[2])
  print(f"Marks of student {i} in Maths is: {m1*2}")
  print(f"Marks of student {i} in English is: {m2*2}")
  print(f"Marks of student {i} in SST is: {m3*2}")

  print(line)




f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()


f = open('myfile3.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()





# ⚡ Summary Table
#
# | Method         | Description            | Returns | Example Use             |
# | -------------- | ---------------------- | ------- | ----------------------- |
# | `write()`      | Writes a single string | None    | `f.write("Hello")`      |
# | `writelines()` | Writes list of strings | None    | `f.writelines(lines)`   |
# | `read()`       | Reads entire file      | String  | `data = f.read()`       |
# | `readline()`   | Reads next line        | String  | `line = f.readline()`   |
# | `readlines()`  | Reads all lines        | List    | `lines = f.readlines()` |
