# ✅ Example: Multithreading with proper comments
import threading
import time

# A simple function to simulate a task
def print_numbers():
    for i in range(1, 6):
        print(f"Numbers Thread: {i}")
        time.sleep(1)   # Simulate delay (I/O wait)

def print_letters():
    for ch in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letters Thread: {ch}")
        time.sleep(1)   # Simulate delay (I/O wait)

# Creating two threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Starting both threads
t1.start()
t2.start()

# Wait for both threads to finish before exiting program
t1.join()
t2.join()

print("✅ Both threads finished!")



# ✅ Real-world Example: Downloading multiple URLs together
import threading
import time

urls = ["file1.zip", "file2.zip", "file3.zip"]

def download(file):
    print(f"Downloading {file}...")
    time.sleep(2)  # Simulate download delay
    print(f"{file} downloaded ✅")

threads = []
for file in urls:
    t = threading.Thread(target=download, args=(file,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("✅ All downloads completed!")
