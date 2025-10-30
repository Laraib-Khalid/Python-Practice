import os

def clear_clutter(folder_path):
    """
    This function renames all files in the given folder
    so that files of the same type (.png, .jpg, .txt, etc.)
    are renamed sequentially as 1.png, 2.png, etc.
    """
    # Change working directory to target folder
    os.chdir(folder_path)

    # Get all files in the folder
    files = os.listdir(folder_path)

    # Create a dictionary to track numbering for each file type
    file_counter = {}

    for file in files:
        # Skip directories
        if os.path.isdir(file):
            continue

        # Split filename and extension
        name, ext = os.path.splitext(file)

        # Skip hidden or system files
        if ext == "":
            continue

        # # Remove leading dot (e.g., .png → png)
        ext = ext.lower()

        # Initialize counter for this extension
        if ext not in file_counter:
            file_counter[ext] = 1

        # Build new filename (e.g., 1.png, 2.png)
        new_name = f"{file_counter[ext]}{ext}"

        # Rename the file
        os.rename(file, new_name)

        print(f"Renamed: {file} → {new_name}")

        # Increment counter for that extension
        file_counter[ext] += 1

    print("\n✅ Clutter cleared successfully!")


# --------------------------
# Example usage
# --------------------------
# 👉 Replace this with your actual folder path
folder_path = r"C:\Users\LaraibKhalid\Downloads\Test"

clear_clutter(folder_path)
