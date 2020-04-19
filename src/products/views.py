from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, Http404
from .models import Product


# Create your views here.

class ProductFeaturedListView(ListView):
	#queryset = Product.objects.all()
	template_name = "products/list.html"			# object_list is by default

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
	queryset = Product.objects.all().featured()
	template_name = "products/featured-detail.html"			# object_list is by default

	# def get_queryset(self, *args, **kwargs):
	# 	request = self.request
	# 	return Product.objects.featured()


class ProductListView(ListView):
	#queryset = Product.objects.all()
	template_name = "products/list.html"			# object_list is by default

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Product.objects.all()

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ProductListView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context


def product_list_view(request):
	qs = Product.objects.all()
	context = {
	'object_list': qs,						# object_list is by default
	}
	return render(request, "products/list.html", context)


class ProductDetailSlugView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_object(self, *args, **kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		#instance = get_object_or_404(Product, slug = slug)
		try:
			instance = Product.objects.get(slug = slug)
		except Product.DoesNotExist:
			raise Http404("Not found")
		except Product.MultipleObjectsReturned:
			qs = Product.objects.filter(slug = slug)
			instance = qs.first()
		except:
			raise Http404("Umjffjf")	
				
		return instance


class ProductDetailView(DetailView):
	#queryset = Product.objects.all()
	template_name = "products/detail.html"			# object_list is by default

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context

	def get_object(self, *args, **kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instance = Product.objects.get_by_id(pk)
		if instance is None:
			raise Http404("product not found")
		else:
			return instance


def product_detail_view(request, pk=None, *args, **kwargs):
	#instance = get_object_or_404(Product, pk = pk)

	instance = Product.objects.get_by_id(pk)
	print(instance)
	if instance is None:
		raise Http404("product not found")
	# qs = Product.objects.filter(id = pk)
	# if qs.count() == 1:
	# 	instance = qs.first()
	# else:
	# 	raise Http404("product not found")	

	context = {
	'object': instance,						# object_list is by default
	}
	return render(request, "products/detail.html", context)