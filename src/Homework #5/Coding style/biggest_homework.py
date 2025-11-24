# A function that verifies the correct placement of the queen vertically and diagonally
def is_safe_direction(
    coordinate_1: tuple[int, int],
    coordinate_2: tuple[int, int],
) -> bool:
    if coordinate_1[1] == coordinate_2[1] or abs(
        coordinate_1[1] - coordinate_2[1],
    ) == abs(coordinate_1[0] - coordinate_2[0]):
        return False
    return True


N = int(input("Enter the value N: "))

board_size = N**2

counter = 0


stack: list[list[tuple[int, int]]] = [[]]
# The main loop, sorting through the number of combinations of possible placements
# and putting them on the stack
while stack:
    # Get the last placement from the top of the stack
    placements: list[tuple[int, int]] = stack.pop()

    # Check the numebr of placements
    if len(placements) == N:
        counter += 1
    else:
        current_row = len(placements)
        # Go through the values of possible placements within the same horizontal
        for column in range(N):
            for placement_column, placement_row in placements:
                if not is_safe_direction(
                    (placement_column, placement_row),
                    (current_row, column),
                ):
                    break
            else:
                # Add the placement to the stack if possible
                stack.append(placements + [(current_row, column)])

print(f"The number of possible different arrangements is {counter}")
