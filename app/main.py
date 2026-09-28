def count_occurrences(phrase: str, letter: str) -> int:

    phrase_lower = phrase.lower()
    counter = int(phrase_lower.count(letter.lower()))
    return counter