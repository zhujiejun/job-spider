import random
import time

import scrapy
from rediscluster import RedisCluster
from scrapy.conf import settings
from scrapy.http import Request
from scrapy.selector import Selector
from tutorial.items import TutorialItem


# zhipin 爬虫
class ZhipinSpider(scrapy.Spider):
    name = "boss"
    allowed_domains = ["www.zhipin.com"]
    current_page = 1  # 开始页码
    start_urls = [
        "https://www.zhipin.com/job_detail/?city=" + settings.get("BOSS_CITY_CODE") + "&source=10" + "&query=" + settings.get("LANGUAGE")]
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            'tutorial.middlewares.ZhipinMiddleware': 299,
        },
        "ITEM_PIPELINES": {
            'tutorial.pipelines.ZhipinPipeline': 300,
        },
        "DEFAULT_REQUEST_HEADERS": {
            'sec-fetch-user': '?1',
            'sec-fetch-site': 'none',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': ' navigate',
            'upgrade-insecure-requests': 1,
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'user-agent': ' Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/87.0.4280.88',
            'cookie': 'lastCity=101280600; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1609996748; t=XGDMvtVUuhnQkVTh; wt2=RPURQQrqGhnQkVTh; _bl_uid=5zkz5je1mjIe8bia44ay428ahekg; __l=l=%2Fwww.zhipin.com%2Fjob_detail%2F%3Fcity%3D101280600%26query%3DJava&r=&g=&s=3&friend_source=0&s=3&friend_source=0; __c=1609996748; __a=60541390.1609996748..1609996748.10.1.10.10; __zp_stoken__=7d39bC3xeB1VGOW1kEB08CEAjM1VvdBEYWipnOBV2ZWd3axNLd3Q7BHp0a193Um4SD2QSZhggZBdNJmECGy4Hbn0EIDMEUWQadQlUbUtrSRovPBQrBBlfFCkdGwshL0J7CTUYdVxfYGxPBTZhHQ%3D%3D; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1609998619'
        }
    }

    def parse(self, response):
        # js = json.loads(response.body)
        # html = js['html']
        html = response.body
        selector = Selector(text=html)
        items = selector.css('.item')
        host = 'https://www.zhipin.com'
        # 初始化redis cluster
        rc = RedisCluster(startup_nodes=settings.get('STARTUP_NODES'), decode_responses=True)
        setkey = settings.get('REDIS_POSITION_KEY')
        sleep_seconds = int(settings.get('SLEEP_SECONDS'))
        for item in items:
            url = host + item.css('a::attr(href)').extract_first()
            position_name = item.css('h4::text').extract_first()  # 职位名称
            salary = item.css('.salary::text').extract_first() or ''  # 薪资
            work_year = item.css('.msg em:nth-child(2)::text').extract_first() or '不限'  # 工作年限
            educational = item.css('.msg em:nth-child(3)::text').extract_first()  # 教育程度
            meta = {
                "salary": salary,
                "work_year": work_year,
                "educational": educational,
                "position_name": position_name,
            }
            sleep_seconds = int(settings.get('SLEEP_SECONDS'))
            time.sleep(int(random.uniform(sleep_seconds, sleep_seconds + 20)))

            position_id = url.split("/")[-1].split('.')[0]
            print(position_id)
            if (rc.sadd(setkey, position_id)) == 1:
                yield Request(url, callback=self.parse_item, meta=meta)
        max_page = settings.get('MAX_PAGE')
        if self.current_page < max_page:
            self.current_page += 1
            api_url = "https://www.zhipin.com/job_detail/?city=" + settings.get("BOSS_CITY_CODE") + "&source=10" + "&query=" + settings.get("LANGUAGE") + "&page=" + str(self.current_page)
            time.sleep(int(random.uniform(sleep_seconds, sleep_seconds + 20)))
            yield Request(api_url, callback=self.parse)
        pass

    def parse_item(self, response):
        item = TutorialItem()
        selector = response.css
        item['address'] = selector('.location-address::text').extract_first()
        item['create_time'] = selector('.job-tags .time::text').extract_first()
        item['body'] = selector('.text').xpath('string(.)').extract_first()
        item['company_name'] = selector('.business-info h4::text').extract_first()
        item['postion_id'] = response.url.split("/")[-1].split('.')[0]
        item = dict(item, **response.meta)
        yield item
