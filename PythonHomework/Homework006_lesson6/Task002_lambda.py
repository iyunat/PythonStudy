# напечатать словарь в порядке убывания суммы каждого значения

bigrams = {
    "AB": [21, 12, 10], 
    "BC": [-1, -5, 3], 
    "CD": [33, 101, 0],
    "DE": [68, 68],
    "EF": [155, 120, 1],
    "FG": [5, 11, 32],
    "GH": [20, 20, 20]
    }
sorter = sorted(bigrams, key=lambda key: sum(bigrams[key]), reverse=True)

for key in sorter:
    print(key, bigrams[key])

# без функции lambda

# from functools import partial

# def sort_func(key, dict):
#     return sum(dict[key])

# bigrams = {
#      "AB": [21, 12, 10], 
#      "BC": [-1, -5, 3], 
#      "CD": [33, 101, 0],
#      "DE": [68, 68],
#      "EF": [155, 120, 1],
#      "FG": [5, 11, 32],
#      "GH": [20, 20, 20]}
# partial_sort = partial(sort_func, dict=bigrams)
# sorter = sorted(bigrams.keys(), key=partial_sort, reverse=True)

# for key in sorter:
#     print(key, bigrams[key])