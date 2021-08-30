from scrapy import Spider, cmdline
import scrapy


class PaperSpider(scrapy.Spider):
    name = 'paper'

    def start_requests(self):
        url = 'https://api2.bmob.cn/1/classes/ComputerImage?limit=100&order=-updatedAt&' \
              'where={"ranking":{"$gt":3},"reportCount":{"$lt":1}}'
        heard = {
            "X-Bmob-Application-Id": "633edd745d4d8630d88c73a16440cb9a",
            "X-Bmob-REST-API-Key": "a4641142e83b0bd08c8fe67791cf9018",
            "Content-Type": "application/json; charset=UTF-8",
            "Host": "api2.bmob.cn"
        }

        yield scrapy.Request(url, method='get', headers=heard)

    def parse(self, response):
        print(response.text)

if __name__ == '__main__':
    cmdline.execute("scrapy crawl paper".split())

