from math import factorial

def combinations(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

# 1. Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.

# число исходов, благоприятствующих нашему событию
four_kresti_of_four = combinations(4, 4)
# Результат - 1

# Общее число исходов 4 карты из 52
all_possible_combitantions = combinations(52, 4)
# Результат - 270725

result_1_a = (four_kresti_of_four / all_possible_combitantions) * 100
# Общий результат - 0.000369%


# б) Найти вероятность, что среди 4-х карт окажется ХОТЯ БЫ один туз.

# Поиск всех удачных комбинаций с хотябы одним тузом
## 1 туз
one_tuz_of_four_cards = combinations(4, 1)
# Результат - 4
other_3_cards_combination = combinations(48, 3)
# Результат - 17296
one_tuz_combintaion = one_tuz_of_four_cards * other_3_cards_combination
# Результат комбинаций с 1 тузом - 69184

## 2 туза
two_tuz_of_four_cards = combinations(4, 2)
# Результат - 6
other_2_cards_combination = combinations(48,2)
# Результат - 1128
two_tuz_combintaion = two_tuz_of_four_cards * other_2_cards_combination
# Результат комбинаций с 2 тузами - 6768

# 3 туза
three_tuz_of_four_cards = combinations(4, 3)
# Результат - 4
other_1_cards_combination = combinations(48,1)
# Результат - 192
three_tuz_combintaion = three_tuz_of_four_cards * other_1_cards_combination
# Результат комбинаций с 3 тузами - 6768

# 4 туза
four_tuz_combination = combinations(4, 4)
# Результат комбинаций с 4 тузами - 1

# Общее кол-во всех комбинаций с тузами
all_positive_tuz_combinations = one_tuz_combintaion + two_tuz_combintaion + three_tuz_combintaion + four_tuz_combination
# Общее кол-во всех комбинаций с тузами - 76144

result_1_b = (all_positive_tuz_combinations / all_possible_combitantions) * 100
# Ответ - 28.12%
