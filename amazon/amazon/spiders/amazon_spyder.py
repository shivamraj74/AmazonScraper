import scrapy
from ..items import AmazonItem
class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        "https://www.amazon.in/s?bbn=1389401031&rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cp_89%3ARedmi&dc&fst=as%3Aoff&qid=1588921161&rnid=3837712031&ref=lp_1389401031_nr_p_89_0"
    ]
    def parse(self, response):
        items = AmazonItem()
        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_price = response.css('.a-price-whole::text').extract()

        items['product_name'] = product_name
        items['product_price'] = product_price

        yield items

