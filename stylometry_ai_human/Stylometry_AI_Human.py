import json
import re
import math


with open("stylometry.json", "r", encoding="utf-8") as file:
    data = json.load(file)



def extract_features(text):

    # ---------- WORD FEATURES ----------
    words = re.findall(r"\w+", text)
    lower_words = [word.lower() for word in words]

    word_count = len(words)
    unique_words = len(set(lower_words))

    ttr = unique_words / word_count if word_count > 0 else 0

    word_lengths = [len(word) for word in words]

    avg_word_length = (
        sum(word_lengths) / len(word_lengths)
        if word_lengths else 0
    )

    long_words = len([word for word in words if len(word) > 6])
    short_words = len([word for word in words if len(word) <= 3])


    # ---------- SENTENCE FEATURES ----------
    sentences = re.split(r"[.!?]+", text)

    sentences = [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]

    sentence_lengths = []

    for sentence in sentences:
        sentence_words = re.findall(r"\w+", sentence)
        sentence_lengths.append(len(sentence_words))

    sentence_count = len(sentences)

    avg_sentence_length = (
        sum(sentence_lengths) / sentence_count
        if sentence_count > 0 else 0
    )

    min_sentence_length = (
        min(sentence_lengths)
        if sentence_lengths else 0
    )

    max_sentence_length = (
        max(sentence_lengths)
        if sentence_lengths else 0
    )


    # ---------- CHARACTER FEATURES ----------
    character_count = len(text)

    letters = len(re.findall(r"[A-Za-z]", text))
    digits = len(re.findall(r"\d", text))
    spaces = len(re.findall(r"\s", text))

    uppercase = len(re.findall(r"[A-Z]", text))
    lowercase = len(re.findall(r"[a-z]", text))


    # ---------- PUNCTUATION ----------
    periods = len(re.findall(r"\.", text))
    commas = len(re.findall(r",", text))
    questions = len(re.findall(r"\?", text))
    exclamations = len(re.findall(r"!", text))
    apostrophes = len(re.findall(r"'", text))


    # ---------- RATIOS ----------
    character_density = (
        character_count / word_count
        if word_count > 0 else 0
    )

    uppercase_ratio = (
        uppercase / letters
        if letters > 0 else 0
    )

    digit_ratio = (
        digits / character_count
        if character_count > 0 else 0
    )

    space_ratio = (
        spaces / character_count
        if character_count > 0 else 0
    )


    # ---------- FUNCTION WORDS ----------
    function_words = [
        "the", "a", "an", "and", "or",
        "but", "of", "to", "in", "for",
        "with", "on", "is", "was",
        "are", "I", "we", "you"
    ]

    function_word_count = 0

    for word in function_words:
        function_word_count += lower_words.count(word)


    return {
        "word_count": word_count,
        "unique_words": unique_words,
        "ttr": ttr,
        "avg_word_length": avg_word_length,
        "long_words": long_words,
        "short_words": short_words,

        "sentence_count": sentence_count,
        "avg_sentence_length": avg_sentence_length,
        "min_sentence_length": min_sentence_length,
        "max_sentence_length": max_sentence_length,

        "character_count": character_count,
        "letters": letters,
        "digits": digits,
        "spaces": spaces,
        "uppercase": uppercase,
        "lowercase": lowercase,

        "periods": periods,
        "commas": commas,
        "questions": questions,
        "exclamations": exclamations,
        "apostrophes": apostrophes,

        "character_density": character_density,
        "uppercase_ratio": uppercase_ratio,
        "digit_ratio": digit_ratio,
        "space_ratio": space_ratio,

        "function_word_count": function_word_count
    }


human_features = extract_features(data[0]["text"])
ai_features = extract_features(data[1]["text"])


print("\nSTYLOMETRIC COMPARISON")

print(f"{'Feature':30} {'Human':>12} {'AI':>12}")
print("-" * 60)

for feature in human_features:

    human_value = human_features[feature]
    ai_value = ai_features[feature]

    if isinstance(human_value, float):
        print(
            f"{feature:30} "
            f"{human_value:12.3f} "
            f"{ai_value:12.3f}"
        )
    else:
        print(
            f"{feature:30} "
            f"{human_value:12} "
            f"{ai_value:12}"
        )