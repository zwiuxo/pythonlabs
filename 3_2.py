def decode(a):
    decoded = []
    i = 0
    n = len(a)
    
    while i < n:
        char = a[i]
        i += 1
        
        count_str = ''
        while i < n and a[i].isdigit():
            count_str += a[i]
            i += 1
        
        count = int(count_str) if count_str else 1
        decoded.append(char * count)
    
    return ''.join(decoded)

decoded = decode("Y4g2ke3A3BV")
print(f"decoded: {decoded}")  