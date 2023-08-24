import random

def getperm(l, key=6135584619):
    # Calculate a seed based on the sum of ASCII values of characters.
    seed = sum(ord(char) for char in l)
    random.seed(seed + key)
    
    permutation = list(range(len(l)))
    random.shuffle(permutation)
    return permutation

def shuffle(l):
    permutation = getperm(l)
    shuffled_list = [l[j] for j in permutation]

    l[:] = shuffled_list

def unshuffle(l, permutation):
    unshuffled_list = [None] * len(l)
    for i, j in enumerate(permutation):
        unshuffled_list[j] = l[i]
    l[:] = unshuffled_list
