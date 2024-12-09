from itertools import permutations
from  random import choice
import json

settings_pth = "settings.json"

with open(settings_pth, 'r') as file:
    data = json.load(file)

MIN_LENGTH = data["MIN_LENGTH"]

MAX_LENGTH = data["MAX_LENGTH"]

word_lst = open(data["word_lst_pth"], "r", encoding="utf-8").read().split("\n")

#
word_prop_pth = "G:/T3/"


def preprocess_word(word_prop_pth):
    wlst = open(word_lst, "r", encoding="utf-8").read().split("\n")
    wlst = [word_prop_pth + x + ".json" for x in wlst if len(x)<=MAX_LENGTH]

    return wlst

def get_word_comb(word):

    word = word_prop_pth + word + ".json"
    word_lst = preprocess_word(word_prop_pth)

    if word in word_lst:
        with open(word, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data["permutations"]


def gen_subs_dict():

    substituted_list = word_lst.copy()

    key_file = open("key.txt", "w", encoding="utf-8")

    for word in substituted_list:
        if len(word) <= MAX_LENGTH:
            if len(word) >= MIN_LENGTH:
                new_word = choice(get_word_comb(word))
                key_file.write(new_word + "\n")
                print(f"{word} -> {new_word}")
            else:
                key_file.write(word + "\n")
                print(f"word: {word} x skipped (too short)")
        else:
            key_file.write(word + "\n")
            print(f"word: {word} x skipped (too long)")

    key_file.close()


def encrypt(msg, key_pth):
    key_word = open(key_pth, "r", encoding="utf-8").read().split("\n")[0:-1]
    cip_dict = dict(map(lambda i,j : (i,j) , word_lst,key_word))

    msg = (msg.lower()).split(" ")

    new_msg = ""

    for word in msg:
        if word in word_lst:
            new_msg = new_msg + " " + cip_dict[word]

    return new_msg



