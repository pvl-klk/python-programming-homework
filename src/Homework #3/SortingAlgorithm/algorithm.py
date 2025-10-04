def bubble_sort(array: list) -> list:
    array_legth = len(array)
    for _ in range(0, array_legth-1):
        for index in range(0, array_legth-1):
            if array[index] > array[index+1]:
                array[index], array[index+1] = array[index+1], array[index]
    return array


test_array = [4, 2, 5, 4, 7, 1, 3]
print(bubble_sort(test_array))

