# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr



import bs4 as BeautifulSoup
import requests 


def PEEK_CLOPPENBURGDE_scrap_fun():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    source_nabidky = requests.get("https://www.peek-cloppenburg.de/herren-bekleidung/", headers = headers)

    if source_nabidky.status_code != 200:
        print("něco je zle - source")
    else:
        print("access granted")


    soup_nabidky = BeautifulSoup.BeautifulSoup(source_nabidky.text,"lxml")
    nabidka      = soup_nabidky.find("ol", class_ = "productList")
    polozky      = nabidka.find_all("li", class_ = "productList-item")


    for polozka in polozky:
        info = polozka.find("a", class_ = "productTile-description")

        brand = info.find("p", class_ = "productTile-brand").text
        nazev = info.find("p", class_ = "productTile-title").text[1:]
        cena  = info.find("span", class_ = "qa-product-tile-price")["content"]

        print(brand)
        print(nazev)
        print(cena)
        print()

# vyhodí chybu kvůli reklamě, která nemá příslušné componenty

    print("PEEK-CLOPPENBURG.DE SCRAP BYL SPUŠTĚN")


PEEK_CLOPPENBURGDE_scrap_fun()


