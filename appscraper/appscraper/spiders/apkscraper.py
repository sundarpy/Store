import scrapy
from appscraper.items import AppItem
from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

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
		item['name'] = hxs.select('//h1[@itemprop="name"]/text()').extract()
		item['icon_url'] = hxs.select('//div[@class="appDown clearfix"]/img/@src').extract()
		item['description'] = hxs.select('//div[@id="hpn"]//text()').extract()
		item['publisher'] = hxs.select('//div[@class="appInfo clearfix"]/p[5]/i/a/text()').extract()
		item['category'] = hxs.select('//div[@class="site"]/a[2]/text()').extract()
		item['subcategory'] = hxs.select('//div[@class="site"]/a[3]/text()').extract()
		item['rating'] = hxs.select('//div[@class="proWrap clearfix"]/meta[2]/@*[2]').extract()
		item['ratingcount'] = hxs.select('//span[@itemprop="ratingCount"]/text()').extract()
		item['pubdate'] = hxs.select('//div[@class="appInfo clearfix"]/p[2]/i/text()').extract()
		item['version'] = hxs.select('//div[@class="appInfo clearfix"]/p[1]/i/text()').extract()
		item['size'] = hxs.select('//div[@class="downBoxLeft"]/a/i/text()').extract()
		item['appapk_url'] = hxs.select('//div[@class="downBoxLeft"]/a/@href').extract()
		item['appimage_url'] = hxs.select('//ul[@class="pa det-pic-list"]/li/a/img/@src').extract()
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
		item['name'] = hxs.select('//h1[@itemprop="name"]/text()').extract()
		item['icon_url'] = hxs.select('//div[@class="appDown clearfix"]/img/@src').extract()
		item['description'] = hxs.select('//div[@id="hpn"]//text()').extract()
		item['publisher'] = hxs.select('//div[@class="appInfo clearfix"]/p[5]/i/a/text()').extract()
		item['category'] = hxs.select('//div[@class="site"]/a[2]/text()').extract()
		item['subcategory'] = hxs.select('//div[@class="site"]/a[3]/text()').extract()
		item['rating'] = hxs.select('//div[@class="proWrap clearfix"]/meta[2]/@*[2]').extract()
		item['ratingcount'] = hxs.select('//span[@itemprop="ratingCount"]/text()').extract()
		item['pubdate'] = hxs.select('//div[@class="appInfo clearfix"]/p[2]/i/text()').extract()
		item['version'] = hxs.select('//div[@class="appInfo clearfix"]/p[1]/i/text()').extract()
		item['size'] = hxs.select('//div[@class="downBoxLeft"]/a/i/text()').extract()
		item['appapk_url'] = hxs.select('//div[@class="downBoxLeft"]/a/@href').extract()
		item['appimage_url'] = hxs.select('//ul[@class="pa det-pic-list"]/li/a/img/@src').extract()
		items.append(item)
		return items

"""=============Spider End============="""

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
		item['name'] = hxs.select('//div[@class="title-like"]/h1/text()').extract()
		item['icon_url'] = hxs.select('//div[@class="icon"]/img/@src').extract()
		item['description'] = hxs.select('//div[@itemprop="description"]/text()').extract()
		item['features'] = hxs.select('//div[@itemprop="description"]/p/text()').extract()
		item['publisher'] = hxs.select('//span[@itemprop="name"]/text()').extract()
		item['category'] = 'Games'
		item['subcategory'] = hxs.select('//div[@class="title bread-crumbs"]/a[2]/text()').extract()
		item['rating'] = hxs.select('//span[@class="rating"]/span[@class="average"]/text()').extract()
		item['pubdate'] = hxs.select('//p[@itemprop="datePublished"]/text()').extract()
		item['version'] = hxs.select('//p[@itemprop="softwareVersion"]/text()').extract()
		item['size'] = hxs.select('//span[@itemprop="fileSize"]/text()').extract()
		item['appapk_url'] = hxs.select('//div[@class="ny-down"]/a/@href').extract()
		# item['appapk_file'] = hxs.select('').extract()
		item['appimage_url'] = hxs.select('//ul[@class="pa det-pic-list"]/li/a/img/@src').extract()
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
		item['name'] = hxs.select('//div[@class="title-like"]/h1/text()').extract()
		item['icon_url'] = hxs.select('//div[@class="icon"]/img/@src').extract()
		item['description'] = hxs.select('//div[@itemprop="description"]/text()').extract()
		item['features'] = hxs.select('//div[@itemprop="description"]/p/text()').extract()
		item['publisher'] = hxs.select('//span[@itemprop="name"]/text()').extract()
		item['category'] = 'Apps'
		item['subcategory'] = hxs.select('//div[@class="title bread-crumbs"]/a[2]/text()').extract()
		item['rating'] = hxs.select('//span[@class="rating"]/span[@class="average"]/text()').extract()
		item['pubdate'] = hxs.select('//p[@itemprop="datePublished"]/text()').extract()
		item['version'] = hxs.select('//p[@itemprop="softwareVersion"]/text()').extract()
		item['size'] = hxs.select('//span[@itemprop="fileSize"]/text()').extract()
		item['appapk_url'] = hxs.select('//div[@class="ny-down"]/a/@href').extract()
		# item['appapk_file'] = hxs.select('').extract()
		item['appimage_url'] = hxs.select('//ul[@class="pa det-pic-list"]/li/a/img/@src').extract()
		items.append(item)
		return items

"""=============Spider End============="""

"""=============Spider Begin==========="""
class apkdlApps(scrapy.Spider):
	"""apk-dl Apps"""
	name = 'apkdlapps'
	next_page = 1
	allowed_domains = ["apk-dl.com"]
	start_urls = [
		"http://apk-dl.com/apps?page=1"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://apk-dl.com/apps?page={pagenum}'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="col-lg-3 col-sm-3"]/a/@href')
		for href in ulink:
			uRl = response.urljoin(href.extract())
			yield scrapy.Request(uRl, callback=self.parse_apps, meta={'url':href.extract()})
		self.next_page += 1
		yield self.create_ajax_request(self.next_page)

	def parse_apps(self, response):
		hxs = HtmlXPathSelector(response)
		items = []
		item = AppItem()
		item['name'] = hxs.select('//div[@class="info"]/div[2]/text()').extract()
		item['icon_url'] = hxs.select('//div[@class="col-md-4 text-center image"]/img/@src').extract()
		item['description'] = hxs.select('//span[@itemprop="description"]/div[@jsname="C4s9Ed"]/text()').extract()
		item['features'] = hxs.select('//span[@itemprop="description"]/div[@jsname="C4s9Ed"]/p/text()').extract()
		item['publisher'] = hxs.select('//div[@class="info"]/div[5]/text()').extract()
		item['category'] = 'Apps'
		item['subcategory'] = hxs.select('//div[@class="info"]/div[4]/text()').extract()
		item['rating'] = hxs.select('//div[@class="info"]/div[13]/span[@itemprop="ratingValue"]/text()').extract()
		item['pubdate'] = hxs.select('//div[@class="info"]/div[7]/text()').extract()
		item['version'] = hxs.select('//div[@class="info"]/div[6]/text()').extract()
		item['size'] = hxs.select('//div[@class="info"]/div[8]/text()').extract()
		item['appapk_url'] = hxs.select('//div[@class="col-md-4 text-center image"]/div[@class="text-center"]/a/@href').extract()
		# item['appapk_file'] = hxs.select('').extract()
		item['appimage_url'] = hxs.select('//div[@class="slick-track"]/div/@href').extract()
		items.append(item)
		return items

"""=============Spider End============="""

"""=============Spider Begin==========="""
class apkdlGames(scrapy.Spider):
	"""apk-dl Games"""
	name = 'apkdlgames'
	next_page = 1
	allowed_domains = ["apk-dl.com"]
	start_urls = [
		"http://apk-dl.com/games?page=1"
		]

	def create_ajax_request(self, page_number):
		ajax_template = 'http://apk-dl.com/games?page={pagenum}'
		url = ajax_template.format(pagenum=page_number)
		return Request(url, callback=self.parse)

	def parse(self, response):
		ulink = response.xpath('//div[@class="col-lg-3 col-sm-3"]/a/@href')
		for href in ulink:
			uRl = response.urljoin(href.extract())
			yield scrapy.Request(uRl, callback=self.parse_apps, meta={'url':href.extract()})
		self.next_page += 1
		yield self.create_ajax_request(self.next_page)

	def parse_apps(self, response):
		hxs = HtmlXPathSelector(response)
		items = []
		item = AppItem()
		item['name'] = hxs.select('//div[@class="info"]/div[2]/text()').extract()
		item['icon_url'] = hxs.select('//div[@class="col-md-4 text-center image"]/img/@src').extract()
		item['description'] = hxs.select('//span[@itemprop="description"]/div[@jsname="C4s9Ed"]/text()').extract()
		item['features'] = hxs.select('//span[@itemprop="description"]/div[@jsname="C4s9Ed"]/p/text()').extract()
		item['publisher'] = hxs.select('//div[@class="info"]/div[5]/text()').extract()
		item['category'] = 'Apps'
		item['subcategory'] = hxs.select('//div[@class="info"]/div[4]/text()').extract()
		item['rating'] = hxs.select('//div[@class="info"]/div[13]/span[@itemprop="ratingValue"]/text()').extract()
		item['pubdate'] = hxs.select('//div[@class="info"]/div[7]/text()').extract()
		item['version'] = hxs.select('//div[@class="info"]/div[6]/text()').extract()
		item['size'] = hxs.select('//div[@class="info"]/div[8]/text()').extract()
		item['appapk_url'] = hxs.select('//div[@class="col-md-4 text-center image"]/div[@class="text-center"]/a/@href').extract()
		# item['appapk_file'] = hxs.select('').extract()
		item['appimage_url'] = hxs.select('//div[@class="slick-track"]/div/@href').extract()
		items.append(item)
		return items

"""=============Spider End============="""



