from services.base_http_client import BaseHTTPClient 
from dotenv import load_dotenv 
import os 

load_dotenv()

class SpotifyService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["SPOTIFY_BASE_URL"])
        self.headers = {
            "Authorization": f"Bearer {os.environ["SPOTIFY_API_KEY"]}"
        }

    def _handleError(self, e):
        print("Error", e)
        return {
            "status": "Error",
            "message": str(e)
        }
    
    def searchItem(self, query : str, queryType : str):
        try:
            qpParams = {
                "q": query,
                "type": queryType
            }
            response = self.client.getCall("search", qpParams=qpParams, headers = self.headers)
            return response 
        except Exception as e:
            return self._handleError(e)


    def getItemTypes(self):
        return [
            "album", "artist", "playlist", "track", "show", "episode", "audiobook"
        ]

    def getArtist(self, artistId : str):
        try:
            return self.client.getCall(f"artists/{artistId}", qpParams={}, headers=self.headers)
        except Exception as e:
            return self._handleError(e)
    

    def getTrackDetails(self, trackId : str):
        try:
            return self.client.getCall(f"tracks/{trackId}", qpParams={}, headers=self.headers)
        except Exception as e:
            return self._handleError(e)
        
    def getAlbumDetails(self, albumId : str):
        try:
            return self.client.getCall(f"albums/{albumId}", qpParams={}, headers = self.headers)
        except Exception as e:
            return self._handleError(e)

    def getArtistTopTracks(self, artistId : str):
        try:
            response = self.client.getCall(f"artists/{artistId}/top-tracks", qpParams={}, headers = self.headers)
            if "tracks" in response:
                tracks = response["tracks"]
                results = []
                for track in tracks:
                    obj = {}
                    obj["id"] = track["id"]
                    obj["name"] = track["name"]
                    if "album" in track:
                        obj["albumName"] = track["album"]["name"]
                        obj["albumId"] = track["album"]["id"]
                    results.append(track)
                return results 
        except Exception as e:
            return self._handleError(e)

    def getAudioFeaturesOfTrack(self, trackId: str):
        try:
            response = self.client.getCall(f"audio-features/{trackId}", qpParams={}, headers = self.headers)
            return response
        except Exception as e:
            return self._handleError(e)
    

    
