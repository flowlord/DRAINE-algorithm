# -*- coding: utf-8 -*-

from itertools import permutations
from  random import choice
import json
from uuid import uuid4
import os

if not os.path.exists("d_keys/"):
    os.makedirs("d_keys/")

settings_pth = "settings.json"

with open(settings_pth, 'r') as file:
    data = json.load(file)

MIN_LENGTH = data["MIN_LENGTH"]

MAX_LENGTH = data["MAX_LENGTH"]

word_lst = open(data["word_lst_pth"], "r", encoding="utf-8").read().split("\n")

words_prop_pth = "G:/T3/"

def get_word_comb(word):

    word_prop_pth  = words_prop_pth+"/"+word+".json"

    if word in word_lst:
        with open(word_prop_pth, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data["permutations"]


def gen_subs_dict():

    substituted_list = word_lst.copy()

    key_file = open(f"d_keys/{str(uuid4())[0:8]}.txt", "w", encoding="utf-8")

    for word in substituted_list:
        if (MIN_LENGTH <= len(word) <= MAX_LENGTH):
            new_word = choice(get_word_comb(word))
            key_file.write(new_word + "\n")
            print(f"{word} -> {new_word}")
        else:
            key_file.write(word + "\n")
            print(f"word: {word} x skipped (too long or too short)")

    key_file.close()


def encrypt(msg, key_pth):
    key_word = open(key_pth, "r", encoding="utf-8").read().split("\n")[0:-1]
    cip_dict = dict(map(lambda i,j : (i,j) , word_lst,key_word))

    msg = (msg.lower()).split(" ")

    new_msg = ""

    for word in msg:
        new_msg = new_msg + " " + cip_dict[word]
    return new_msg


def decrypt(msg, key_pth):
    key_word = open(key_pth, "r", encoding="utf-8").read().split("\n")[0:-1]
    cip_dict = dict(map(lambda i,j : (i,j) ,key_word, word_lst))

    msg = (msg.lower()).split(" ")

    new_msg = ""

    for word in msg:
        new_msg = new_msg + " " + cip_dict[word]
        
    return new_msg


# test -------------------------------------------------

msg = "il se dit il faut que je gagne dix heures et je prendrai mon bock à américain"
key_pth = "d_keys/faa5e90e.txt"

encrypted_text = encrypt(msg, key_pth)
print(encrypted_text)

print(decrypt(encrypted_text, key_pth))

# 12/12/24: Test passed. Encrypt and decrypt functions work correctly.

# ---------------------------------

