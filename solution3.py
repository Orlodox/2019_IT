import numpy as np


def main():
    for indexes in get_indexes(100, 5, 0.25):
        print(indexes)


def get_indexes(gen_length, batches_count, split_ratio):
    second = (gen_length - 1) / (batches_count + (1 / split_ratio))
    i = 0
    j = 0
    k = 0
    for n in range(batches_count):
        j = i + second * (1 / split_ratio)
        k = j + second
        yield np.array([int(i), int(j), int(k)])
        i += second


if __name__ == "__main__":
    main()
