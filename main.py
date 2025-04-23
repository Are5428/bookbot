from stats import words_count, char_count, dict_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    txt_msg = get_book_text(book_path)
    num_words = words_count(txt_msg)
    char_dict = char_count(txt_msg)
    char_sorted_list = dict_list(char_dict)
    print_report(book_path, num_words, char_sorted_list)


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    
    print("============ END ============")
main()