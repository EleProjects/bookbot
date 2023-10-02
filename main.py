with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def num_words(book_text):
    words = file_contents.split()
    total_words = 0
    for i in range(0, len(words)):
        total_words += 1
    print(total_words)

num_words(file_contents)