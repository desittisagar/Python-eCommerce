from django.db import models
import random
import os
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
# Create your models here.

def get_filename_ext(filepath):
	basename = os.path.basename(filepath)
	name, ext = os.path.splitext(basename)
	return name, ext


def upload_image_path(instance, filename):
	new_filename = random.randint(1,1234)
	name, ext = get_filename_ext(filename)
	final_filename = f'{new_filename}{ext}'
	return f"products/{new_filename}/{final_filename}"


class ProductQuerySet(models.query.QuerySet):
	def featured(self):
		return self.filter(featured = True)					# Custome queryset

	def active(self):
		return self.filter(active = True)	


class ProductManager(models.Manager):						# Custome Model Manager

	def get_queryset(self):
		return ProductQuerySet(self.model, using = self._db)

	# def all(self):
	# 	return self.get_queryset().active()					# will return only active items Products.objectsa.all()

	def features(self):
		return self.get_queryset().featured()				# model manager feature

	def get_by_id(self, id):
		qs = self.get_queryset().filter(id = id)			# Product.objects == self.get_queryset()
		if qs.count() == 1:
			return qs.first()
		return None	


class Product(models.Model):
	title		= models.CharField(max_length = 100)
	slug 		= models.SlugField(blank = True, unique = True)
	description = models.TextField()
	price		= models.DecimalField(decimal_places = 2, max_digits = 20, default = 39.99)
	image		= models.ImageField(upload_to = upload_image_path, null = True, blank = True)
	featured	= models.BooleanField(default = False)
	active		= models.BooleanField(default = False)

	objects = ProductManager()

	def get_absolute_url(self):
		return f"/products/{self.slug}"


	def __str__(self):			# for python 3
		return self.title


	def __unicode__(self):		# for python 2
		return self.title	


def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender = Product)		