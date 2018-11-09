import scrapy

class GucciSpider(scrapy.Spider):
    name = "guccispider"
    start_urls=['https://www.gucci.com/uk/en_gb/ca/women/womens-ready-to-wear/coats-c-women-readytowear-coats-furs']



    def parse(self,response):
         for price in response.css('div.product-tiles-grid-item-info'):
             yield{'price':price.css('span.sale::text').extract_first(),
                   'caption':response.css('h2::text').extract_first(),}
         for image  in response.css('div.product-tiles-grid-item-image >img'):
              yield{'image':image.css('img::attr(src)').extract_first(),}
         for dataproduct in response.css('div.product-tiles-grid >article'):
              yield{'dataproduct':dataproduct.css('a::attr(data-style-id)').extract_first(),
                      'herf':dataproduct.css('a::attr(href)').extract_first(),}
