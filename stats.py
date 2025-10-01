def get_num_words(text: str) -> int:
    """Return the number of words in `text` using a simple whitespace split.

    This mirrors the previous behavior of count_words in `main.py`.
    """
    if not text:
        return 0
    return len(text.split())


def get_char_counts(text: str) -> dict:
    """Return a dict mapping lowercased characters to their occurrence counts.

    Counts every character in the string (including whitespace and symbols).
    Characters are converted to lowercase so that 'A' and 'a' are counted
    together.
    """
    counts = {}
    if not text:
        return counts
    for ch in text.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def sort_char_counts(counts: dict) -> list:
    """Convert a char->count dict into a list of {'char': c, 'num': n}

    - Skips any character for which .isalpha() is False.
    - Uses a helper function and the list.sort() method to sort by the
      'num' key in descending order (greatest to least).
    """
    items = []
    if not counts:
        return items
    for ch, num in counts.items():
        # only include alphabetical characters per the spec
        if not ch.isalpha():
            continue
        items.append({"char": ch, "num": num})

    def _by_num(d: dict) -> int:
        # helper used by .sort()
        return d["num"]

    # sort in-place from greatest to least
    items.sort(key=_by_num, reverse=True)
    return items
