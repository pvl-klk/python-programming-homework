from random import shuffle

def monekey_sort(array: list) -> list:
    while True:
        for index in range(1, len(array)):
            if array[index-1] > array[index]:
                shuffle(array)
                break
        else:
            return array
    