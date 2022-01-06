# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr



# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapEshopsPipeline:
    def process_item(self, item, spider):
        return item
