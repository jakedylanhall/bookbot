import sys

def get_book_text(filepath: str) -> str:
    """Return the contents of the file at `filepath` as a string.

    Raises FileNotFoundError if the file does not exist.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def main() -> None:
    # require exactly one CLI argument: the path to the book
    if len(sys.argv) != 2:
        # exact message required by the tests
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    text = get_book_text(path)

    # import stats functions here to match your previous structure
    from stats import get_num_words, get_char_counts, sort_char_counts

    num_words = get_num_words(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    char_counts = get_char_counts(text)
    sorted_chars = sort_char_counts(char_counts)

    for entry in sorted_chars:
        ch = entry["char"]
        num = entry["num"]
        print(f"{ch}: {num}")

    print("============= END ===============")


def count_words(text: str) -> int:
    # kept for backward compatibility
    from stats import get_num_words
    return get_num_words(text)


if __name__ == "__main__":
    main()
