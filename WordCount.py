import re
from collections import defaultdict

def func(path):
    word_count = defaultdict(int)
    
    try:
        with open(path, 'r') as f:
            for line in f:
                words = re.findall(r'\b\w+\b', line.lower())
                for word in words:
                    word_count[word] += 1
    except FileNotFoundError:
        print(f"The file {path} does not exist.")
        return
    
    sorted_word_count = dict(sorted(word_count.items()))
    
    for word, count in sorted_word_count.items():
        print(f"{word}: {count}")

path = input("Enter the path to the text file: ")
func(path)