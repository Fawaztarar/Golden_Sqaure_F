
from lib.diary_entry import *
from lib.diary import *
from datetime import date
def test_diary_entry_constructs () :
        entry = DiaryEntry("My Title", "My Contents")
        assert entry.title == "My Title"
        assert entry.contents == "My Contents"



#empty diary test function

# def test_diary_entry_initialization():
#     test_date = date.today()
#     test_title = "Design_class_system"
#     test_content = "This is entry for my diary"
    
#     entry = diary_entry(test_date, test_title, test_content)

#     # Assert that the attributes are correctly set
#     assert entry.date == test_date
#     assert entry.title == test_title
#     assert entry.content == test_content




def test_adding_and_retrieving_diary_entries():
    pass