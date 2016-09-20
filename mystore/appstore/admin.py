from django.contrib import admin
from .models import Application, Publisher, Category, SubCategory, ApplicationImage, Featured, TopFree, TopNewFree, Trending, Collection, SerfoApp
# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
	list_display = ('app_name', 'app_publisher', 'app_category', 'app_subcategory', 'app_size', 'app_version', 'app_ratingcount')
	search_fields = ('app_name',)

class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category_name',)
	search_fields = ('category_name',)

class SubCategoryAdmin(admin.ModelAdmin):
	list_display = ('subcategory_name', 'category')
	search_fields = ('subcategory_name',)

class ApplicationImageAdmin(admin.ModelAdmin):
	list_display = ('app_name', 'image_url',)

class TopFreeAdmin(admin.ModelAdmin):
	list_display = ('application', 'app_rank', 'category',)

class TopNewFreeAdmin(admin.ModelAdmin):
	list_display = ('application', 'app_rank', 'category',)

class TrendingAdmin(admin.ModelAdmin):
	list_display = ('application', 'app_rank', 'category',)

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(ApplicationImage, ApplicationImageAdmin)
admin.site.register(Featured)
admin.site.register(Collection)
admin.site.register(SerfoApp)
admin.site.register(TopFree, TopFreeAdmin)
admin.site.register(TopNewFree, TopNewFreeAdmin)
admin.site.register(Trending, TrendingAdmin)

