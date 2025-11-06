import time
from concurrent.futures import ProcessPoolExecutor

def slow_square(n):
    time.sleep(1)
    return n * n

if __name__ == "__main__":
    start = time.time()
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(slow_square, range(5)))

    print("Time WITH ProcessPoolExecutor:", time.time() - start)
    print(results)
