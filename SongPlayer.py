class SongPlayer:
    # Object initializer
    def __init__(self) -> None:
        pass
    
    # Import song(s)
    def importSongs(self) -> None:
        raise NotImplementedError()

    # Read song(s) -> list[songs]
    def readSongs(self) -> list[str]:
        raise NotImplementedError()

    # Create song info
    def createSongInfo(self, fileName: str, **options) -> dict:
        """Method that creates song details."""
        for key, value in options:
            if key is "songTitle":
                songTitle = value
            if key is "songArtist":
                songArtist = value
            if key is "songAlbum":
                songAlbum = value
            if key is "songYear":
                songYear = value
        
        songInfo = {
            "fileName" : fileName,
            "songTitle" : songTitle,
            "songArtist" : songArtist,
            "songAlbum" : songAlbum,
            "songYear" : songYear
        }

        raise NotImplementedError()

    # Edit song info
    def editSongInfo(self, fileName: str, *options):
        raise NotImplementedError()

    # Delete song info
    def deleteSongInfo(self, fileName: str):
        raise NotImplementedError()

    # Create playlist
    def createPlaylist(self, playlistName: str):
        raise NotImplementedError()

    # Delete playlist
    def deletePlaylist(self, playlistName: str):
        raise NotImplementedError()
    
    # Add song to playlist
    def addSongToPlaylist(self, fileName: str, playlistName: str):
        raise NotImplementedError()

    # Delete song from playlist
    def deleteSongFromPlaylist(self, fileName: str, playlistName: str):
        raise NotImplementedError()
