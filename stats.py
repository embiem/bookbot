from typing import Dict, TypedDict


def count_words(text: str):
    return len(text.split())


def count_chars(text: str) -> Dict[str, int]:
    dic = {}
    for c in text:
        cl = c.lower()
        if cl in dic:
            dic[cl] = dic[cl] + 1
        else:
            dic[cl] = 1

    return dic


class CharCount(TypedDict):
    char: str
    num: int


def get_chars_list(char_counts: Dict[str, int]) -> list[CharCount]:
    lst = []
    for key, val in char_counts.items():
        lst.append({"char": key, "num": val})
    return sorted(lst, key=lambda x: x["num"], reverse=True)
