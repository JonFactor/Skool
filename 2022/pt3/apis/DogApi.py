import requests

responce = requests.get("https://dog.ceo/api/breeds/image/random")

print(f'STATUS: {responce.status_code} \n TEXT: {responce.text} \n HEADERS: {responce.headers} \n REQUEST HEADERS: {responce.request.headers}')