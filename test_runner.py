import random
import timeit
from merge_sort import merge_sort
from insertion_sort import insertion_sort
from timsort_test import timsort

SIZES = [100, 1000, 5000, 10000, 20000]
REPEATS = 3

def generate_data(size):
    return [random.randint(0, 100000) for _ in range(size)]

def benchmark(func, data):
    return timeit.timeit(lambda: func(data.copy()), number=REPEATS) / REPEATS

with open("results.csv", "w") as f:
    f.write("Size,MergeSort,InsertionSort,Timsort\n")

    for size in SIZES:
        data = generate_data(size)
        print(f"Testing size: {size}")

        t_merge = benchmark(merge_sort, data)
        t_insert = benchmark(insertion_sort, data if size <= 2000 else [0])  # обмеження через повільність
        t_tim = benchmark(timsort, data)

        f.write(f"{size},{t_merge},{t_insert if size <= 2000 else 'N/A'},{t_tim}\n")