from math import sqrt

# Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. Посчитать (желательно без
# использования статистических методов наподобие std, var, mean) среднее арифметическое, среднее квадратичное
# отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.

sample = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]

# среднее арифметическое
mean = sum(sample) / len(sample)
# Ответ: среднее арифметическое - 65.3

# среднее квадратичное отклонение
std = sqrt(sum((x - sum(sample ) / len(sample)) ** 2 for x in sample) / (len(sample)))
# Ответ: среднее квадратичное отклонение - 30.8238543

# смещенную и несмещенную оценки дисперсий
variance = sum((x - sum(sample ) / len(sample)) ** 2 for x in sample) / (len(sample))
# Ответ: смещенная оценка дисперсии - 950.11

variance2 = sum((x - sum(sample ) / len(sample)) ** 2 for x in sample) / (len(sample) - 1)
# Ответ: несмещенная оценка дисперсии - 1000.11
