# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr



import bs4 as BeautifulSoup
import requests 


def BORN2BEPL_scrap_fun():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    source_nabidky = requests.get("https://born2be.pl/buty-damskie", headers = headers)

    if source_nabidky.status_code != 200:
        print("něco je zle - source")
    else:
        print("access granted")


    soup_nabidky = BeautifulSoup.BeautifulSoup(source_nabidky.text,"lxml")
    nabidka      = soup_nabidky.find("div", class_ = "list__products")
    polozky      = nabidka.find_all("div", class_ = "product")

    for polozka in polozky:
        nazev = polozka.find("div", class_ = "product__name").text
        cena  = polozka.find("div", class_ = "product")

        print(nazev)
        print(polozka["data-gtm-price"])
        print()


    print("BORN2BE.PL SCRAP BYL SPUŠTĚN")


BORN2BEPL_scrap_fun()


