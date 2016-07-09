from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
from django_countries.fields import CountryField

_APP_NAME = 'appstore'
# class UserProfile(models.Model):
# 	"""User Profile Class"""
# 	user = models.OneToOneField(User, primary_key=True, related_name='appstore_users')
# 	phone_number = models.CharField(max_length=15, null=True)
# 	country = CountryField(blank_label='(Select Country)')
# 	pincode = models.CharField(max_length=15, null=True)
# 	date_of_birth = models.DateField(null=True)
# 	image = models.ImageField(upload_to='imgs/', null=True)

# 	GENDER_CHOICES = (
# 		('M', 'Male'),
# 		('F', 'Female'),
# 		('X', 'Other'),
# 	)
# 	gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True, null=True)

# 	class Meta:
# 		db_table = "appstore_userprofile"
# 		verbose_name_plural = "User Profile"
# 		abstract = True

# 	def __unicode__(self):
# 		return unicode(self.user)

# 	class Meta:
# 		app_label = _APP_NAME

class Publisher(models.Model):
	"""Publisher of the Application"""
	name = models.CharField(max_length=100, null=True)
	slug = AutoSlugField(populate_from='name', null=True)

	def __str__(self):
		return self.name

class Category(models.Model):
	"""Application Categories"""
	category_name = models.CharField(max_length=100, null=True)
	category_slug = AutoSlugField(populate_from='category_name', null=True)

	def __str__(self):
		return self.category_name

	def get_subs(self):
		return SubCategory.objects.filter(category=self)


class SubCategory(models.Model):
	"""Application Categories"""
	subcategory_name = models.CharField(max_length=100, null=True)
	category = models.ForeignKey(Category, blank=True, null=True)
	subcategory_slug = AutoSlugField(populate_from='subcategory_name', null=True)
	icon = models.ImageField(upload_to='imgs/', null=True)

	def __str__(self):
		return self.subcategory_name

	def get_apps(self):
		return Application.objects.filter(app_subcategory=self).order_by('-app_ratingcount')

class Application(models.Model):
	"""Applications and Games"""
	app_name = models.CharField(max_length=100, null=True, blank=True)
	app_icon_url = models.CharField(max_length=255, null=True, blank=True)
	app_slug = AutoSlugField(populate_from='app_name', null=True)
	app_description = models.TextField(null=True, blank=True)
	app_publisher = models.ForeignKey(Publisher, blank=True, null=True)
	app_category = models.ForeignKey(Category, blank=True, null=True)
	app_subcategory = models.ForeignKey(SubCategory, blank=True, null=True)
	app_ratingcount = models.DecimalField(max_digits=20, decimal_places=0, null=True, blank=True)
	app_rating = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	app_pubdate = models.CharField(max_length=25, null=True, blank=True)
	app_version = models.CharField(max_length=10, null=True, blank=True)
	app_size = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	app_url = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return self.app_name

class ApplicationImage(models.Model):
	"""Application Image Class"""
	image_url = models.CharField(max_length=255, null=True, blank=True)
	app_name = models.ForeignKey(Application)

	def __str__(self):
		return self.app_name.app_name

class Featured(models.Model):
	"""Featured Applications Class"""
	application = models.ForeignKey(Application, null=True, blank=True)
	image = models.ImageField(upload_to='featured/', null=True)
	FD_TYPE = (
		('1', 'HomeScreen_Banner'),
		('2', 'App_Banner'),
		('3', 'Game_Banner'),
	)
	featured_type = models.CharField(max_length=2, choices=FD_TYPE, null=True)

# class Recommendation(models.Model):
# 	"""Recommended Applications Class"""
# 	user = models.ForeignKey(User)
# 	application = models.ManyToManyField(Application)
# 	REC_TYP = (
# 		('1', 'HomeScreen_CategoryRecommendations'),
# 		('2', 'HomeScreen_RecentInstalls'),
# 		('3', 'AppDetail_Recommendations'),
# 		('4', 'Nearby_Recommendations'),
# 		('5', 'SimilarUser_Recommendations'),
# 	)
# 	rec_type = models.CharField(max_length=2, choices=REC_TYP, null=True)


class TopFree(models.Model):
	"""Top Free Applications Class"""
	application = models.ForeignKey(Application, null=True, blank=True)
	app_rank = models.IntegerField(default="1", null=True)
	category = models.ForeignKey(Category, null=True, blank=True)

class TopNewFree(models.Model):
	"""Top New Free Applications Class"""
	application = models.ForeignKey(Application, null=True, blank=True)
	app_rank = models.IntegerField(default="1", null=True)
	category = models.ForeignKey(Category, null=True, blank=True)

class Trending(models.Model):
	"""Trending Applications Class"""
	application = models.ForeignKey(Application, null=True, blank=True)
	app_rank = models.IntegerField(default="1", null=True)
	category = models.ForeignKey(Category, null=True, blank=True)

# class Favorite(models.Model):
# 	"""User Favorites Class"""
# 	user = models.ForeignKey(User)
# 	favorite_apps = models.ForeignKey(Application, null=True, blank=True)

