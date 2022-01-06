# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr



import scrapy
import json
from math               import floor
from scrapy.loader      import ItemLoader
from SCRAP_ESHOPS.items import Limango_Products_Items



class TestingSpider(scrapy.Spider):
    name = "testing"

    allowed_domains = ["https://www.limango.de"]
    start_urls      = ["https://www.limango.de/search/api/search/listing?limit=200&search=&offset=0&sort=popularity&size=&color=&brand=&\
                        category=&campaign=&gender=&style=&product=&merchantId=&price=&discount=&availability=&in=&tag=&shop-type=&\
                        referer=/shop/baby?&landing-page-id=baby&testGroup=20210706_ProductGateway"]


    def parse(self, response):
        data = json.loads(response.body)

        products = data["data"]["products"]["data"]

        for product in products:
            yield {
                "product_discount_fr": product["discount"],
                "brand_name": product["brand"]["name"]
            }
