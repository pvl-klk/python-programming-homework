def is_safe_direction(coordinate_1: tuple[int, int], coordinate_2: tuple[int, int]) -> bool:
    if coordinate_1[1] == coordinate_2[1] or abs(
        coordinate_1[1] - coordinate_2[1]
    ) == abs(coordinate_1[0] - coordinate_2[0]):
        return False
    return True


N = int(input("Enter the value N: "))

board_size = N**2

counter = 0

stack: list[list[tuple[int, int]]] = [[]]
while stack:
    placements: list[tuple[int, int]] = stack.pop()

    if len(placements) == N:
        counter += 1
    else:
        current_row = len(placements)
        for column in range(N):
            for placement_column, placement_row in placements:
                if not is_safe_direction(
                    (placement_column, placement_row), (current_row, column)
                ):
                    break
            else:
                stack.append(placements + [(current_row, column)])

print(f"The number of possible different arrangements is {counter}")
