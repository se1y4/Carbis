from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import dadata
import os

token = os.getenv('API_KEY')
secret = os.getenv('SECRET_KEY')

dadata_api = dadata.Dadata(token, secret)

result = dadata_api.suggest(name="address", query="Москва", language="en")
print(result)