#importamos las librerias
import os
import openai
from dotenv import load_dotenv, find_dotenv

# carga y pruebas con apikey de openai

test_enviorment = load_dotenv(find_dotenv())
print(test_enviorment)

openai_api_key=os.environ['OPENAI_API_KEY']  

