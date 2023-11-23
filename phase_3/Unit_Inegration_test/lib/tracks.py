class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def matches(self, keyword):
        # Check if the keyword matches the title or artist (case insensitive)
        return keyword.lower() in self.title.lower() or keyword.lower() in self.artist.lower()