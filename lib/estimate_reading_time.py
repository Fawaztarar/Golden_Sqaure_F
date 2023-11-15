
def estimate_reading_time(text):
    if text == "":
        raise Exception ("Can't estimate reading time for an empty text.")
    words = text.split()
    words_count = len(words)
    return words_count / 200

