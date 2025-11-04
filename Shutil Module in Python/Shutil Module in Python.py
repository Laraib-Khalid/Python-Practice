import shutil
import os
import stat

# Copy a single file: source → destination
shutil.copy("Sets Data/practice.py", "Sets Data/main2.py")

# Copy entire folder "../sets" into "Sets Data"
# (Creates a new folder inside "Sets Data" with all contents)
shutil.copytree("../sets", "Sets Data")

# Move a file: "practice.py" → rename/move it to "file.py"
shutil.move("Sets Data/practice.py", "file.py")

# Folder we want to delete
folder = r"Sets Data"

# Function to handle read-only files while deleting
# If a file/folder has read-only permissions, this makes it writable and retries delete
def remove_readonly(func, path, exc_info):
    os.chmod(path, stat.S_IWRITE)  # Change file permission → writable
    func(path)                     # Retry delete operation

# Delete folder if exists
if os.path.exists(folder):
    shutil.rmtree(folder, onerror=remove_readonly)  # Remove folder + all contents
    print("✅ Folder deleted successfully")
else:
     print("❌ Folder not found")

# Remove the moved/renamed file
os.remove("file.py")
