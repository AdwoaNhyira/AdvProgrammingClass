# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
from itemadapter import ItemAdapter


class ScrapyprojectPipeline:
    def __init__(self):
        self.csv_file = open('output.csv', 'w', newline='')
        self.csv_writer = csv.DictWriter(self.csv_file, fieldnames=['company', 'symbol', 'ytd_rtn'])
        self.csv_writer.writeheader()

    def process_item(self, item, spider):
        self.csv_writer.writerow(item)
        return item

    def close_spider(self, spider):
        self.csv_file.close()
