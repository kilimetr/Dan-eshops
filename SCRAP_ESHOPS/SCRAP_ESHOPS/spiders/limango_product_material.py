# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr



import scrapy



class LimangoProductMaterialSpider(scrapy.Spider):
    name = "Limango_product_material"

    allowed_domains = ["https://www.limango.de/shop"]
    start_urls      = ["https://www.limango.de/shop/gap/sweatjacke-in-blau-dunkelblau-2-7667368"]


    def parse(self, response):
        product_details = response.css("[id = 'product_details']")
        priblizeni      = product_details.css(".shop87")

        for item in priblizeni:
            material = item.css(".shop453 span::text").getall()

        yield{
            "material": material
        }

