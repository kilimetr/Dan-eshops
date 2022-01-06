# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr



import scrapy
from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Compose, SelectJmes



class Limango_Products_Items(Item):
    product_brand          = Field()
    product_name           = Field()
    product_id             = Field()
    product_discount       = Field()
    product_price_full     = Field()
    product_price_sale     = Field()
    product_price_currency = Field()
    product_labels   	   = Field()
    product_label_type     = Field()
    product_label_value    = Field()
    product_image_link     = Field()
    product_variants       = Field()


