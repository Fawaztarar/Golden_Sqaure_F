
from lib.music_library import *
from lib.tracks import *

class TestMusicLibraryIntegration:
    def setUp(self):
        self.library = MusicLibrary()
        self.track1 = Track("Song by John", "John Artist")
        self.track2 = Track("Another Song", "Another Artist")

    def test_integration(self):
        self.library.add(self.track1)
        self.library.add(self.track2)
        results = self.library.search("John")
        self.assertEqual(results, [self.track1])

