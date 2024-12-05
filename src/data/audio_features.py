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

def get_audio_features(track_ids):
    """
    Obtém características sonoras de uma lista de faixas.
    """
    features = sp.audio_features(track_ids)
    return features

# Teste com algumas faixas populares (exemplo: IDs de faixas)
track_ids = ['3n3PqQOZtpnq6c97tGUy6a', '0VjIjW4GlUZAMYd2vXMi3b']  # IDs de exemplo
audio_features = get_audio_features(track_ids)
print(audio_features)

#https://developer.spotify.com/documentation/web-api/reference/get-audio-features