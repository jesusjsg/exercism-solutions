def add_prefix_un(word: str) -> str:
    prefix = "un"
    negative_word = prefix + word
    return negative_word


def make_word_groups(vocab_words: list) -> str:
    prefix = vocab_words[0]
    new_words = [prefix] + [prefix + word for word in vocab_words[1:]]
    return " :: ".join(new_words)


def remove_suffix_ness(word: str) -> str:
    if word.endswith("ness"):
        new_word = word[:-4]
        if new_word.endswith("i"):
            new_word = new_word[:-1] + "y"
        return new_word
    return word


def adjective_to_verb(sentence: str, index: int) -> str:
    words = sentence.split()
    adjective = words[index]
    adjective = adjective.replace(".", "")
    verb = adjective + "en"
    return verb
