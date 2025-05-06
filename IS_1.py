def to_ascii_value(char):
    """Custom function to get ASCII value of a character without ord()"""
    ascii_map = {
        ' ': 32, '!': 33, '"': 34, '#': 35, '$': 36, '%': 37, '&': 38, "'": 39,
        '(': 40, ')': 41, '*': 42, '+': 43, ',': 44, '-': 45, '.': 46, '/': 47,
        '0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55,
        '8': 56, '9': 57, ':': 58, ';': 59, '<': 60, '=': 61, '>': 62, '?': 63,
        '@': 64, 'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71,
        'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79,
        'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87,
        'X': 88, 'Y': 89, 'Z': 90, '[': 91, '\\': 92, ']': 93, '^': 94, '_': 95,
        '`': 96, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103,
        'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111,
        'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119,
        'x': 120, 'y': 121, 'z': 122, '{': 123, '|': 124, '}': 125, '~': 126
    }
    return ascii_map.get(char, 0)

def custom_and(a, b):
    """Custom AND operation without using & operator"""
    result = 0
    bit_position = 1
    while a > 0 or b > 0:
        a_bit = a % 2
        b_bit = b % 2
        if a_bit == 1 and b_bit == 1:
            result += bit_position
        bit_position *= 2
        a = a // 2
        b = b // 2
    return result

def custom_xor(a, b):
    """Custom XOR operation without using ^ operator"""
    result = 0
    bit_position = 1
    while a > 0 or b > 0:
        a_bit = a % 2
        b_bit = b % 2
        if (a_bit == 1 and b_bit == 0) or (a_bit == 0 and b_bit == 1):
            result += bit_position
        bit_position *= 2
        a = a // 2
        b = b // 2
    return result

def and_xor_string(input_string):
    print("Original String:", input_string)
    print("\nResults:")
    print(f"{'Character':<10} {'ASCII':<10} {'AND 127':<10} {'XOR 127':<10}")
    print("-" * 40)
    for char in input_string:
        ascii_value = to_ascii_value(char)
        and_result = custom_and(ascii_value, 127)
        xor_result = custom_xor(ascii_value, 127)
        print(f"{char:<10} {ascii_value:<10} {and_result:<10} {xor_result:<10}")

# Main driver
print("String AND and XOR Operations Program")
print("------------------------------------")
input_string = input("Enter the String: ")
and_xor_string(input_string)
