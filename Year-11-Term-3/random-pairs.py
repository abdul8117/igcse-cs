import random

group_A = ["Bob", "John", "Nora"]
group_B = ["Cecil", "Rezaq", "Ralph", "Troy"]
pairs = []

num_of_pairs = 0
if len(group_A) > len(group_B):
    num_of_pairs = len(group_B)
else:
    num_of_pairs = len(group_A)

for i in range(num_of_pairs):
    pair = [random.choice(group_A), random.choice(group_B)]

    group_A.remove(pair[0])
    group_B.remove(pair[1])

    pairs.append(pair)

print("Groups:", *pairs, sep="\n")