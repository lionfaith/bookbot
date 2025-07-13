from stats import count_words, construct_char_count, sort_char_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def pretty_print_sorted_char_count( scc ):
    for e in scc:
        print( f"{e["char"]}: {e["num"]}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    bookpath = sys.argv[1]
    s = get_book_text(bookpath)
    # print(get_book_text(s))
    word_count = count_words(s)
    char_count = construct_char_count(s)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    pretty_print_sorted_char_count( sort_char_count( char_count ) )

main()