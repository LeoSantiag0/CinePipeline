from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Pega a chave da API guardada em .env
api_key = os.getenv("TMDB_API_KEY")

# Retorna mensagem de erro caso não encontre apikey grava no .env
if not api_key:
    raise ValueError("Chave da API TMDB não encontrada. Verifique o arquivo .env")