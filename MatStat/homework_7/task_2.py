import numpy as np

# Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).

X = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

n = len(X)

def mse(B1, y=y, X=X, n=n):
    return np.sum((B1*X - y)**2) / n

B1 = 0.1
alpha = 1e-06


for i in range(500):
    B1 -= alpha * (2/n) * np.sum((B1*X - y) * X)
    if not i % 50:
        print(f"Iteration: {i}, B1={B1}, mse={mse(B1)}")

# Iteration: 0, B1=0.25952808, mse=493237.7212546963
# Iteration: 50, B1=4.497229618367758, mse=83233.94472982832
# Iteration: 100, B1=5.54537842245223, mse=58151.31823171113
# Iteration: 150, B1=5.804626485478126, mse=56616.849068093856
# Iteration: 200, B1=5.868748638669329, mse=56522.97550129376
# Iteration: 250, B1=5.884608547059329, mse=56517.232638059555
# Iteration: 300, B1=5.888531320728348, mse=56516.88130936019
# Iteration: 350, B1=5.889501575592372, mse=56516.85981627392
# Iteration: 400, B1=5.8897415574471985, mse=56516.85850140053
# Iteration: 450, B1=5.889800914315978, mse=56516.858420961085

print(mse(5.8898009))
# Ответ 56516.858420968776