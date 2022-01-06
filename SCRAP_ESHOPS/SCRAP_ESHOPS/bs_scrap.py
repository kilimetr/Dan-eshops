# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr



import bs4 as BeautifulSoup
import requests 



headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

source_nabidky = requests.get("https://www.limango.de/shop/gap/sweatjacke-in-blau-dunkelblau-2-7667368", headers = headers)

if source_nabidky.status_code != 200:
    print("něco je zle - source")
else:
    print("access granted")


soup_nabidky = BeautifulSoup.BeautifulSoup(source_nabidky.text,"lxml")
polozky      = soup_nabidky.find_all("div", {"id": "product_details"})


for item in polozky:
    print()
    print()
    print(item.prettify())
    print()
    print()
    print()


print("SCRAPPER BYL SPUŠTĚN")


