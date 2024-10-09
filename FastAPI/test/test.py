import requests
from pydantic import BaseModel


url = "http://172.30.1.45:8000"

response = requests.get(url)

print(response)

url = url+"/items"

response = requests.get(url, params={"a": 1})
