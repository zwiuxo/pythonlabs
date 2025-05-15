with open('input2.txt', 'r') as f:
    numbers = [int(line) for line in f.readlines()]

numbers.sort()
    
with open('output2.txt', 'w') as f:
    for number in numbers:
        f.write(f"{number}\n")
