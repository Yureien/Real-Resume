def to_title_case(input_string):
    exceptions = {
        "a",
        "an",
        "the",
        "and",
        "but",
        "or",
        "nor",
        "for",
        "so",
        "yet",
        "on",
        "in",
        "at",
        "by",
        "from",
        "to",
        "as",
        "with",
    }
    words = input_string.split()
    title_case_words = []

    for i, word in enumerate(words):
        if i == 0 or word.lower() not in exceptions:
            title_case_words.append(word.capitalize())
        else:
            title_case_words.append(word.lower())

    return " ".join(title_case_words)
