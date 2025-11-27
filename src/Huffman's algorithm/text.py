def generate_table(message: str) -> dict[str, str]:
    freq_table = {}
    for symbol in message:
        if symbol in freq_table:
            freq_table[symbol] += 1
        else:
            freq_table[symbol] = 1

    nodes = [(key, freq_table[key]) for key in freq_table]
    nodes = sorted(nodes, key=lambda element: element[1])

    while len(nodes) != 1:
        element_1 = nodes[0]
        element_2 = nodes[1]
        new_element = ([element_1[0], element_2[0]], element_1[1] + element_2[1])
        nodes = nodes[2:]
        nodes += [new_element]
        nodes = sorted(nodes, key=lambda element: element[1])

    tree = nodes[0][0]

    def traverse(node, current_code=""):
        if isinstance(node, str):
            yield (node, current_code if current_code else "0")
        else:
            yield from traverse(node[0], current_code + "0")
            yield from traverse(node[1], current_code + "1")

    return dict(traverse(tree))


def encode(message: str) -> tuple[str, dict[str, str]]:
    table = generate_table(message)
    result = ""
    for symbol in message:
        result += table[symbol]
    return (result, table)


def decode(message: str, table: dict[str, str]) -> str:
    reversed_table = {}
    for key in table:
        reversed_table[table[key]] = key

    current_code = ""
    result = ""

    for bit in message:
        current_code += bit

        if current_code in reversed_table:
            result += reversed_table[current_code]
            current_code = ""

    return result
