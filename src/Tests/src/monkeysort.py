from random import shuffle

def monekey_sort(array: list) -> list:
    while True:
        for index in range(1, len(array)):
            if array[index-1] > array[index]:
                shuffle(array)
                break
        else:
            return array
    


print(monekey_sort([-4, 100, -30, 21, 42, -9, 0, 5]))