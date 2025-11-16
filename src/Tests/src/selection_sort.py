def selection_sort(array: list) -> list:
    for index_1 in range(len(array)):
        min_idx = index_1
        for index_2 in range(index_1 + 1, len(array)):
            if array[index_2] < array[min_idx]:
                min_idx = index_2

        array[index_1], array[min_idx] = array[min_idx], array[index_1]

    return array
