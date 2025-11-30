from stats import get_all_words, get_num_words, get_char_count, get_sorted_dict
import sys



def main():
    if len(sys.argv) != 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    all_words = get_all_words(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    num_words = get_num_words(all_words)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    all_char_count = get_char_count(all_words)
    all_char_count_sorted = get_sorted_dict(all_char_count)
    print("--------- Character Count -------")
    for key, val in all_char_count_sorted.items():
        print(f"{key}: {val}")

main()
