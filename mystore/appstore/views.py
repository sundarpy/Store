from django.shortcuts import render
from appstore.models import Publisher, Category, SubCategory, Application, ApplicationImage, Featured, TopFree, TopNewFree, Trending, Collection, SerfoApp
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.views.decorators.csrf import csrf_protect
import json
from django.shortcuts import render, HttpResponse, Http404, render_to_response, get_object_or_404
from django.template.loader import get_template
from django.template import Context, RequestContext, loader
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
"""==============================="""
"""=========SEARCH METHOD========="""
"""==============================="""

def search(request):
	"""Search."""
	subcat = SubCategory.objects.all()
	try:
		q = request.GET.get('q')
	except:
		q = None

	if q:
		applications = Application.objects.filter(app_name__icontains=q)
		context = {"query": q, "applications": applications, "user" : request.user, "subcats":subcat,}
		template = 'results.html'
	else:
		template = 'home.html'
		context = {"user" : request.user, "subcats":subcat,}
	return render(request, template, context)


"""==============================="""
"""===========HOME PAGE==========="""
"""==============================="""

def HomePage(request):
	"""HomePage Method"""
	category = Category.objects.first()
	subcats = SubCategory.objects.filter(category=category)
	sub_category = SubCategory.objects.all()
	applications = Application.objects.filter(app_subcategory=sub_category)
	featured = Featured.objects.filter(featured_type='1')

	rowappz1 = Collection.objects.filter(rowno='1')
	rowappz2 = Collection.objects.filter(rowno='2')
	rowappz3 = Collection.objects.filter(rowno='3')
	rowappz4 = Collection.objects.filter(rowno='4')
	rowappz5 = Collection.objects.filter(rowno='5')
	rowappz6 = Collection.objects.filter(rowno='6')
	rowappz7 = Collection.objects.filter(rowno='7')
	rowappz8 = Collection.objects.filter(rowno='8')
	rowappz9 = Collection.objects.filter(rowno='9')
	rowappz10 = Collection.objects.filter(rowno='10')

	rowappz11 = Collection.objects.filter(rowno='11')
	rowappz12 = Collection.objects.filter(rowno='12')
	rowappz13 = Collection.objects.filter(rowno='13')
	rowappz14 = Collection.objects.filter(rowno='14')
	rowappz15 = Collection.objects.filter(rowno='15')
	rowappz16 = Collection.objects.filter(rowno='16')
	rowappz17 = Collection.objects.filter(rowno='17')
	rowappz18 = Collection.objects.filter(rowno='18')
	rowappz19 = Collection.objects.filter(rowno='19')
	rowappz20 = Collection.objects.filter(rowno='20')

	template = "home.html"
	context = {"applications":applications, "subcategory":sub_category, "subcats":subcats, "featured":featured, "rowappz1":rowappz1, "rowappz2":rowappz2, "rowappz3":rowappz3, "rowappz4":rowappz4, "rowappz5":rowappz5, "rowappz6":rowappz6, "rowappz7":rowappz7, "rowappz8":rowappz8, "rowappz9":rowappz9, "rowappz10":rowappz10, "rowappz11":rowappz11, "rowappz12":rowappz12, "rowappz13":rowappz13, "rowappz14":rowappz14, "rowappz15":rowappz15, "rowappz16":rowappz16, "rowappz17":rowappz17, "rowappz18":rowappz18, "rowappz19":rowappz19, "rowappz20":rowappz20}
	return render(request, template, context)

"""====================================="""
"""=====SUBCATEGORY INDIVIDUAL PAGE====="""
"""====================================="""

def SubCategoryPage(request, s_id):
	"""Individual SubCategory Page Method"""
	sub_category = SubCategory.objects.get(pk=s_id)
	applications_list = Application.objects.filter(app_subcategory=sub_category).order_by('-app_ratingcount')
	paginator = Paginator(applications_list, 32)
	page = request.GET.get('page')
	subcat = SubCategory.objects.all()
	try:
		applications = paginator.page(page)
	except PageNotAnInteger:
		applications = paginator.page(1)
	except EmptyPage:
		applications = paginator.page(paginator.num_pages)


	total_pages = applications.paginator.num_pages+1
	template = "SubCategory.html"
	context = {"applications":applications, "subcategory":sub_category, "subcats":subcat, 'range': range(1,total_pages)}
	return render(request, template, context)

"""================================="""
"""=====APPLICATION DETAIL PAGE====="""
"""================================="""

def AppDetailPage(request, a_id):
	"""Application Detail Page Method"""
	app_obj = Application.objects.get(pk=a_id)
	similar_apps = Application.objects.filter(app_subcategory=app_obj.app_subcategory).order_by('-app_ratingcount')
	publisher_apps = Application.objects.filter(app_publisher=app_obj.app_publisher).order_by('?')
	app_image = ApplicationImage.objects.filter(app_name=app_obj)
	subcat = SubCategory.objects.all()
	template = "description.html"
	context = {"app_detail":app_obj, "similar_apps":similar_apps,"subcats":subcat, "publisher_apps":publisher_apps, "app_image":app_image}
	return render(request, template, context)

"""================================="""
"""======PUBLISHER DETAIL PAGE======"""
"""================================="""

def PublisherPage(request, p_id):
	"""Publisher Page Method"""
	publisher = Publisher.objects.get(pk=p_id)
	publisher_apps = Application.objects.filter(app_publisher=publisher)
	subcat = SubCategory.objects.all()
	template = "publisher.html"
	context = {"publisher":publisher,"subcats":subcat, "publisher_apps":publisher_apps,}
	return render(request, template, context)

"""=============================="""
"""=====APPS AND GAMES PAGES====="""
"""=============================="""

def AppPagePopular(request):
	"""Popular Page Apps Method"""
	subcat = SubCategory.objects.all()
	category = Category.objects.first()
	sub_category = SubCategory.objects.filter(category=category)
	applications = Application.objects.filter(app_subcategory=sub_category).order_by('-app_ratingcount')
	featured = Featured.objects.filter(featured_type='2')
	template = "AppPopular.html"
	context = {"applications":applications,"subcats":subcat, "subcategory":sub_category, "category":category, "featured":featured,}
	return render(request, template, context)

def AppPageChart(request):
	"""Chart Page Apps Method"""
	subcat = SubCategory.objects.all()
	category = Category.objects.first()
	topfree = TopFree.objects.filter(category=category).order_by('app_rank')
	topnewfree = TopNewFree.objects.filter(category=category).order_by('app_rank')
	trending = Trending.objects.filter(category=category).order_by('app_rank')

	template = "AppChart.html"
	context = {"topfree":topfree,"subcats":subcat, "topnewfree":topnewfree, "trending":trending,}
	return render(request, template, context)

def GamePagePopular(request):
	"""Popular Page Games Method"""
	subcat = SubCategory.objects.all()
	category = Category.objects.last()
	sub_category = SubCategory.objects.filter(category=category)
	applications = Application.objects.filter(app_subcategory=sub_category).order_by('-app_ratingcount')
	featured = Featured.objects.filter(featured_type='3')
	template = "GamePopular.html"
	context = {"applications":applications,"subcats":subcat, "subcategory":sub_category, "category":category, "featured":featured,}
	return render(request, template, context)

def GamePageChart(request):
	"""Chart Page Games Method"""
	subcat = SubCategory.objects.all()
	category = Category.objects.last()
	topfree = TopFree.objects.filter(category=category).order_by('app_rank')
	topnewfree = TopNewFree.objects.filter(category=category).order_by('app_rank')
	trending = Trending.objects.filter(category=category).order_by('app_rank')

	template = "GameChart.html"
	context = {"topfree":topfree,"subcats":subcat, "topnewfree":topnewfree, "trending":trending,}
	return render(request, template, context)

"""=============================================="""
"""======APPLICATIONS INDIVIDUAL CHART PAGE======"""
"""=============================================="""

def APPTopFreeChartPage(request):
	subcat = SubCategory.objects.all()
	all_category = Category.objects.first()
	topfree = TopFree.objects.filter(category=all_category).order_by('app_rank')

	template = "apptopfreechart.html"
	context = {"topfree":topfree,"subcats":subcat, "category":all_category,}
	return render(request, template, context)

def APPTopNewFreeChartPage(request):
	subcat = SubCategory.objects.all()
	all_category = Category.objects.first()
	topnewfree = TopNewFree.objects.filter(category=all_category).order_by('app_rank')

	template = "apptopnewfreechart.html"
	context = {"topnewfree":topnewfree,"subcats":subcat, "category":all_category,}
	return render(request, template, context)

def APPTrendingChartPage(request):
	subcat = SubCategory.objects.all()
	all_category = Category.objects.first()
	trending = Trending.objects.filter(category=all_category).order_by('app_rank')

	template = "apptrendingchart.html"
	context = {"trending":trending,"subcats":subcat, "category":all_category,}
	return render(request, template, context)

"""======================================="""
"""======GAMES INDIVIDUAL CHART PAGE======"""
"""======================================="""

def GAMETopFreeChartPage(request):
	subcat = SubCategory.objects.all()
	all_category = Category.objects.last()
	topfree = TopFree.objects.filter(category=all_category).order_by('app_rank')

	template = "gametopfreechart.html"
	context = {"topfree":topfree,"subcats":subcat, "category":all_category,}
	return render(request, template, context)

def GAMETopNewFreeChartPage(request):
	subcat = SubCategory.objects.all()
	all_category = Category.objects.last()
	topnewfree = TopNewFree.objects.filter(category=all_category).order_by('app_rank')

	template = "gametopnewfreechart.html"
	context = {"topnewfree":topnewfree,"subcats":subcat, "category":all_category,}
	return render(request, template, context)

def GAMETrendingChartPage(request):
	subcat = SubCategory.objects.all()
	all_category = Category.objects.last()
	trending = Trending.objects.filter(category=all_category).order_by('app_rank')

	template = "gametrendingchart.html"
	context = {"trending":trending,"subcats":subcat, "category":all_category,}
	return render(request, template, context)


# @login_required
# def WishListPage(request):
# 	"""Wish List Page"""
# 	favors = Favorite.objects.filter(user=request.user)
# 	fav_apps = favors.favorite_apps.all()

# 	context = {"favors":favors, "fav_apps":fav_apps,}
# 	template = 'wishlist.html'
# 	return render(request, template, context)

# @login_required
# def FavAdd(request, app_id):
# 	"""Add Application to Wish List Method"""
# 	favors = Favorite.objects.filter(user=request.user)
# 	application = Application.objects.get(pk=app_id)
# 	favors = Favorite.objects.get_or_create(user=request.user, favorite_apps=application)
# 	messages.info(request, 'Application added to Wish List.',fail_silently=True)
# 	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# @login_required
# def FavDelete(request, app_id):
# 	"""Delete Application from Wish List Method"""
# 	favors = Favorite.objects.filter(user=request.user)
# 	application_to_delete = get_object_or_404(Favorite, pk=app_id).delete()
# 	messages.info(request, 'Application removed from Wish List.',fail_silently=True)
# 	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@api_view(['GET','POST'])
def gettrendingApps(request):
	item=[]
	app1=SerfoApp.objects.filter(rowno='1')
	for j in app1:
		response1 = {}
		response1['apptype'] = j.rowno
		response1['name'] = j.applications.app_name
		response1['iconurl'] = j.applications.app_icon_url
		response1['appid'] = j.applications.id
		response1['publisher'] = j.applications.app_publisher.name
		response1['rating'] = j.applications.app_rating
		item.append(response1)
	
	data=item
	return Response({"data":data, 'status':200})

@api_view(['GET','POST'])
def getpopularApps(request):
	item=[]
	app2=SerfoApp.objects.filter(rowno='2')
	for k in app2:
		response2 = {}
		response2['apptype'] = k.rowno
		response2['name'] = k.applications.app_name
		response2['iconurl'] = k.applications.app_icon_url
		response2['appid'] = k.applications.id
		response2['publisher'] = k.applications.app_publisher.name
		response2['rating'] = k.applications.app_rating
		item.append(response2)
	
	data=item
	return Response({"data":data, 'status':200})

@api_view(['GET','POST'])
def getApps(request):
	item=[]
	app1=SerfoApp.objects.filter(rowno='1')
	app2=SerfoApp.objects.filter(rowno='2')
	for j in app1:
		response1 = {}
		response1['apptype'] = j.rowno
		response1['name'] = j.applications.app_name
		response1['iconurl'] = j.applications.app_icon_url
		response1['appid'] = j.applications.id
		response1['publisher'] = j.applications.app_publisher.name
		response1['rating'] = j.applications.app_rating
		item.append(response1)

	for k in app2:
		response2 = {}
		response2['apptype'] = k.rowno
		response2['name'] = k.applications.app_name
		response2['iconurl'] = k.applications.app_icon_url
		response2['appid'] = k.applications.id
		response2['publisher'] = k.applications.app_publisher.name
		response2['rating'] = k.applications.app_rating
		item.append(response2)
	
	data=item
	return Response({"data":data, 'status':200})








