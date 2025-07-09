def main():
    from stats import count_words, count_characters

    count_words("books/frankenstein.txt")
    char_count = count_characters("books/frankenstein.txt")
    print(char_count)


main()