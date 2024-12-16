# -*- coding: utf-8 -*-

import os
import json
from random import choice
from uuid import uuid4

def create_directory(path):
    """Create a directory if it does not exist."""
    if not os.path.exists(path):
        os.makedirs(path)

def load_settings(file_path):
    """Load settings from a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Settings file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in settings file.")

def load_word_list(file_path):
    """Load a list of words from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Word list file not found: {file_path}")

def load_word_permutations(word, base_path):
    """Load permutations for a given word from its corresponding JSON file."""
    file_path = os.path.join(base_path, f"{word}.json")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data.get("permutations", [])
    except FileNotFoundError:
        print(f"Warning: Permutations file not found for word: {word}")
        return []

def generate_substitution_dict(word_list, min_length, max_length, base_path, output_dir):
    """Generate a substitution dictionary and save it to a file."""
    create_directory(output_dir)
    output_file = os.path.join(output_dir, f"{str(uuid4())[:8]}.txt")

    with open(output_file, "w", encoding="utf-8") as key_file:
        for word in word_list:
            if min_length <= len(word) <= max_length:
                permutations = load_word_permutations(word, base_path)
                if permutations:
                    new_word = choice(permutations)
                    key_file.write(new_word + "\n")
                    print(f"{word} -> {new_word}")
                else:
                    key_file.write(word + "\n")
                    print(f"{word} x skipped (no permutations found)")
            else:
                key_file.write(word + "\n")
                print(f"{word} x skipped (too long or too short)")

def encrypt_message(message, key_file_path, word_list):
    """Encrypt a message using a substitution dictionary."""
    try:
        with open(key_file_path, "r", encoding="utf-8") as file:
            key_words = file.read().splitlines()
        cipher_dict = {original: substituted for original, substituted in zip(word_list, key_words)}
        return " ".join(cipher_dict.get(word, word) for word in message.lower().split())
    except FileNotFoundError:
        raise FileNotFoundError(f"Key file not found: {key_file_path}")

def decrypt_message(message, key_file_path, word_list):
    """Decrypt a message using a substitution dictionary."""
    try:
        with open(key_file_path, "r", encoding="utf-8") as file:
            key_words = file.read().splitlines()
        decipher_dict = {substituted: original for original, substituted in zip(word_list, key_words)}
        return " ".join(decipher_dict.get(word, word) for word in message.lower().split())
    except FileNotFoundError:
        raise FileNotFoundError(f"Key file not found: {key_file_path}")

if __name__ == "__main__":
    SETTINGS_PATH = "settings.json"
    OUTPUT_DIR = "d_keys"

    settings = load_settings(SETTINGS_PATH)
    word_list = load_word_list(settings["word_lst_pth"])

    generate_substitution_dict(
        word_list=word_list,
        min_length=settings["MIN_LENGTH"],
        max_length=settings["MAX_LENGTH"],
        base_path="G:/T3/",
        output_dir=OUTPUT_DIR
    )

    # Example usage
    example_message = "il se dit il faut que je gagne dix heures et je prendrai mon arme à américain"
    key_path = os.path.join(OUTPUT_DIR, "example_key.txt")

    encrypted = encrypt_message(example_message, key_path, word_list)
    print("Encrypted:", encrypted)

    decrypted = decrypt_message(encrypted, key_path, word_list)
    print("Decrypted:", decrypted)




