from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

# Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?

n = 144
p = 1 / 2
k = 70
q = 1 - p

result = combinations(n, k) * p**k * q**(n-k)
# Ответ: вероятность, что орел выпадет ровно 70 раз равна 0.062 или 6.2%
