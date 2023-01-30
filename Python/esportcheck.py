from time import sleep
import bs4
import os
import re
import requests

url = "https://rffi.halbooking.dk/newlook/proc_liste.asp"
os.system("mode con: cols=25 lines=4")

def get_spaces() -> str:
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    selector = "#item13286 > td.liste_wide.min992.holdinfo"
    td = str(soup.select(selector)[0])
    pattern = r"\d+ ledige pladser"
    return re.findall(pattern, td)[0]


if __name__ == "__main__":
    while True:
        print(get_spaces())
        sleep(10)
