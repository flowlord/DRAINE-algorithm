# -*- coding: utf-8 -*-

import os
import json

def load_settings(settings_path):
    """Load settings from a JSON file."""
    try:
        with open(settings_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Settings file not found: {settings_path}")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in settings file.")

def load_word_list(file_path):
    """Load a list of words from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Word list file not found: {file_path}")

def filter_words_by_length(word_list, min_length, max_length, output_path):
    """Filter words by length and save the result to a new file."""
    filtered_words = [word for word in word_list if min_length <= len(word) <= max_length]

    with open(output_path, "w", encoding="utf-8") as file:
        for word in filtered_words:
            file.write(word + "\n")
            print(f"Filtered word: {word}")

    print(f"Filtered words saved to {output_path}")

if __name__ == "__main__":
    SETTINGS_PATH = "settings.json"

    settings = load_settings(SETTINGS_PATH)
    word_list = load_word_list(settings["word_lst_pth"])

    output_file = f"filtered_{os.path.basename(settings['word_lst_pth'])}"
    filter_words_by_length(
        word_list=word_list,
        min_length=settings["MIN_LENGTH"],
        max_length=settings["MAX_LENGTH"],
        output_path=output_file
    )


