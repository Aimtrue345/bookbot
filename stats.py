# Reads text file, prints amount of words in a string of text.
def count_words(book_path):
    num_words = 0
    with open(book_path) as f:
        book_contents = f.read()
        words = book_contents.split()
    for word in words:
        num_words = num_words + 1
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

# Reads text file, counts through each character in text and appends to dictionary.
def count_characters(book_path):
    char_count = {}
    with open(book_path) as f:
        book_contents = f.read()
    for char in book_contents.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

# Takes a dictionary and returns the value of the "num" key.

def sort_num(list):
    return list["num"]

# Sort char_count from highest to lowest and filter non-alpha characters.

def sort_char(char_count):
    count_list = []
    for char in char_count:
        count_dict = {}
        num = char_count[char]
        count_dict["char"] = char
        count_dict["num"] = num
        count_list.append(count_dict)
    count_list.sort(reverse=True, key=sort_num)
    print("--------- Character Count -------")
    for count_dict in count_list:
        if count_dict["char"].isalpha() == True:
            print(f"{count_dict["char"]}: {count_dict["num"]}")

        
