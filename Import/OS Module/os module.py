# ==========================================
# 📘 Python os Module Examples
# ==========================================
import os
import shutil

# ------------------------------------------
# 1️⃣ Get the current working directory (CWD)
# ------------------------------------------
current_dir = os.getcwd()
print("Current Working Directory:", current_dir)
# Example Output: C:\Users\Laraib\Desktop
#
# ------------------------------------------
# 2️⃣ Change the current working directory
# ------------------------------------------
# os.chdir(r"C:/Users\LaraibKhalid\OneDrive - Business Solutions & Services\Desktop\Laraib Data\SQA\Automation\Python-Practice\Import")
# print("Changed Directory:", os.getcwd())
# (Commented out to avoid error if path doesn’t exist)

# # ------------------------------------------
# # 3️⃣ List all files and folders in a directory
# # ------------------------------------------
print("\nFiles and Folders in current directory:")
for item in os.listdir(current_dir):
    print(" -", item)
# Output: shows all files/folders in that path

# # ------------------------------------------
# # 4️⃣ Create a new folder
# # ------------------------------------------
folder_name = "test_folder"
if not os.path.exists(folder_name):  # Check to avoid re-creation error
    os.mkdir(folder_name)
    print(f"\nFolder '{folder_name}' created successfully!")
else:
    print(f"\nFolder '{folder_name}' already exists!")
#
# # Create 100 folders named Tutorial 1, Tutorial 2, ..., Tutorial 100
# for i in range(0, 100):  # from 1 to 100
#     folders_name = f"Tutorial {i+1}"
#
#     # Check if the folder already exists
#     if not os.path.exists(folders_name):
#         os.mkdir(folders_name)
#         print(f"✅ Created folder: {folders_name}")
#     else:
#         print(f"⚠️ Folder already exists: {folders_name}")


# # ------------------------------------------
# # 5️⃣ Create nested directories
# # ------------------------------------------
# nested_path = "main_folder/sub_folder"
# os.makedirs(nested_path, exist_ok=True)  # exist_ok=True avoids error if exists
# print("Nested directories created:", nested_path)

# # ------------------------------------------
# # 6️⃣ Rename a file or folder
# # ------------------------------------------
# Suppose a file or folder exists named 'old_name'

# Create (or overwrite) a file
if not os.path.exists("example.txt"):
    file = open("example.txt", "w")   # 'w' means write mode
    file.write("This is a new file created using open().")
    file.close()  # Always close the file after writing

    print("✅ File created successfully!")
else:
    print("File already exist!")

#
# os.rename("old_name.txt", "new_name.txt")
# print("File renamed successfully!")

# # ------------------------------------------
# # 7️⃣ Remove a file or directory
# # ------------------------------------------
# os.remove("old_name.txt")        # Delete a file
# os.rmdir("test_folder")      # Delete an empty folder
# os.removedirs("main_folder/sub_folder")  # Delete nested empty folders

print(os.access(r"main_folder\sub_folder", os.W_OK))

#
# folder_path = r"main_folder\sub_folder"
#
# if os.path.exists(folder_path):
#     shutil.rmtree(folder_path)
#     print("Deleted folder successfully.")
# else:
#     print("Folder does not exist.")

# # ------------------------------------------
# # 8️⃣ Get environment variables
# # ------------------------------------------
# print("\nEnvironment Variables Example:")
# user = os.getenv("USERNAME") or os.getenv("USER")
# print("Current User:", user)
#
# # ------------------------------------------
# # 9️⃣ Join paths safely (cross-platform)
# # ------------------------------------------
path = os.path.join(current_dir, "Documents", "files")
print("\nJoined Path:", path)
# Output example: C:\Users\Laraib\Desktop\Documents\files

# # ------------------------------------------
# # 🔟 Split path into directory and file
# # ------------------------------------------
# file_path = os.path.join(current_dir, "example.txt")
# directory, file = os.path.split(file_path)
# print("\nDirectory:", directory)
# print("File:", file)

# # ------------------------------------------
# # 11️⃣ Check if path exists
# # ------------------------------------------
print("\nDoes 'test_folder' exist?", os.path.exists("test_folder"))
#
# # ------------------------------------------
# # 12️⃣ Check if path is a file or directory
# # ------------------------------------------
print("Is 'test_folder' a directory?", os.path.isdir("test_folder"))
print("Is 'example.txt' a file?", os.path.isfile("example.txt"))

# # ------------------------------------------
# # 13️⃣ Get file absolute path
# # ------------------------------------------
abs_path = os.path.abspath("test_folder")
print("\nAbsolute Path of test_folder:", abs_path)

# # ------------------------------------------
# # 14️⃣ Walk through directories (list all files/folders recursively)
# # ------------------------------------------
print("\nWalking through current directory:")
for root, dirs, files in os.walk(current_dir):
    print(f"\n📁 Directory: {root}")
    print("   Subfolders:", dirs)
    print("   Files:", files)
    # This loop goes through all levels of directories
    break  # remove break to go deeper

# # ------------------------------------------
# # ✅ Summary
# # ------------------------------------------
print("\n✅ Common os functions:")
print("""
os.getcwd()         → Get current working directory
os.chdir(path)      → Change directory
os.listdir(path)    → List files/folders
os.mkdir(name)      → Create a single directory
os.makedirs(path)   → Create nested directories
os.rename(src, dst) → Rename file/folder
os.remove(path)     → Delete file
os.rmdir(path)      → Delete folder (empty)
os.path.exists(p)   → Check if path exists
os.path.join(p1,p2) → Join paths
os.path.split(p)    → Split directory & file
os.path.isdir(p)    → Check if directory
os.path.isfile(p)   → Check if file
os.walk(path)       → Traverse folders recursively
""")
