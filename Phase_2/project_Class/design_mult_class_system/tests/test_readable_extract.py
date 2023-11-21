def test_gets_single_entry_that_fits_in_the_time () :
    diary = Diary ()
    entry_1 = DiaryEntry("Title",
    "one two three four")
    diary.add(entry_1)
    extractor = ReadableEntryExtractor (diary)
    assert extractor.extract (wpm=2, minutes=2) == entry_1