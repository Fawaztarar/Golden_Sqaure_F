# implement the following user story in your project. This will be in a new class.

# As a user
# So that I can keep track of my music listening
# I want to add tracks I've listened to and see a list of them.

#EMPTY TRACK LIST

#ADD TRACK

# ADD MULTIPLE TRACKS

#LIST ADDED TRACKS

#REMOVE TRACK

# TEST EMPTY LIST, TEST ADD TRACK , TEST LIST TRACK

from lib.music_album import *

def test_initially_has_no_tracks():
    tracker = musicAlbum()
    tracker.list_track()

def test_add_track_into_albums():
    tracker = musicAlbum()
    tracker.add_track("Song1")
    assert tracker.list_track() == ["Song1"]

def test_add_multiple_tracks_into_albums():
    tracker = musicAlbum()
    tracker.add_track("Song1")
    tracker.add_track("Song2")
    assert tracker.list_track() == ["Song1", "Song2"]

def test_remove_track_from_album():
    tracker = musicAlbum()
    tracker.add_track("Song1")
    tracker.add_track("Song2")
    tracker.remove_track("Song2")
    assert tracker.list_track() == ["Song1"]


    



    
