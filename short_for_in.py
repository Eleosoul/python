my_scores = {
    'a': 10,
    'b': 15,
    'c': 100
}

scores = {k: v * 10 for k, v in my_scores.items()}

print(scores)

my_list = [7, 12, 15]

list_to_dict = {k:v for k, v in enumerate(my_list)}

print(list_to_dict )