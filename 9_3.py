import numpy as np

data = np.random.normal(size=(10, 4))

min_val = np.min(data)
max_val = np.max(data)
mean_val = np.mean(data)
dev = np.std(data)

first_5_rows = data[:5]

print(f"min: {min_val:.4f}")
print(f"max: {max_val:.4f}")
print(f"avg: {mean_val:.4f}")
print(f"deviation : {dev:.4f}")
print("\n1st five str:\n", first_5_rows)