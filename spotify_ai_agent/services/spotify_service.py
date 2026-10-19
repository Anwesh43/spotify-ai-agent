from services.base_http_client import BaseHTTPClient 
from dotenv import load_dotenv 
import base64
import os 

load_dotenv()

class SpotifyService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["SPOTIFY_BASE_URL"])
        self.headers = {
            "Authorization": f"Bearer {self._authorize()}"
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
            response = self.client.getCall(f"albums/{albumId}", qpParams={}, headers = self.headers)
            tracks = response["tracks"]["items"]
            newTracks = []
            for track in tracks:
                trackObj = {}
                trackObj["id"] = track["id"]
                trackObj["name"] = track["name"]
                newTracks.append(trackObj)
            response["tracks"] = newTracks
            return response
        except Exception as e:
            return self._handleError(e)

    def getArtistAlbums(self, artistId : str):
        try:
            response = self.client.getCall(f"artists/{artistId}/albums", qpParams={}, headers = self.headers)
            if "items" in response:
                albums = response["items"]
                results = []
                for track in albums:
                    obj = {}
                    obj["id"] = track["id"]
                    obj["name"] = track["name"]
                    results.append(track)
                return results 
        except Exception as e:
            return self._handleError(e)

    def _authorize(self):
        try:
            authClient = BaseHTTPClient("https://accounts.spotify.com")
            authString = f"{os.environ["SPOTIFY_CLIENT_ID"]}:{os.environ["SPOTIFY_CLIENT_SECRET"]}"
            authBytes = authString.encode("utf-8")
            authHeader = str(base64.b64encode(authBytes), "utf-8")
            data = {
                "grant_type": "client_credentials"
            }
            headers = {
                "Content-type": "application/x-www-form-urlencoded",
                "Authorization": f"Basic {authHeader}"
            }
            response = authClient.postCallFormEncoded("api/token", data = data, headers=headers)
            print("Auth succeeded")
            return response["access_token"]
        except Exception as e:
            return self._handleError(e)

    def getAudioFeaturesOfTrack(self, trackId: str):
        try:
            response = self.client.getCall(f"audio-features/{trackId}", qpParams={}, headers = self.headers)
            return response
        except Exception as e:
            return self._handleError(e)

    def getShowDetails(self, showId : str):
        try:
            response = self.client.getCall(f"shows/{showId}", qpParams={}, headers=self.headers)
            resultObj = {}
            resultObj["description"] = response["description"]
            if "name" in response:
                resultObj["name"] = response["name"]
            resultObj["episodes"] = []
            if "episodes" in response and "items" in response["episodes"]:
                items = response["episodes"]["items"]
                for item in items:
                    resultObj["epsiodes"].append({"id": item["id"]})
            return resultObj

        except Exception as e:
            return self._handleError(e)

    def getEpisodeDetails(self, episodeId : str):
        try:
            response = self.client.getCall(f"episodes/{episodeId}", qpParams={}, headers=self.headers)
            return response 
        except Exception as e:
            return self._handleError(e)


    def getAudioBookDetails(self, audioBookId : str):
        try:
            response = self.client.getCall(f"audiobooks/{audioBookId}", qpParams={}, headers=self.headers)
            return response 
        except Exception as e:
            return self._handleError(e)

    def getAudioBookChapterDetails(self, chapterId : str):
        try:
            response = self.client.getCall(f"chapters/{chapterId}", qpParams={}, headers=self.headers)
            return response 
        except Exception as e:
            return self._handleError(e)