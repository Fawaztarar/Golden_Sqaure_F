import re
class PhoneNumberExtractor () :
    def __init__(self, diary) :
        self. _diary = diary
    
    

    def extract (self):
        phone_numbers = [] 
        for entry in self._diary.all ():
            contents = entry. contents
        phone_numbers += re.findall (r"0[0-9]{10]", contents)
        unique_phone_numbers = [] 
        for phone_number in phone_numbers:
            if not phone_number in unique_phone_numbers:
                unique_phone_numbers.append (phone_number)
        return unique_phone_numbers
    
    
    def extract (self):
        phone_numbers = set
        for entry in self._diary.all():
            found_numbers = re.findall(r"\bo[0-9]{10}\b", entry.contents)
            phone_numbers. update (found_numbers)
        return phone_numbers