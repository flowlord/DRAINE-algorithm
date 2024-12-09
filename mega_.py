from itertools import permutations
from  random import choice
import json
from uuid import uuid4

MIN_LENGTH = 2

MAX_LENGTH = 10

file_path="world_lst_fr.txt"

word_lst = open(file_path, "r", encoding="utf-8").read().split("\n")

word_prop_pth = "G:/T3/"


def preprocess_word(word_prop_pth):
    wlst = open(file_path, "r", encoding="utf-8").read().split("\n")
    wlst = [word_prop_pth + x + ".json" for x in wlst if len(x)<=MAX_LENGTH]

    return wlst

def get_word_comb(word):

    word = word_prop_pth + word + ".json"
    word_lst = preprocess_word(word_prop_pth)

    if word in word_lst:
        with open(word, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data["permutations"]

def gen_subs_dict(des_path):

    substituted_list = word_lst.copy()

    key_file = open(des_path+".txt", "w", encoding="utf-8")

    for word in substituted_list:
        if len(word) <= MAX_LENGTH:
            if len(word) >= MIN_LENGTH:
                new_word = choice(get_word_comb(word))
                key_file.write(new_word + "\n")
                print(f"{word} -> {new_word}")
            else:
                key_file.write(word + "\n")
                print(f"{word} x skipped (too short)")
        else:
            key_file.write(word + "\n")
            print(f"{word} x skipped (too long)")

    key_file.close()


def gen_many_keys(num_keys, des_path):
    for i in range(num_keys):
        id = str(uuid4())
        id = id[0:8]
        gen_subs_dict(des_path+id)
        print(f"Generated key: {i} {id}")


gen_many_keys(100, "key/")






