from bs4 import BeautifulSoup
import requests
import json


def main():

    url = "https://js-trebesin.github.io/bsoup-exam/"
    response = requests.get(url)  # get je python fce <--- U: ?

    soup = BeautifulSoup(
        response.content, "html.parser"
    )  # Pomocí knihovny BeautifulSoup, chceme obsah (content) response. Response nám odkazije na url adresu. "html parser" přetvoří/púřepíše text, aby mu kod rozuměl.

    food = soup.find_all("p")
    # U: na stránce jsou nějaké <p> ?

    list_food = ["kmín", "česnek", "voda", "sůl"]
    # U: správné ingredience měly být programátorky vyfiltrované ze všech prvků stránky, ne vytvořené staticky

    for p in food:
        list_food.append(p.text)

    with open("polevka.json", mode="w") as soubor:
        json.dump(list_food, soubor, indent=4, ensure_ascii=False)
    print(list_food)
    # U: do konzole měl být vypsán text z prvků, ne celý list


if __name__ == "__main__":
    main()
