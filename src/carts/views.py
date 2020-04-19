from django.shortcuts import render, redirect
from products.models import Product

from .models import Cart
# Create your views here.

def cart_home(request):

	#del request.session["cart_id"]
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	cart_obj.save()	
	return render(request, "carts/home.html", {"cart":cart_obj})


def cart_update(request):
	product_id = request.POST.get('product_id')
	if product_id is not None:
		try:
			product_obj = Product.objects.get(id = product_id)
		except Product.DoesNotExist:
			print("No products")
			return redirect("cart:home")	
		#print(prod_obj)
		cart_obj, new_obj = Cart.objects.new_or_get(request)
		if product_obj in cart_obj.products.all():
			cart_obj.products.remove(product_obj)
		else:
			cart_obj.products.add(product_obj)	
		request.session['cart_items'] = cart_obj.products.count()	
	return redirect("cart:home")
