import sys

def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        return file_contents

def word_count(file_contents):
    num_words = len(file_contents.split())
    print("Found",num_words,"total words")

word_count(get_book_text())

freq = {}

def frequency():
    for c in get_book_text().lower():
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    print(freq)

frequency()
