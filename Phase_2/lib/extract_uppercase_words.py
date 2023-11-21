def extract_uppercase_words(str):
    words = str.split()
    return [word for word in words if word.isupper()]


#for last one
def extract_uppercase_words_with_punctutatuion(str):
    words = str.split()

    # Creating a list to hold the uppercase words
    uppercase_words = []

    for word in words:
        # Removing punctuation by keeping only alphabetic characters
        cleaned_word = ''.join(char for char in word if char.isalpha())

        # Checking if the cleaned word is in uppercase
        if cleaned_word.isupper():
            uppercase_words.append(cleaned_word)

    return uppercase_words
