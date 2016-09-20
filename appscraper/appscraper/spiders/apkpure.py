#!/usr/bin/python
# -*- coding: utf-8 -*-
import scrapy
from appscraper.items import AppItem
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import unicodedata

"""========Application Spiders========="""

# """=============Spider Begin==========="""
# class GoogleApps(scrapy.Spider):
# 	"""Google Play Apps"""
# 	name = 'googleapps'
# 	next_page = 1
# 	allowed_domains = ["play.google.com"]
# 	start_urls = [
# 		"https://play.google.com/store/apps?authuser=0"
# 		]

# 	def create_ajax_request(self, page_number):
# 		ajax_template = 'https://play.google.com/store/apps?authuser={pagenum}'
# 		url = ajax_template.format(pagenum=page_number)
# 		return Request(url, callback=self.parse)

# 	def parse(self, response):
# 		ulink = response.xpath('//div[@class="details"]/a[2]/@href')
# 		for href in ulink:
# 			uRl = response.urljoin(href.extract())
# 			yield scrapy.Request(uRl, callback=self.parse_apps)
# 		self.next_page += 1
# 		yield self.create_ajax_request(self.next_page)

# 	def parse_apps(self, response):
# 		hxs = HtmlXPathSelector(response)
# 		items = []
# 		item = AppItem()
# 		item['name'] = hxs.select('//div[@class="id-app-title"]/text()').extract()
# 		item['icon_url'] = hxs.select('//div[@class="cover-container"]/img/@src').extract()
# 		item['description'] = hxs.select('//div[@jsname="C4s9Ed"]/text()').extract()
# 		item['features'] = hxs.select('//div[@jsname="C4s9Ed"]/p/text()').extract()
# 		item['publisher'] = hxs.select('//a[@class="document-subtitle primary"]/span/text()').extract()
# 		item['category'] = hxs.select('//a[@class="document-subtitle category"]/span/text()').extract()
# 		item['rating'] = hxs.select('//div[@class="score-container"]/div[1]/text()').extract()
# 		item['pubdate'] = hxs.select('//div[@class="meta-info"]/div[@itemprop="datePublished"]/text()').extract()
# 		item['version'] = hxs.select('//div[@class="meta-info"]/div[@itemprop="softwareVersion"]/text()').extract()
# 		item['size'] = hxs.select('//div[@class="meta-info"]/div[@itemprop="fileSize"]/text()').extract()
# 		# item['appapk_url'] = hxs.select('//div[@class="ny-down"]/a/@href').extract()
# 		# item['appapk_file'] = hxs.select('').extract()
# 		item['appimage_url'] = hxs.select('//div[@class="thumbnails"]/img/@src').extract()
# 		items.append(item)
# 		return items

# """=============Spider End============="""

"""=============Spider Begin==========="""
class ApkPureGames(scrapy.Spider):
	"""ApkPure Games"""
	name = 'apkpuregames'
	next_page = 1
	allowed_domains = ["apkpure.com"]
	start_urls = [
		"https://apkpure.com/game?page=1"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'https://apkpure.com/game?page={pagenum}'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="category-template-title"]/a/@href')
		for href in ulink:
			uRl = response.urljoin(href.extract())
			yield scrapy.Request(uRl, callback=self.parse_apps, meta={'url':href.extract()})
		self.next_page += 1
		yield self.create_ajax_request(self.next_page)

	def parse_apps(self, response):
		hxs = HtmlXPathSelector(response)
		items = []
		item = AppItem()
		name = hxs.select('//div[@class="title-like"]/h1/text()').extract()
		item['icon_url'] = hxs.select('//div[@class="icon"]/img/@src').extract()
		description = hxs.select('//div[@itemprop="description"]//node()').extract()
		publisher = hxs.select('//span[@itemprop="name"]/text()').extract()
		item['category'] = 'Games'
		item['subcategory'] = hxs.select('//div[@class="title bread-crumbs"]/a[2]/text()').extract()
		item['rating'] = hxs.select('//span[@class="rating"]/span[@class="average"]/text()').extract()
		item['pubdate'] = hxs.select('//p[@itemprop="datePublished"]/text()').extract()
		item['version'] = hxs.select('//p[@itemprop="softwareVersion"]/text()').extract()
		item['size'] = hxs.select('//span[@itemprop="fileSize"]/text()').extract()
		item['appapk_url'] = hxs.select('//div[@class="ny-down"]/a/@href').extract()
		# item['appapk_file'] = hxs.select('').extract()
		item['appimage_url'] = hxs.select('//ul[@class="pa det-pic-list"]/li/a/img/@src').extract()
		item['minimum'] = hxs.select('//p[@itemprop="operatingSystem"]/text()').extract()
		item['ratingcount'] = hxs.select('//span[@itemprop="ratingCount"]/text()').extract()

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
class ApkPureApps(scrapy.Spider):
	"""ApkPure Apps"""
	name = 'apkpureapps'
	next_page = 1
	allowed_domains = ["apkpure.com"]
	start_urls = [
		"https://apkpure.com/app?page=1"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'https://apkpure.com/app?page={pagenum}'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="category-template-title"]/a/@href')
		for href in ulink:
			uRl = response.urljoin(href.extract())
			yield scrapy.Request(uRl, callback=self.parse_apps, meta={'url':href.extract()})
		self.next_page += 1
		yield self.create_ajax_request(self.next_page)

	def parse_apps(self, response):
		hxs = HtmlXPathSelector(response)
		items = []
		item = AppItem()
		name = hxs.select('//div[@class="title-like"]/h1/text()').extract()
		item['icon_url'] = hxs.select('//div[@class="icon"]/img/@src').extract()
		description = hxs.select('//div[@itemprop="description"]//node()').extract()
		publisher = hxs.select('//span[@itemprop="name"]/text()').extract()
		item['category'] = 'Apps'
		item['subcategory'] = hxs.select('//div[@class="title bread-crumbs"]/a[2]/text()').extract()
		item['rating'] = hxs.select('//span[@class="rating"]/span[@class="average"]/text()').extract()
		item['pubdate'] = hxs.select('//p[@itemprop="datePublished"]/text()').extract()
		item['version'] = hxs.select('//p[@itemprop="softwareVersion"]/text()').extract()
		item['size'] = hxs.select('//span[@itemprop="fileSize"]/text()').extract()
		item['appapk_url'] = hxs.select('//div[@class="ny-down"]/a/@href').extract()
		# item['appapk_file'] = hxs.select('').extract()
		item['appimage_url'] = hxs.select('//ul[@class="pa det-pic-list"]/li/a/img/@src').extract()
		item['minimum'] = hxs.select('//p[@itemprop="operatingSystem"]/text()').extract()
		item['ratingcount'] = hxs.select('//span[@itemprop="ratingCount"]/text()').extract()

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
class ApkMirrorApps(scrapy.Spider):
	"""ApkMirror Apps"""
	name = 'apkmirrorapps'
	next_page = 1
	allowed_domains = ["apkmirror.com"]
	start_urls = [
		"https://apkmirror.com/page/1/"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'https://apkmirror.com/page/{pagenum}/'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//a[@class="fontBlack"]/@href')
		for href in ulink:
			uRl = response.urljoin(href.extract())
			yield scrapy.Request(uRl, callback=self.parse_apps, meta={'url':href.extract()})
		self.next_page += 1
		yield self.create_ajax_request(self.next_page)

	def parse_apps(self, response):
		hxs = HtmlXPathSelector(response)
		items = []
		item = AppItem()
		item['name'] = hxs.select('//div[@class="table-cell"]/h1/text()').extract()
		item['icon_url'] = hxs.select('//div[@class="table-cell"]/img/@src').extract()
		item['publisher'] = hxs.select('//div[@class="table-cell"]/h3/a/text()').extract()
		items.append(item)
		return items

"""=============Spider End============="""


