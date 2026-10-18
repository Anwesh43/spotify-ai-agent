from services.spotify_service import SpotifyService

ss = SpotifyService()

def getItemTypes():
    print(f"Calling getItemTypes tool")
    return ss.getItemTypes()

def searchItem(query : str, itemType: str):
    print(f"Calling searchItem {query} and {itemType}")
    return ss.searchItem(query=query, queryType=itemType)

def getArtistDetails(artistId : str):
    print(f"Calling getArtistDetails tool {artistId}")
    return ss.getArtist(artistId=artistId)

def getArtistAlbums(artistId : str):
    print(f"Calling getArtistAlbums tool for {artistId}")
    return ss.getArtistAlbums(artistId=artistId)

def getTrackDetails(trackId : str):
    print(f"Calling getTrackDetails tool for {trackId}")
    return ss.getTrackDetails(trackId)

def getAudioFeaturesOfTrack(trackId: str):
    print(f"Calling getAudioFeaturesOfTrack tool for {trackId}")
    return ss.getAudioFeaturesOfTrack(trackId=trackId)

def getAlbumDetails(albumId : str):
    print(f"Calling getAlbumDetails tool {albumId}")
    return ss.getAlbumDetails(albumId=albumId)


def getAvailableTools():
    return [
        getItemTypes, searchItem, getArtistDetails, getArtistAlbums, getTrackDetails, getAlbumDetails 
    ]