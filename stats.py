def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    letter_count = {}
    for letter in text:
        lowered = letter.lower()
        if lowered in letter_count:
            letter_count[lowered] += 1
        else:
            letter_count[lowered] = 1
    return letter_count

def sorted_list(letter_count):
    stats = []
    for letter, count in letter_count.items():
        stats.append({"char" : letter, "num" : count})
    def sort_on(items): return items["num"]
    stats.sort(key=sort_on, reverse=True)
    return stats