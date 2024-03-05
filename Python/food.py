from bs4 import BeautifulSoup
import requests

MENU_URI = "https://medarbejdere.au.dk/administration/bygninger/bygningsservice/nat-tech-bygningsservice/kontakt-os/kantiner/navitas-kantine"


def get_menu() -> dict:
    response = requests.get(MENU_URI)
    soup = BeautifulSoup(response.text, "html.parser")

    menu = {"Mandag": "", "Tirsdag": "", "Onsdag": "", "Torsdag": "", "Fredag": ""}

    options = soup.select("td h3")
    i = 0
    while True:
        text = options[i].get_text()
        if text in menu:
            food = options[i + 1].get_text()
            food = food.split("\t", 1)[0].strip()
            menu[text] = food

        if i + 1 == len(options):
            break
        i += 1

    return menu


def main():
    menu = get_menu()
    print(menu)


if __name__ == "__main__":
    main()
