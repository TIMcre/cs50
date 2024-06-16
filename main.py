import sys

decode_table = {
    "0000": "0",
    "0001": "00",
    "0010": "000",
    "0011": "0000",
    "0100": "00000",
    "0101": "000000",
    "0110": "0000000",
    "0111": "00000000",
    "1000": "1",
    "1001": "11",
    "1010": "111",
    "1011": "1111",
    "1100": "11111",
    "1101": "111111",
    "1110": "1111111",
    "1111": "11111111",
}


def decode(encoded_list, decode_table=decode_table):
    result = []
    for item in encoded_list:
        try:
            result.append(decode_table[item])
        except KeyError:
            result.append(None)
    return result


codiert = "0111-0111-0001-1011-0110-1000-0110-1000-0101-1001-0100-1000-0101-1000-0110-1011-0111-0111-0001"
codiert = "0111-0111-0111-0001-1000-1001-0110-0110-0000-1000-1001-0110-0110-0000-1000-1001-1010-1000-1110-1110-0000-0001-1110-1110-1000-1001-1110-1110-0101-0101-0000-1000-1001-0110-0110-0000-1000-1001-0110-0110-0000-1000-1001-0110-0110-0110-0000"

codiert_list = codiert.split("-")

decoded = decode(codiert_list)

output_len = len("".join(decoded))
input_len = len("".join(codiert_list))

print(f"\nKompressions Rate: {round((input_len / output_len) * 100)}%")
print(f"Codiert Länge: {input_len}")
print(f"Decodiert Länge: {output_len}\n")

print("Decoded:\n" + "".join(decoded))
