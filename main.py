def main():
    import sys
    from stats import count_words, count_characters, sort_char

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        count_words(book_path)
        char_count = count_characters(book_path)
        sort_char(char_count)
        print("============= END ===============")
    

main()