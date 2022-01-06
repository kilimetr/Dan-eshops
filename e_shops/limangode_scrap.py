# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr



import bs4 as BeautifulSoup
import requests 


def LIMANGODE_scrap_fun():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    source_nabidky = requests.get("https://www.limango.de/shop/baby", headers = headers)

    if source_nabidky.status_code != 200:
        print("něco je zle - source")
    else:
        print("access granted")


    soup_nabidky = BeautifulSoup.BeautifulSoup(source_nabidky.text,"lxml")
    nabidka      = soup_nabidky.find("div", class_ = "shop978")
    polozky      = nabidka.find_all("div", class_ = "shop87 shop73 shop82 shop89 shop133 shop172")

    # print(nabidka.prettify())

    for polozka in polozky:
        nazev = polozka.find("div", class_ = "shop1288").text
        cena  = polozka.find("span", class_ = "shop1297").text

        print(nazev)
        print(cena)
        print()

# vyhodí chybu kvůli reklamě, která nemá příslušné componenty

    print("LIMANGO.DE SCRAP BYL SPUŠTĚN")


LIMANGODE_scrap_fun()


