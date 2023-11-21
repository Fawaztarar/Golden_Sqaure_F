from lib.make_snippet import make_snippet



def test_empty_string_snippet():
    result = make_snippet("")

    assert result == ""


def test_four_words_string_snippet():
    result = make_snippet("thomas mathew Jony Fawaz")

    assert result == "thomas mathew Jony Fawaz..."


def test_give_first_five_words_with_elipsis():
    result = make_snippet("thomas mathew Jony Fawaz Ali Henry")

    assert result == "thomas mathew Jony Fawaz Ali..."
