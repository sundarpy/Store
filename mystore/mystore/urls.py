
from django.conf.urls import url, include
from django.contrib import admin
from appstore import views, api
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^read/', api.read_file, name='read_file'),
    url(r'^$', views.HomePage, name='home'),
    url(r'^appdetails/(?P<a_id>\d+)/$', views.AppDetailPage, name='appdetail'),
    url(r'^publisherdetails/(?P<p_id>\d+)/$', views.PublisherPage, name='pubdetail'),
    url(r'^subcategory/(?P<s_id>\d+)/$', views.SubCategoryPage, name='subcatdetail'),
    url(r'^results/$', views.search, name='results'),

    url(r'^app/popular/', views.AppPagePopular, name='apppopular'),
    url(r'^app/charts/', views.AppPageChart, name='appchart'),
    url(r'^game/popular/', views.GamePagePopular, name='gamepopular'),
    url(r'^game/charts/', views.GamePageChart, name='gamechart'),

    url(r'^app/topfree', views.APPTopFreeChartPage, name='apptopfree'),
    url(r'^app/topnewfree', views.APPTopNewFreeChartPage, name='apptopnewfree'),
    url(r'^app/trending', views.APPTrendingChartPage, name='apptrending'),

    url(r'^game/topfree', views.GAMETopFreeChartPage, name='gametopfree'),
    url(r'^game/topnewfree', views.GAMETopNewFreeChartPage, name='gametopnewfree'),
    url(r'^game/trending', views.GAMETrendingChartPage, name='gametrending'),

    url(r'^gettrendingApps/', views.gettrendingApps, name='gettrendingApps'),
    url(r'^getpopularApps/', views.getpopularApps, name='getpopularApps'),
    url(r'^getApps/', views.getApps, name='getApps'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()