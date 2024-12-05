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

# Teste inicial: Buscar informações sobre um artista
artist_name = "Taylor Swift"
result = sp.search(q=artist_name, type="artist", limit=1)

# Exibir informações do artista
if result["artists"]["items"]:
    artist = result["artists"]["items"][0]
    print(f"Nome: {artist['name']}")
    print(f"Popularidade: {artist['popularity']}")
    print(f"Gêneros: {', '.join(artist['genres'])}")
    print(f"ID do Artista: {artist['id']}")
else:
    print("Artista não encontrado.")

# try:
#     response = sp.me()
#     print("Autenticação bem-sucedida!")
# except Exception as e:
#     print("Erro de autenticação:", e)