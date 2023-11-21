class ReadableEntryExtractor () :
    def __init__(self, diary):
        self._diary = diary
    
    

    def extract (self, wpm, minutes) :
        entries = self. _diary.all ()
        if self._entry_readable_in_tJme(wpm, minutes, entries [0]):
            return entries [e]
        else:
            return None
        

    def extract (self, wpm, minutes) :
        readable_entries = self._find_readable_entries (wpm, minutes)
        if len (readable_entries) == 0:
            return None     
        return max (readable_entries,
key=lambda entry: self._count_words (entry contents))


    def _find_readable_entries (self, wpm, minutes) :
        return [ 
            entry for entry in self._diary.all ()
        if self._is_entry_readable_in_time (wpm, minutes, entry)]
    







        
    def entry_readable_in_time (self, wpm, minutes, entry) :
        length_readable = wpm * minutes 
        return self._word_count (entry.contents) <= length_readable
    def _word_count(self, string):
        return len(string.split(" ."))