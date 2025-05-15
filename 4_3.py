lst = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']

dict = {}
for i in lst:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
a = " ".join(map(str, dict.values()))
print(a)