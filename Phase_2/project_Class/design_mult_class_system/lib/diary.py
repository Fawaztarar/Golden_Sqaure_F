# Add diary entries.
# Read all diary entries.
# Select diary entries based on estimated reading time 
# and user's available time.


from lib.diary_entry import *


class Diary ():
    def __init__(self):
        self._entries = []


    def add(self, diary_entry):
        self._entries.append(diary_entry)


    def all (self):
        return self._entries



















#
# class Diary:
#     def __init__(self):
#         self.entries = {}


#     def add_entry(self, date, entry):
#         self.entries[entry.date] = entry.content
    
#     def get_entries(self):
#         return [DiaryEntry(date, None, content) for date, content in self.entries.items()]
        

#     def read_entry(self, date):
#         return self.entries.get(date, "No entry found for this date.")


#     def select_entries_for_reading(self, available_time, words_per_minute):
#         pass
#         # Select entries that can be read in the given time

#     def extract_phone_numbers(self):
#         pass