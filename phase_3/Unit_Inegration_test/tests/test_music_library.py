import unittest
from lib.music_library import MusicLibrary
from lib.tracks import Track
from unittest.mock import Mock


class TestMusicLibrary(unittest.TestCase):
    def setUp(self):
        self.library = MusicLibrary()
        self.track1 = Track("Bohemian Rhapsody", "Queen")
        self.track2 = Track("Stairway to Heaven", "Led Zeppelin")

    def test_add(self):
        self.library.add(self.track1)
        self.assertIn(self.track1, self.library.tracks)

    def test_search_found(self):
        self.library.add(self.track1)
        self.library.add(self.track2)
        results = self.library.search("Queen")
        self.assertEqual(results, [self.track1])

    def test_search_not_found(self):
        self.library.add(self.track1)
        results = self.library.search("Beatles")
        self.assertEqual(results, [])

if __name__ == '__main__':
    unittest.main()


#MOCKING
    def test_searches_by_keyword():
        library = MusicLibrary ()
        fake_matching = Mock()
        fake_matching.matches.return_value = True
        library.add (fake_matching)
        fake_not_matching = Mock()
        fake_not_matching.matches.return_value = False
        library.add (fake_not_matching)
        assert library.search ("hello") == [fake_matching]