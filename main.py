with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def num_words(book_text):
    words = file_contents.split()
    total_words = 0

    for i in range(0, len(words)):
        total_words += 1
    return(total_words)

def num_of_char(book_text):
    characters = {}

    for char in book_text.lower():
        if char.isalpha() and char not in characters:
            characters[char] = 1
        elif char.isalpha() and char in characters:
            characters[char] += 1
    return(characters)
    