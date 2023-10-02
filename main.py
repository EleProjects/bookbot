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

def get_value(item):
    return item[1]

num_words = num_words(file_contents)
char_report = sorted(num_of_char(file_contents).items(), key = get_value, reverse = True)


print(f"--- Begin report of {f.name} ---")
print(f"{num_words} words found in the document\n")
for i in range(0, len(char_report)):
    print(f"The '{char_report[i][0]}' character was found {char_report[i][1]} times")

print("--- End report ---")