def encode(s):
    result = []
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append(current_char + (str(count) if count > 1 else ""))
            current_char = char
            count = 1
    
    result.append(current_char + (str(count) if count > 1 else ""))
    return "".join(result)

input_str = "YYYYggkeeeAAABV"
encoded = encode(input_str)
print(f"Закодированная строка: {encoded}") 