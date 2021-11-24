KEY = 2


def encode(value: str):  # 1234 -> 2345
    result = ''
    for char in value:
        result += chr(ord(char) + KEY)

    return result

def decode(value: str):  # 2345 -> 1234
    result = ''
    for char in value:
        result += chr(ord(char) - KEY)

    return result

print(decode('2345'))
print(decode('bcde'))
print(decode('Ejnb'))