from math import sqrt

# О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5?
# Если да, найдите ее.

variance = 0.2
a = 0.5

# Зная дисперсию можно найти значение правой границы (b), используя формулу нахождения дисперсии
# 1/5 = 1/12 * (x-1/2)**2
b = 0.5 + 2 * sqrt(3 / 5)
# Ответ: 2.049

# среднее значение
mean = (a + b) / 2
# Ответ: 1.274

