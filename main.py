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

size = os.get_terminal_size()


def store_sentence(words: List[str], letter_representation: dict[str, list[list[str]]]):
    sentence = []
    for word in words:
        word_representation = []
        for letter in word:
            word_representation.append(letter_representation[letter.upper()])
        sentence.append(word_representation)
    return sentence


def print_sentence(sentence):
    for i in range(5):
        for word_representation in sentence:
            for letter_representation in word_representation:
                print("".join(letter_representation[i]), end="")
            print("    ", end="")
        print()


def main(words: str, letter_representation: dict[str, list[list[str]]]):
    words = words.split()

    sentence = store_sentence(words, letter_representation)
    print_sentence(sentence)
    print(size)


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
