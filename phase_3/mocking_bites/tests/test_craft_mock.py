from unittest.mock import Mock



def test_assert_that_mock_was_called():
        fake_object = Mock()

        fake_object.speak("Steve")
    # Write an assertion below that the method "s
    # the argument. "Steve"
        fake_object.speak.assert_called_with("Steve")
def test_creates_mock_for_specific_case ():
    fake_diary = Mock ()
    # Set up this mock to pass the tests below
    fake_diary.count_entries.return_value = 2
    # Don't edit below
    fake_diary.add(Mock())
    fake_diary.add (Mock())
    assert fake_diary.count_entries () == 2