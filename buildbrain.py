# -*- coding: utf-8 -*-

import itertools
import json
import os
import sys

def read_dictionary(file_path):
    """Read a list of words from a file."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, 'r', encoding='utf-8') as file:
        words = [line.strip().lower() for line in file if line.strip()]
    return words

def generate_unique_permutations(word):
    """Generate all unique permutations of a word."""
    return sorted(set(''.join(p) for p in itertools.permutations(word)))

def create_json_file(word, permutations, output_dir):
    """Create a JSON file for a word with its permutations."""
    file_name = f"{word}.json"
    file_path = os.path.join(output_dir, file_name)

    data = {
        "permutations": permutations
    }

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def process_words(words, output_dir, max_length, log_interval):
    """Generate JSON files for words within a specified length and log progress."""
    existing_files = set(os.listdir(output_dir))

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Output directory created: {output_dir}")

    total_words = len(words)
    processed_words = 0
    included_words = 0
    excluded_words = 0

    for word in words:
        processed_words += 1
        if word:
            if len(word) <= max_length:
                if f"{word}.json" not in existing_files:
                    permutations = generate_unique_permutations(word)
                    create_json_file(word, permutations, output_dir)
                    included_words += 1
                else:
                    excluded_words += 1
            else:
                excluded_words += 1

        if processed_words % log_interval == 0:
            print(f"{processed_words}/{total_words} words processed...")

    print(f"\nProcessing complete. {included_words} words included and {excluded_words} words excluded.")
    print(f"JSON files have been saved to the directory '{output_dir}'.")

def main():
    input_file = 'd_word_lst.txt'
    output_dir = 'output'
    max_length = 10
    log_interval = 5

    try:
        words = read_dictionary(input_file)
        print(f"{len(words)} words read from '{input_file}'.")

        process_words(words, output_dir, max_length=max_length, log_interval=log_interval)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()


