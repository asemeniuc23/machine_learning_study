import numpy as np

# Измерены значения IQ выборки студентов,
# обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

sample = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
n = len(sample)
M = np.mean(sample)
t = 2.262
variance = sample.var(ddof=1)
std = np.sqrt(variance)

confidence_interval_a = M - t * (std / np.sqrt(len(sample)))
confidence_interval_b = M + t * (std / np.sqrt(len(sample)))
# Ответ: (110.55;125.64)

