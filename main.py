""" 
Make a grid that can print words that are passed in as command line arguments.

There should be a max limit of characters per line, and total amount of characters per page.
As words wrap the characters should take up less space as to accomodate the total amount of characters per line.
"""
import argparse
import os
import sys
import logging
from typing import List
from letter_class import Letter


logging.basicConfig(level=logging.ERROR)


def store_sentence(words: List[str], letter_representation: dict[str, list[list[str]]]):
    terminal_width = os.get_terminal_size().columns
    sentence = []
    word_group = []
    current_width = 0
    for word in words:
        word_representation = []
        word_width = 0
        for letter in word:
            single_letter_representation = letter_representation[letter.upper()]
            word_representation.append(single_letter_representation)
            letter_width = (
                max(len("".join(line)) for line in single_letter_representation) + 1
            )
            word_width += letter_width
        if current_width + word_width + len(word_group) * 4 > terminal_width:
            sentence.append(word_group)
            word_group = [word_representation]
            current_width = word_width
        else:
            word_group.append(word_representation)
            current_width += word_width
    if word_group:
        sentence.append(word_group)
    return sentence


def print_sentence(word_group):
    for i in range(5):
        for word_representation in word_group:
            for letter_representation in word_representation:
                printed_string = "".join(letter_representation[i])
                print("\033[33m" + printed_string, end="")
            print("    ", end="")
        print()


def main(words: str, letter_representation: dict[str, list[list[str]]]):
    words = words.split()

    sentence = store_sentence(words, letter_representation)
    for word_group in sentence:
        print_sentence(word_group)
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Print words on a grid")

    parser.add_argument(
        "words",
        type=str,
        nargs="?",
        help="The sentence to print. Must pass in as a continuous string.\nExample: bigwords 'this is a bigg ol sentence'",
    )

    args = parser.parse_args()

    if args.words is None:
        logging.error("Please pass in a sentence to print")
        sys.exit(1)

    elif not isinstance(args.words, str):
        logging.error("Argument must be a string")
        sys.exit(1)

    l = Letter()
    l.set_spacing()
    letter_representation = l.get_letter_representation()

    main(words=args.words, letter_representation=letter_representation)
