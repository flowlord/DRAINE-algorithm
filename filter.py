# -*- coding: utf-8 -*-

MIN_LENGTH = 2

MAX_LENGTH = 10

file_path="word_lst.txt"

word_lst = open(file_path, "r", encoding="utf-8").read().split("\n")

def d_filter_by_lenght():
    new_file = "d_" + file_path[0:-4] + ".txt"
    new_file = open(new_file, "w", encoding="utf-8")
    for word in word_lst:
        if (MIN_LENGTH <= len(word) <= MAX_LENGTH):
            new_file.write(word + "\n")
            print(f"Filtered words: {word}")
    new_file.close()

