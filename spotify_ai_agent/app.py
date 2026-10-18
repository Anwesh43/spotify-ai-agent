from agents.spotify_agent import recommendUserSpotifyData
import asyncio 
import sys 

if __name__ == "__main__" and len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
    asyncio.run(recommendUserSpotifyData(prompt=prompt)) 