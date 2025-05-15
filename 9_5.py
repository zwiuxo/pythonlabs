import numpy as np
from scipy.stats import multivariate_normal
import time

def log(X, m, C):
    N, D = X.shape
    C_inv = np.linalg.inv(C)
    log_det_C = np.log(np.linalg.det(C))
    logpdf = -D / 2 * np.log(2 * np.pi)
    diff = X - m  
    for i in range(N):
        # Квадратичная форма + половина log_det_C
        quad = diff[i].T @ C_inv @ diff[i]
        logpdf -= 0.5 * quad + 0.5 * log_det_C
    return logpdf


N, D = 1000, 2
np.random.seed(42)
X = np.random.rand(N, D)
m = np.array([0.5, 0.5])
C = np.array([[1, 0.5], [0.5, 1]])


logpdf_custom = log(X, m, C)

logpdf_scipy = multivariate_normal(mean=m, cov=C).logpdf(X)

print("Разница:", np.max(np.abs(logpdf_custom - logpdf_scipy)))

start_custom = time.time()
log(X, m, C)
end_custom = time.time()

start_scipy = time.time()
multivariate_normal(mean=m, cov=C).logpdf(X)
end_scipy = time.time()

print("Время выполнения нашей функции:", end_custom - start_custom)
print("Время выполнения scipy функции:", end_scipy - start_scipy)