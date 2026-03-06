import os
from dotenv import load_dotenv

load_dotenv() 

spotify = os.getenv("SPOTIFY_CLIENT_ID")
print(spotify)

