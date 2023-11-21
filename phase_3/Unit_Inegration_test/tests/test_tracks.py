from lib.tracks import Track
import unittest
class TestTrack(unittest.TestCase):
    def setUp(self):
        self.track = Track("Bohemian Rhapsody", "Queen")

    def test_init(self):
        self.assertEqual(self.track.title, "Bohemian Rhapsody")
        self.assertEqual(self.track.artist, "Queen")

    def test_matches_true(self):
        self.assertTrue(self.track.matches("Bohemian"))

    def test_matches_false(self):
        self.assertFalse(self.track.matches("Yesterday"))

if __name__ == '__main__':
    unittest.main()