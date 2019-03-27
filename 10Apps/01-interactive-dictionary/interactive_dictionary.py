#!/usr/bin/env python3
import json
import sys
from difflib import get_close_matches
data = json.load(open("data.json",'r'))
usage = """
interactive_dictionary.py <word>
  <word>      A word to find in dictionary
"""

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        # we always return a list
        matched = ["Word not found"]
        matches = get_close_matches(word, data.keys(), 1, 0.7)
        if len(matches) == 1:
            yn = input("Did you mean %s instead? Press Y for yes, N for No > " % matches[0]).upper()
            if yn == 'Y':
                matched = data[matches[0]]
        return matched
if __name__ == "__main__":
    if len(sys.argv) > 1:
        for item in translate(sys.argv[1]):
            print(item)
    else:
        print("Not enough arguments")
        print(usage)
