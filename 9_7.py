import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
# Виды в последнем столбце
species = iris[:, 4]
# Уникальные названия и их частоты
unique_species, counts = np.unique(species, return_counts=True)
print("Виды ириса:", unique_species)
print("Количество объектов по виду:", counts)