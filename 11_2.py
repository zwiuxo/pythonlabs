import numpy as np
import matplotlib.pyplot as plt

mu = 0  # математическое ожидание 
sigma = 1  # стандартное отклонение 
samples = 1000  # размер выборки

def normal(x, mu, sigma):
    a = 1.0 / (sigma * np.sqrt(2 * np.pi))
    b = np.exp(-0.5 * ((x - mu) / sigma) ** 2)
    return a * b

# Диапазон значений x
x_vals = np.linspace(mu - 4*sigma, mu + 4*sigma, num=500)
pdf_vals = normal(x_vals, mu, sigma)

data = np.random.normal(mu, sigma, samples)


plt.figure(figsize=(10, 4))

plt.plot(x_vals, pdf_vals, label="Теоретическая плотность", linewidth=2)

plt.hist(data, bins=30, density=True, alpha=0.6, label="Гистограмма выборки")

plt.title(f"Нормальное распределение: μ={mu}, σ={sigma}")
plt.xlabel("Значение")
plt.ylabel("Плотность вероятности")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()