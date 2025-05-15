lst = [1,2,3,4,5]
a = lst.index(max(lst))
b = lst.index(min(lst))
lst[a], lst[b] = lst[b], lst[a]
print(lst)
