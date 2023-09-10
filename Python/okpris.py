import requests

data = {
    "varenr": "533",
    "pumpepris": False
}
url = "https://www.ok.dk/privat/produkter/ok-kort/prisudvikling/getProduktHistorik"
r = requests.post(url, json=data)

json = r.json()

print(json["historik"][0]["dato"])
print(json["historik"][0]["pris"])
