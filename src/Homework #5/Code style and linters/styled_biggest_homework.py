# Функция проверки корректности размещения ферзей по вертикали и диагонали
def is_safe_direction(
        coordinate_1: tuple[int, int], coordinate_2: tuple[int, int]
        ) -> bool:
    if coordinate_1[1] == coordinate_2[1] or abs(
        coordinate_1[1] - coordinate_2[1]
    ) == abs(coordinate_1[0] - coordinate_2[0]):
        return False
    return True


N = int(input("Enter the value N: "))

board_size = N**2

counter = 0

# Цикл перебора сочетаний ферзей по три
stack: list[list[tuple[int, int]]] = [[]]
while stack:
    # Нынешнее сочетание ферзей
    placements: list[tuple[int, int]] = stack.pop()

    if len(placements) == N:
        counter += 1
    else:
        current_row = len(placements)
        # Перебор возможных ферзей в пределах одной горизонтали
        for column in range(N):
            # Проверка, возможно ли такое сочетание для каждой уже размещенной фигуры
            for placement_column, placement_row in placements:
                if not is_safe_direction(
                    (placement_column, placement_row), (current_row, column)
                ):
                    break
            else:
                # Добавление сочетания, если такое возможно
                stack.append(placements + [(current_row, column)])

print(f"The number of possible different arrangements is {counter}")
