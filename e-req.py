import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=51.5085&longitude=-0.1257&current_weather=true"

resp = requests.get(url)
rj = resp.json()
print(rj)
# print(rj["elevation"])