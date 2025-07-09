# Reads text file, prints amount of words in a string of text.
def count_words(book_path):
    num_words = 0
    with open(book_path) as f:
        book_contents = f.read()
        words = book_contents.split()
    for word in words:
        num_words = num_words + 1
    print(f"{num_words} words found in the document")

# Reads text file, counts through each character in text and appends to dictionary.
def count_characters(book_path):
    char_count = {}
    with open(book_path) as f:
        book_contents = f.read()
    for char in book_contents.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count



        
