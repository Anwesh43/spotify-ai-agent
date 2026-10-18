from tools.spotify_tools import searchItem, getArtistDetails
import json 
from typing import Dict 

def writeFile(data : Dict, fileName : str):
    with open(fileName, "w") as f:
        f.write(json.dumps(data))
    print(f"Wrting data to {fileName}")

if __name__ == "__main__":
    writeFile(searchItem("Kanye West", itemType="artist"), "test_search.json")
    