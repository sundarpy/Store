#!/usr/bin/python
# -*- coding: utf-8 -*-
import scrapy
from appscraper.items import AppItem
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import unicodedata

"""========Application Spiders========="""
"""=============Spider Begin==========="""
class koplayerApps(scrapy.Spider):
	"""koplayer Apps"""
	name = 'koplayerapps'
	next_page = 1
	allowed_domains = ["koplayer.com"]
	start_urls = [
		"http://apk.koplayer.com/app/?page=1"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://apk.koplayer.com/app/?page={pagenum}'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//li[@class="clerafix"]/a/@href')
		for href in ulink:
			uRl = response.urljoin(href.extract())
			yield scrapy.Request(uRl, callback=self.parse_apps, meta={'url':href.extract()})
		self.next_page += 1
		yield self.create_ajax_request(self.next_page)

	def parse_apps(self, response):
		hxs = HtmlXPathSelector(response)
		items = []
		item = AppItem()
		name = hxs.select('//h1[@itemprop="name"]/text()').extract()
		item['icon_url'] = hxs.select('//div[@class="appDown clearfix"]/img/@src').extract()
		description = hxs.select('//div[@id="hpn"]//node()').extract()
		publisher = hxs.select('//div[@class="appInfo clearfix"]/p[5]/i/a/text()').extract()
		item['category'] = hxs.select('//div[@class="site"]/a[2]/text()').extract()
		item['subcategory'] = hxs.select('//div[@class="site"]/a[3]/text()').extract()
		item['rating'] = hxs.select('//div[@class="proWrap clearfix"]/meta[2]/@*[2]').extract()
		item['ratingcount'] = hxs.select('//span[@itemprop="ratingCount"]/text()').extract()
		item['pubdate'] = hxs.select('//div[@class="appInfo clearfix"]/p[2]/i/text()').extract()
		item['version'] = hxs.select('//div[@class="appInfo clearfix"]/p[1]/i/text()').extract()
		item['minimum'] = hxs.select('//div[@class="appInfo clearfix"]/p[4]/i/text()').extract()
		item['size'] = hxs.select('//div[@class="downBoxLeft"]/a/i/text()').extract()
		item['appapk_url'] = hxs.select('//div[@class="downBoxLeft"]/a/@href').extract()
		item['appimage_url'] = hxs.select('//ul[@class="pa det-pic-list"]/li/a/img/@src').extract()

		xlistname=[]
		for i in name:
			x0 = unicodedata.normalize('NFKD', i).encode('ascii', 'ignore')
			xlistname.append(x0)

		xlistdesc=[]
		for i in description:
			x1 = unicodedata.normalize('NFKD', i).encode('ascii', 'ignore')
			xlistdesc.append(x1)

		xlistpub=[]
		for i in publisher:
			x2 = unicodedata.normalize('NFKD', i).encode('ascii', 'ignore')
			xlistpub.append(x2)

		item['name'] = xlistname
		item['description'] = xlistdesc
		item['publisher'] = xlistpub
		
		items.append(item)
		return items

"""=============Spider End============="""

"""=============Spider Begin==========="""
class koplayerGames(scrapy.Spider):
	"""koplayer Games"""
	name = 'koplayergames'
	next_page = 1
	allowed_domains = ["koplayer.com"]
	start_urls = [
		"http://apk.koplayer.com/game/?page=1"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://apk.koplayer.com/game/?page={pagenum}'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//li[@class="clerafix"]/a/@href')
		for href in ulink:
			uRl = response.urljoin(href.extract())
			yield scrapy.Request(uRl, callback=self.parse_apps, meta={'url':href.extract()})
		self.next_page += 1
		yield self.create_ajax_request(self.next_page)

	def parse_apps(self, response):
		hxs = HtmlXPathSelector(response)
		items = []
		item = AppItem()
		name = hxs.select('//h1[@itemprop="name"]/text()').extract()
		item['icon_url'] = hxs.select('//div[@class="appDown clearfix"]/img/@src').extract()
		description = hxs.select('//div[@id="hpn"]//node()').extract()
		publisher = hxs.select('//div[@class="appInfo clearfix"]/p[5]/i/a/text()').extract()
		item['category'] = hxs.select('//div[@class="site"]/a[2]/text()').extract()
		item['subcategory'] = hxs.select('//div[@class="site"]/a[3]/text()').extract()
		item['rating'] = hxs.select('//div[@class="proWrap clearfix"]/meta[2]/@*[2]').extract()
		item['ratingcount'] = hxs.select('//span[@itemprop="ratingCount"]/text()').extract()
		item['pubdate'] = hxs.select('//div[@class="appInfo clearfix"]/p[2]/i/text()').extract()
		item['version'] = hxs.select('//div[@class="appInfo clearfix"]/p[1]/i/text()').extract()
		item['minimum'] = hxs.select('//div[@class="appInfo clearfix"]/p[4]/i/text()').extract()
		item['size'] = hxs.select('//div[@class="downBoxLeft"]/a/i/text()').extract()
		item['appapk_url'] = hxs.select('//div[@class="downBoxLeft"]/a/@href').extract()
		item['appimage_url'] = hxs.select('//ul[@class="pa det-pic-list"]/li/a/img/@src').extract()

		xlistname=[]
		for i in name:
			x0 = unicodedata.normalize('NFKD', i).encode('ascii', 'ignore')
			xlistname.append(x0)

		xlistdesc=[]
		for i in description:
			x1 = unicodedata.normalize('NFKD', i).encode('ascii', 'ignore')
			xlistdesc.append(x1)

		xlistpub=[]
		for i in publisher:
			x2 = unicodedata.normalize('NFKD', i).encode('ascii', 'ignore')
			xlistpub.append(x2)

		item['name'] = xlistname
		item['description'] = xlistdesc
		item['publisher'] = xlistpub
		
		items.append(item)
		return items

"""=============Spider End============="""



