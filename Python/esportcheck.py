from time import sleep
import bs4
import os
import re
import requests
import pyperclip

# team = {
#     "name": "",
#     "dates: ": "",
#     "weekday": "",
#     "time": "",
#     "location": "",
#     "trainer": "",
#     "signupDays": 0,
#     "freeSpaces": 0,
#     "priceDKK": 0
# }

LIST_PATTERN = r"(.*)(\d{2}-\d{2}-\d{4} - \d{2}-\d{2}-\d{4})\(Samlet tilmelding til (\d*) dage\)"
DAYTIME_PATTERN = r"(.*)(\d{2}:\d{2} - \d{2}:\d{2})"
INFO_PATTERN = r"(.*)\d{2}:\d{2} - \d{2}:\d{2}(.*?)(\d+) ledige pladserDKK  (\d+)"

url = "https://rffi.halbooking.dk/newlook/proc_liste.asp"

os.system("mode con: cols=20 lines=3")


def get_table() -> bs4.element.Tag:
    response = requests.get(url)
    pyperclip.copy(response.text)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    selector = '#content > div > div > div > div.boxmain.padding10 > table > tbody'
    table = soup.select(selector)[0]
    return table


def get_teams(table: bs4.element.Tag) -> list[dict]:
    team_trs = []
    for el in table:
        classes = el["class"]
        if len(classes) == 1 and classes[0] == "infinite-item":
            team_trs.append(el)

    teams = []
    for team_tr in team_trs:
        teams.append(get_team_info(team_tr))

    return teams


def get_team_info(team_tr: bs4.element.Tag) -> dict:
    team_info = {}
    for el in team_tr:
        if not isinstance(el, bs4.element.Tag):
            continue
        if is_team_list(el):
            list_value = el.select("span")[0].text
            list_match = re.match(LIST_PATTERN, list_value)
            if list_match is not None:
                team_info["name"] = list_match.group(1)
                team_info["dates"] = list_match.group(2)
                team_info["signupDays"] = int(list_match.group(3))
            daytime_value = el.select("div")[0].text
            daytime_match = re.match(DAYTIME_PATTERN, daytime_value)

            if daytime_match is not None:
                team_info["weekday"] = daytime_match.group(1)
                team_info["time"] = daytime_match.group(2)

        elif is_team_info(el):
            team_info_value = el.text
            team_info_match = re.match(INFO_PATTERN, team_info_value)
            if team_info_match is None:
                continue
            team_info["location"] = team_info_match.group(1)
            team_info["trainer"] = team_info_match.group(2)
            team_info["freeSpaces"] = int(team_info_match.group(3))
            team_info["priceDKK"] = int(team_info_match.group(4))

    return team_info


def is_team_list(team_tr: bs4.element.Tag) -> bool:
    classes = team_tr["class"]
    return len(classes) == 2 and set(classes) == {"liste_wide", "min992"}


def is_team_info(team_tr: bs4.element.Tag) -> bool:
    classes = team_tr["class"]
    return len(classes) == 3 and set(classes) == {"liste_wide", "min992", "holdinfo"}


def main():
    while True:
        table = get_table()
        teams = get_teams(table)
        for team in teams:
            if "overwatch".casefold() in team["name"].casefold():
                print("Tilmeldinger:", 10 - team["freeSpaces"])
                print("Ledige pladser:", team["freeSpaces"])
        sleep(60)


if __name__ == "__main__":
    main()
