import pandas as pd

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from dotenv import load_dotenv
import os

load_dotenv()
# Insira suas credenciais aqui
CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Configuração do gerenciador de credenciais
client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_artist_data(artist_name):
    """
    Busca informações sobre um artista no Spotify.
    """
    result = sp.search(q=artist_name, type='artist', limit=1)
    if result['artists']['items']:
        artist = result['artists']['items'][0]
        artist_data = {
            'name': artist['name'],
            'id': artist['id'],
            'popularity': artist['popularity'],
            'genres': artist['genres']
        }
        return artist_data
    else:
        return None
    
# Teste com um artista
artist_name = "Marília Mendonça"
artist_data = get_artist_data(artist_name)
print(artist_data)




