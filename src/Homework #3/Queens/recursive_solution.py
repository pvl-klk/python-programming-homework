def is_safe_placement(coordinate_1: tuple[int, int], coordinate_2: tuple[int, int]) -> bool:
    if coordinate_1[0] == coordinate_2[0] or abs(
        coordinate_1[1] - coordinate_2[1]
    ) == abs(coordinate_1[0] - coordinate_2[0]):
        return False
    return True


N = int(input('Enter the value N: '))

board_size = N**2

result = 0
def foo(placements=[]):
    if len(placements) == N:
        global result
        result += 1
        return
    current_row = len(placements)
    for next_column in range(N):
        position = (next_column, current_row)
        if all(is_safe_placement(placement, position) for placement in placements):
            foo(placements + [position])

foo()

print(f"The number of possible different arrangements is {result}")
