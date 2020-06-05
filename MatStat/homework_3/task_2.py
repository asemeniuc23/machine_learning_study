from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


# В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых.
# Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?

# 2 белых из 1ой и 1 белый из 2ой
p1 = combinations(5, 2) / combinations(8, 2) * (combinations(5, 1) * combinations(7, 3)) / combinations(12, 4)
# Ответ: 0.12

# 1 белый из 1ой и 2 белых из 2ой
p2 = (combinations(5, 1) * combinations(3, 1)) / combinations(8, 2) * (combinations(5, 2) * combinations(7, 2)) / combinations(12, 4)
# Ответ: 0.22

# 0 белых из 1ой и 3 белых из 2ой
p3 = combinations(3, 2) / combinations(8, 2) * (combinations(5, 3) * combinations(7, 1)) / combinations(12, 4)
# Ответ: 0.015


p = p1 + p2 + p3
# Ответ: 0.36