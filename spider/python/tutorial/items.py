# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    company_name = scrapy.Field()  #
    address = scrapy.Field()  #
    position_id = scrapy.Field()  #
    position_name = scrapy.Field()  #
    salary = scrapy.Field()  #
    describe = scrapy.Field() #?
    work_year = scrapy.Field()  #
    educational = scrapy.Field()  #
    create_time = scrapy.Field() #
    pass
