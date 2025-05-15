lst = [10, 15, 12, 18, 20, 10]
newLst = []
for i in range(1, len(lst)):
    if lst[i] > lst[i-1]: newLst.append(lst[i])
print(newLst)