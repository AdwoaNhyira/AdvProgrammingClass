import scrapy
from ScrapyProject.items import ScrapyprojectItem

class MySpider(scrapy.Spider):
    name = "my_spider"
    url = [
        'https://www.slickcharts.com/sp500/performance',
    ]

    def parse(self, response):
        rows = response.xpath('//div[@class="table-responsive"]//tbody/tr')
        for row in rows:
            item = ScrapyprojectItem()
            item['num'] = row.xpath('.//td[1]/a/text()').get()
            item['company'] = row.xpath('.//td[2]/a/text()').get()
            item['symbol'] = row.xpath('.//td[3]/a/text()').get()
            item['ytd_rtn'] = row.xpath('.//td[4]/text()').get().strip()


            yield item
