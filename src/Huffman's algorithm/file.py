from json import loads, dumps
from collections import Counter


def generate_table(data: bytes) -> dict[int, str]:
    freq_table = Counter(data)

    nodes = [(byte, freq) for byte, freq in freq_table.items()]
    nodes = sorted(nodes, key=lambda element: element[1])

    while len(nodes) > 1:
        element_1 = nodes[0]
        element_2 = nodes[1]
        new_element = ([element_1[0], element_2[0]], element_1[1] + element_2[1])
        nodes = nodes[2:]
        nodes += [new_element]
        nodes = sorted(nodes, key=lambda element: element[1])

    tree = nodes[0][0] if nodes else []

    def traverse(node, current_code=""):
        if isinstance(node, int):
            yield (node, current_code if current_code else "0")
        else:
            yield from traverse(node[0], current_code + "0")
            yield from traverse(node[1], current_code + "1")

    return dict(traverse(tree)) if tree else {}


def encode(path: str) -> None:
    with open(path, "rb") as file:
        content = file.read()

    table = generate_table(content)

    result_bits = ""
    for byte in content:
        result_bits += table[byte]

    padding = 8 - len(result_bits) % 8
    if padding != 8:
        result_bits += "0" * padding

    result_bytes = bytearray()
    for i in range(0, len(result_bits), 8):
        byte_str = result_bits[i : i + 8]
        result_bytes.append(int(byte_str, 2))

    with open(path, "wb") as file:
        file.write(bytes([padding]))

        table_json = dumps({str(k): v for k, v in table.items()})
        table_bytes = table_json.encode("utf-8")
        file.write(len(table_bytes).to_bytes(4, "big"))
        file.write(table_bytes)

        file.write(result_bytes)


def decode(path: str) -> None:
    with open(path, "rb") as file:
        padding = int.from_bytes(file.read(1), "big")

        table_length = int.from_bytes(file.read(4), "big")
        table_data = file.read(table_length).decode("utf-8")

        encoded_data = file.read()

    table_json = loads(table_data)
    table = {int(key): value for key, value in table_json.items()}
    reversed_table = {value: key for key, value in table.items()}

    bits_string = ""
    for byte in encoded_data:
        bits_string += format(byte, "08b")

    if padding != 0:
        bits_string = bits_string[:-padding]

    current_code = ""
    result_bytes = bytearray()

    for bit in bits_string:
        current_code += bit
        if current_code in reversed_table:
            result_bytes.append(reversed_table[current_code])
            current_code = ""

    if current_code:
        raise ValueError("Decoding error")

    with open(path, "wb") as file:
        file.write(result_bytes)
