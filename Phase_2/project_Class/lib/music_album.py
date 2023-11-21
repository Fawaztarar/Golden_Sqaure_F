#EMPTY TRACK LIST

#ADD TRACK

#LIST ADDED TRACKS

#REMOVE TRACK

class musicAlbum:

    def __init__(self):
        self._tracks = []

    def add_track(self, track):
        self._tracks.append(track)

    def list_track(self):
        return self._tracks
    
    def remove_track(self, track):
        if track in self._tracks:
            self._tracks.remove(track)

    

