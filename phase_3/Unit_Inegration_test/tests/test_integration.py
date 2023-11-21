import unittest
from lib.music_library import MusicLibrary
from lib.tracks import Track

class TestMusicLibraryIntegration(unittest.TestCase):
    def setUp(self):
        self.library = MusicLibrary()
        self.track1 = Track("Imagine", "John Lennon")
        self.track2 = Track("Yesterday", "The Beatles")

    def test_integration(self):
        self.library.add(self.track1)
        self.library.add(self.track2)
        results = self.library.search("John")
        self.assertEqual(results, [self.track1])

if __name__ == '__main__':
    unittest.main()