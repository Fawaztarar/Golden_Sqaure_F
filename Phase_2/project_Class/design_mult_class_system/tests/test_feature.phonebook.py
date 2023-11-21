def test_extracts_phone_numbers () :
    diary = Diary ()
    entry_1 = DiaryEntry ("My Title 1", "My friend is 07800000000 and 078")
    entry_2 = DiaryEntry ("My Title 2", "My Contents 2")
    entry_3 = DiaryEntry("My Title 3", "My friend is 07800000002")
    diary.add(entry_1)
    diary.add (entry_2)
    diary.add (entry_3)
    extractor = PhoneNumberExtractor (diary)
    assert extractor.extract|() == ["o7800000000", "07800000001", "0780000006"]