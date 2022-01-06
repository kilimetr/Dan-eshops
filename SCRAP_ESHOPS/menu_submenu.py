# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr



import bs4
import requests 
import csv



headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
		   AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

source_nabidky = requests.get("https://www.limango.de/shop", headers = headers)

if source_nabidky.status_code != 200:
	print("něco je zle - source")
else:
	print("access granted")


response = bs4.BeautifulSoup(source_nabidky.text,"lxml")
menu     = response.find("div", class_ = "shop71")
menu     = menu.find_all("div", class_ = "shop190")


for item in menu:
	subhref = item.find("a", class_ = "shop192")["href"]
	subtext = item.find("span").text
	# print(item.prettify())
	print()
	print(subhref)
	print(subtext)
	print()
	print()
	print()

	# i = 1
	# NextPage = True

	# while NextPage == True:

		# if i != 1:
			# source_nabidky = requests.get("https://www.kupi.cz" + next_page, 
							 # headers = headers)
			# soup_nabidky   = BeautifulSoup.BeautifulSoup(source_nabidky.text,"lxml")
			# polozky        = soup_nabidky.find_all("div", class_ = "area_content")
		
			# if source_nabidky.status_code != 200:
				# print("něco je zle - source")
			# else:
				# print("access granted")

		# else:
			# pass

		# j = 1
		# for polozka in polozky:
			# print(polozka.prettify())
			# print(polozka["aria-label"])
			# nazev = polozka.find("span", class_ = "name").text
			# cena  = polozka.find("span", class_ = "price").text
			# obrazek_odkaz = polozka.find("a", class_ = "full_map_link log_map_click")["href"]


			# source_obrazek = requests.get("https://www.kupi.cz" + obrazek_odkaz,
							 # headers = headers)

			# if source_obrazek.status_code != 200:
				# print("něco je zle_source obrazek")
			# else:
				# print("access granted")

			# soup_obrazek           = BeautifulSoup.BeautifulSoup(source_obrazek.text, "lxml")
			# obrazek_zuzeni_hledani = soup_obrazek.find("div", class_ = "product_image")
			# obrazek                = obrazek_zuzeni_hledani.find("img")["src"]

			# nazev = letter_conv_fun(nazev)

			# csv_writer_polozky.writerow([nazev, cena, obrazek])

			# print(nazev)
			# print(cena)
			# print(obrazek_odkaz)
			# print(obrazek)
			# print()
			

		# try:
			# next_page_div = soup_nabidky.find("div", class_ = "leaflet_next_pages text-center")
			# next_page     = next_page_div.find("a")["href"]
			# print()
			# print(next_page)
			# print()

		# except Exception as e:
			# next_page = "no next page is there"


		# if next_page != "no next page is there":
			# NextPage = True

		# else:
			# NextPage = False

		# print(NextPage)

		# i = i + 1


	# csv_file_polozky.close()

print("ALBERT SCRAP BYL SPUŠTĚN")
	

