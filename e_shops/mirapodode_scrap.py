# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr



import bs4 as BeautifulSoup
import requests 


def MIRAPODODE_scrap_fun():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    source_nabidky = requests.get("https://www.mirapodo.de/damen/schuhe/", headers = headers)

    if source_nabidky.status_code != 200:
        print("něco je zle - source")
    else:
        print("access granted")


    soup_nabidky = BeautifulSoup.BeautifulSoup(source_nabidky.text,"lxml")
    nabidka      = soup_nabidky.find("ul", class_ = "prod-grid")
    polozky      = nabidka.find_all("li", class_ = "prod-grid__item")


    for polozka in polozky:
        brand = polozka.find("span", class_ = "prod-tile__brand").text
        nazev = polozka.find("span", class_ = "prod-tile__name").text
        cena  = polozka.find("span", class_ = "prod-tile__price-reduced").text

        print(brand)
        print(nazev)
        print(cena)
        print()

# vyhodí chybu kvůli reklamě, která nemá příslušné componenty

    print("MIRAPODO.DE SCRAP BYL SPUŠTĚN")


MIRAPODODE_scrap_fun()


