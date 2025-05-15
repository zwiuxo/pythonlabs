with open('input4.txt', encoding='utf-8') as f:
    children = [line.split() for line in f] 

oldest = max(children, key=lambda x: x[2])
youngest = min(children, key=lambda x: x[2])

with open('oldest.txt', 'w', encoding='utf-8') as f:
    f.write(f"{oldest[0]} {oldest[1]} {oldest[2]}")
    
with open('youngest.txt', 'w', encoding='utf-8') as f:
    f.write(f"{youngest[0]} {youngest[1]} {youngest[2]}")
