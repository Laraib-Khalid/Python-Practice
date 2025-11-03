import argparse
import requests


def download_file(url, local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
        # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return local_filename


parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("url", help="Url of the file to download")
# parser.add_argument("output", help="by which name do you want to save your file")
parser.add_argument("-o", "--output", type=str, help="Name of the file", default=None)

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.url)
print(args.output, type(args.output))
download_file(args.url, args.output)



# python argparse_function.py http://superkuh.com/pictures/3phladder.jpg -o ladder.jpg
# python python_filename url_address -o output_filename


# python python_filename url_address
# python argparse_function.py http://superkuh.com/pictures/3phladder.jpg



# ✅ This file demonstrates how to download a file using command-line arguments

# Example commands to run this script in terminal:

# 1) Download with custom output file name:
# python argparse_function.py http://superkuh.com/pictures/3phladder.jpg -o ladder.jpg
# ⬆️ The image will be saved as ladder.jpg

# 2) Download using the original filename from the URL:
# python argparse_function.py http://superkuh.com/pictures/3phladder.jpg
# ⬆️ The image will be saved as 3phladder.jpg (same name as in URL)

# Format:
# python python_filename URL -o output_filename (optional)
# python argparse_function.py url_address -o file_name
# python argparse_function.py url_address            # (no -o → use default filename)
