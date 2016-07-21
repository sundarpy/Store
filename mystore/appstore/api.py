#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import json
from appstore.models import Application, ApplicationImage, Category, SubCategory, Publisher
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import urllib2
import unicodedata

"""==================================="""
"""====#API for Application Items#===="""
"""==================================="""

@api_view(['GET','POST'])
def read_file(request):

	urls = [
		'/Users/nishant/store/appscraper/apps.json',
		'/Users/nishant/store/appscraper/games.json',
	]
	
	for url in urls:
		f = open(url, 'r')						
		json_string = f.read()																																	
		data = json.loads(json_string)
		f.close()												
		for item in data:															
			for key in item:
				if key=='name':
					nam1 = str(item[key])
					nam2 = nam1.replace("u'","").replace("']","").replace(" APK","")
					app_name = nam2[1:]
				elif key=='icon_url':
					ico1 = str(item[key])
					ico2 = ico1.strip("]").replace("u'","").strip("'").strip('"').replace('u"','')
					app_icon = ico2[1:]
				elif key=='description':
					temp1 = item[key]
					xlist = []
					for i in temp1:
						temp2 = i.replace("\r","").replace("\n","")
						xlist.append(temp2)
					desc1 = str(xlist)
					desc2 = desc1.replace("u'","").replace("\u","").strip("]").replace('", ',"").replace("', ","").replace("', '","").replace('", "',"").replace("'","").replace('u"','').replace('"','').strip("[").replace("\xa0","")
					desc3 = desc2.lstrip().rstrip()
					app_description = desc3
				elif key=='publisher':
					pub1 = str(item[key])
					pub2 = pub1.replace("u'","").replace("']","")
					pub3 = pub2[6:]
					pub4 = pub3.lstrip()
					app_publisher = pub4[:-32]
				elif key=='category':
					cat1 = str(item[key])
					cat2 = cat1.replace("u'","").replace("']","")
					cat3 = cat2[6:]
					cat4 = cat3.lstrip()
					app_category = cat4[:-24]
				elif key=='subcategory':
					subcat1 = str(item[key])
					subcat2 = subcat1.replace("u'","").replace("']","")
					subcat3 = subcat2[6:]
					subcat4 = subcat3.lstrip()
					app_subcategory = subcat4[:-24]
				elif key=='minimum':
					mini1 = str(item[key])
					mini2 = mini1.replace("u'","").replace("']","")
					mini3 = mini2[1:]
					minimumandroid = mini3
				elif key=='pubdate':
					date1 = str(item[key])
					date2 = date1.replace("u'","").replace("']","")
					app_pubdate = date2[1:]
				elif key=='version':
					ver1 = str(item[key])
					ver2 = ver1.replace("u'","").replace("']","")
					app_version = ver2[1:]
				elif key=='ratingcount':
					ratcnt1 = str(item[key])
					ratcnt2 = ratcnt1.replace("u'","").replace("']","").replace(" votes","")
					rating_count = ratcnt2[1:]
				elif key=='rating':
					rate1 = str(item[key])
					rate2 = rate1.replace("u'","").replace("']","")
					rate3 = rate2[1:]
					app_rating = float(rate3)
				elif key=='size':
					size1 = str(item[key])
					size2 = size1[9:-10]
					app_size = float(size2)
				elif key=='appapk_url':
					filelist = []
					apk_urls = item[key]
					for i in apk_urls:
						temp = str(i)
						filelist.append(temp)
				elif key=='appimage_url':
					imagelist = []
					image_urls = item[key]
					for i in image_urls:
						temp = str(i)
						imagelist.append(temp)

			try:
				app_cat=Category.objects.get(category_name=app_category)
			except:
				app_cat=Category(category_name=app_category)
				app_cat.save()

			try:
				app_subcat=SubCategory.objects.get(subcategory_name=app_subcategory, category=app_cat)
			except:
				app_subcat=SubCategory(subcategory_name=app_subcategory, category=app_cat)
				app_subcat.save()

			try:
				app_publish=Publisher.objects.get(name=app_publisher)
			except:
				app_publish=Publisher(name=app_publisher)
				app_publish.save()

			try:
				app_obj=Application.objects.get(app_name=product_title)
			except:
				app_obj=Application(
					app_name=app_name,
					app_icon_url=app_icon,
					app_description=app_description,
					app_category=app_cat,
					app_subcategory=app_subcat,
					app_publisher=app_publish,
					app_ratingcount=rating_count,
					app_minimum=minimumandroid,
					app_rating=app_rating,
					app_pubdate=app_pubdate,
					app_version=app_version,
					app_size=app_size,
					app_url=filelist[0],
					)
				app_obj.save()

			for i in imagelist:
				app_im=ApplicationImage(
					image_url=i,
					app_name=app_obj,
					)
				app_im.save()

	return Response({'message':'Applications saved succesfully', 'status':200})

