# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field

class AppItem(scrapy.Item):
	name = scrapy.Field()
	icon_url = scrapy.Field()
	icon_file = scrapy.Field()
	description = scrapy.Field()
	publisher = scrapy.Field()
	category = scrapy.Field()
	subcategory = scrapy.Field()
	rating = scrapy.Field()
	ratingcount = scrapy.Field()
	pubdate = scrapy.Field()
	version = scrapy.Field()
	size = scrapy.Field()
	appapk_url = scrapy.Field()
	appapk_file = scrapy.Field()
	appimage_url = scrapy.Field()
	appimage_files = scrapy.Field()
