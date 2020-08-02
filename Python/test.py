import requests, bs4

res = requests.get('https://www.amazon.co.uk/EVGA-GeForce-Express-1755MHz-14000MHz/dp/B07K6H583G/')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
elems = noStarchSoup.select("._eYtD2XCVieq6emjKBH3m")

print(elems)