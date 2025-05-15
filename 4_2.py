lst = [1, 2, 3, 2]
lstt = [2, 3, 4]
cnt = 0
for num in lst:  
    if num in lstt:  
        cnt += 1
print(cnt)