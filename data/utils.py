import random, json

def getkey(key_name):
    with open(key_name, "r") as json_file:
        return json.load(json_file)

def readeblecontent(input_name):
    with open(input_name, "r") as txt:
        return txt.read()

def getperm(l, key):
    randomseed = int(key["seed"])

    # Calculate a seed based on the sum of ASCII values of characters + unique seed from key.
    seed = sum(ord(char) for char in l)
    random.seed(seed + randomseed)
    
    permutation = list(range(len(l)))
    random.shuffle(permutation)
    return permutation

def shuffle(l, key):
    perm = getperm(l, key)
    shuffled_list = [l[j] for j in perm]

    l[:] = shuffled_list

def unshuffle(l, perm):
    unshuffled_list = [None] * len(l)
    for i, j in enumerate(perm):
        unshuffled_list[j] = l[i]
    l[:] = unshuffled_list
