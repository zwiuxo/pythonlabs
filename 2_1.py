n = int(input("n:"))

triangle = []
for i in range(n):
    row = [1]  
    if i > 0:  
        prevRow = triangle[i-1]  
        for j in range(1, i):
            row.append(prevRow[j-1] + prevRow[j])
        row.append(1)  
    triangle.append(row)

maxWidth = len(' '.join(map(str, triangle[-1])))

for row in triangle:
    rowStr = ' '.join(map(str, row))
    currWidth = len(rowStr)
    left = (maxWidth - currWidth) // 2
    print(' ' * left + rowStr)