from lib.count_words import count_words

def test_count_words():
    result = count_words("fawaz")
    assert result ==  5


def test_count_words():
    result = count_words("james")
    assert result == 5