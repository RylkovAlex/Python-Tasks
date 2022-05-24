import timeit

code_append = """

elements = range(%d)
array = []
for e in elements:
    array.insert(0, e)
"""


def elapsed_time(code, size):
    return timeit.timeit(code % size, number=100) / 100


for exp in range(10, 15):
    size_1 = 2 ** exp
    size_2 = 2 * size_1
    measure_1 = elapsed_time(code_append, size_1)
    measure_2 = elapsed_time(code_append, size_2)
    ratio = measure_2 / measure_1
    print(f"[{size_2} elements: {measure_2:.3f} sec]/[{size_1} elements: : {measure_1:.3f} sec] -> {ratio:.1f}")