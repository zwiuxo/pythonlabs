import numpy as np

text = """3,4,17,-3
5,11,-1,6
0,2,-5,8"""

with open('matrix.txt', 'w') as f:
    f.write(text)

matrix = np.loadtxt('matrix.txt', delimiter=',', dtype=np.int64)
print("Матрица:")
print(matrix)
print("Сумма всех элементов:", matrix.sum())
print("Максимальный элемент:", matrix.max())
print("Минимальный элемент:", matrix.min())