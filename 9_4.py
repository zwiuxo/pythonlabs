import numpy as np

x = np.array([6, 2, 0, 3, 0, 4, 0, 5, 7, 0])

zero_positions = np.where(x[:-1] == 0)[0] 
next_to_zero = x[zero_positions + 1]

if len(next_to_zero) > 0:
    max_val = np.max(next_to_zero)
    print(f"max after 0: {max_val}")
else:
    print("no one el after 0")