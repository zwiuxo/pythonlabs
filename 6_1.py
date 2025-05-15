lst = list(map(int, open("input.txt").readline().split() ))
cnt = 1
for i in range(len(lst)):
    cnt*= lst[i]
f = open("output.txt", "w")
f.write(str(cnt))

