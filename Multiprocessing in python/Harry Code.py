# import concurrent.futures
# import requests
#
#
# def downloadFile(url, name):
#     print(f"Started Downloading {name}")
#     response = requests.get(url)
#     open(f"files/file{name}.jpg", "wb").write(response.content)
#     print(f"Finished Downloading {name}")
#
#
# url = "https://picsum.photos/2000/3000"
# # pros = []
# # for i in range(50):
# #   # downloadFile(url, i)
# #   p = multiprocessing.Process(target=downloadFile, args=[url, i])
# #   p.start()
# #   pros.append(p)
#
# # for p in pros:
# #   p.join()
# if __name__ == "__main__":
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         l1 = [url for i in range(60)]
#         l2 = [i for i in range(60)]
#         results = executor.map(downloadFile, l1, l2)
#         for r in results:
#             print(r)



print("-" * 50)


# Creating a process
import multiprocessing
def my_func():
  print("Hello from process", multiprocessing.current_process().name)
  process = multiprocessing.Process(target=my_func)
  process.start()
  process.join()


# Creating a pool of worker processes
from multiprocessing import Pool

def process_task(task):
    # Do some work here
    print("Task processed:", task)

if __name__ == '__main__':
    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    with Pool(processes=4) as pool:
        results = pool.map(process_task, tasks)