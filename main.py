import sys

from stats import count_chars, count_words, get_chars_list


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    chars_count = count_chars(text)
    chars_list = get_chars_list(chars_count)

    chars_counts: list[str] = []
    for e in chars_list:
        if e["char"].isalpha():
            chars_counts.append("{}: {}".format(e["char"], e["num"]))

    s = """\
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
{chars_count_str}
============= END ===============
    """.format(
        book_path=book_path,
        word_count=word_count,
        chars_count_str="\n".join(chars_counts),
    )

    print(s)


main()
