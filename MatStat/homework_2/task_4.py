from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


# В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей,
# из которых 9 белых. Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность того,
# что все мячи белые? Какова вероятность того, что ровно два мяча белые? Какова вероятность того,
# что хотя бы один мяч белый?

# bucket_1_total_combinations = combinations(10, 2)
# # bucket_2_total_combinations = combinations(11, 2)
# #
# # p_bucket_1 =
# #
# # print(bucket_1_total_combinations)
# # print(bucket_2_total_combinations)


# Какова вероятность того, что все мячи белые?
bucket_1_balls_probability = 7 / 10 * 6 / 9
bucket_2_balls_probability = 9 / 11 * 8 / 10
four_balls_white = bucket_1_balls_probability * bucket_2_balls_probability
# Ответ: вероятность того, что все мячи белые равна 0.29 или 29%


# Какова вероятность того, что ровно два мяча белые?
four_balls_combinations = combinations(4, 1)

# Какова вероятность того, что хотя бы один мяч белый?