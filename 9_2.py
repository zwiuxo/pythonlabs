import numpy as np

x = np.array([2, 2, 2, 3, 3, 3, 5])

def rle_encode(x):
    unique_values = []
    counts = []
    current_val = x[0]
    count = 1
    
    for val in x[1:]:
        if val == current_val:
            count += 1
        else:
            unique_values.append(current_val)
            counts.append(count)
            current_val = val
            count = 1
    unique_values.append(current_val)
    counts.append(count)
    
    return (np.array(unique_values), np.array(counts))

values, counts = rle_encode(x)
print(f"values: {values}, repeats: {counts}")