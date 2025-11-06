# # ✅ Example 1: Basic Multiprocessing
# # 🔹 Run a function in multiple processes
# from multiprocessing import Process
# import time
#
# def task(name):
#     print(f"Process {name} started")
#     time.sleep(2)
#     print(f"Process {name} finished")
#
# if __name__ == "__main__":
#     p1 = Process(target=task, args=("A",))
#     p2 = Process(target=task, args=("B",))
#
#     p1.start()  # Start Process A
#     p2.start()  # Start Process B
#
#     p1.join()   # Wait for Process A to finish
#     p2.join()   # Wait for Process B to finish
#
#     print("✅ Both processes completed")
#
# #
# # ✅ Example 2: Multiprocessing Pool
# # 🔹 Run same function on multiple values in parallel
# from multiprocessing import Pool
# import time
#
# def square(n):
#     time.sleep(1)
#     return n * n
#
# if __name__ == "__main__":
#     numbers = [1, 2, 3, 4, 5]
#
#     with Pool(processes=3) as pool:  # 3 processes in parallel
#         results = pool.map(square, numbers)
#
#     print("Squares:", results)
#
#
# # ✅ Example 3: CPU Heavy Task — Compare Time
# # Without multiprocessing (slow)
# import time
#
# def cube(n):
#     return n*n*n
#
# numbers = list(range(1, 50000))
#
# start = time.time()
# result = [cube(x) for x in numbers]
# print("Time without multiprocessing:", time.time() - start)
#
#
# #
# # With multiprocessing (fast!)
# from multiprocessing import Pool
# import time
#
# def cube(n):
#     return n*n*n
#
# if __name__ == "__main__":
#     numbers = list(range(1, 50000))
#
#     start = time.time()
#     with Pool() as pool:
#         result = pool.map(cube, numbers)
#
#     print("Time WITH multiprocessing:", time.time() - start)



# # ✅ Correct Example to Test Speed
#
# import time
# from multiprocessing import Pool
#
# # CPU-intensive task
# def long_task(x):
#     total = 0
#     for i in range(5_000_000):
#         total += (i * x) % 23
#     return total
#
# # Without multiprocessing
# start = time.time()
# for i in range(4):
#     long_task(i)
# print("Time WITHOUT multiprocessing:", time.time() - start)
#
# # With multiprocessing
# if __name__ == "__main__":
#     start = time.time()
#     with Pool() as p:
#         p.map(long_task, range(4))
#     print("Time WITH multiprocessing:", time.time() - start)



from multiprocessing import Pool
import time

def square(num):
    # Simulate heavy CPU task
    time.sleep(2)
    return num * num

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]

    print("Running WITHOUT multiprocessing...")
    start = time.time()
    results = [square(n) for n in numbers]
    print("Results:", results)
    print("Time WITHOUT multiprocessing:", time.time() - start)

    print("\nRunning WITH multiprocessing...")
    start = time.time()
    with Pool() as p:   # Pool automatically uses CPU cores
        results = p.map(square, numbers)
    print("Results:", results)
    print("Time WITH multiprocessing:", time.time() - start)
