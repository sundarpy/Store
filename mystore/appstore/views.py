from django.shortcuts import render
from appstore.models import Publisher, Category, SubCategory, Application, ApplicationImage, Featured, TopFree, TopNewFree, Trending
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.views.decorators.csrf import csrf_protect

from django.shortcuts import render, HttpResponse, Http404, render_to_response, get_object_or_404
from django.template.loader import get_template
from django.template import Context, RequestContext, loader
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

	template = "home.html"
	context = {"applications":applications, "subcategory":sub_category, "subcats":subcats, "featured":featured,}
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



