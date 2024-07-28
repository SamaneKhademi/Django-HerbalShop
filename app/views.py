from urllib import request
from django.http import HttpResponse
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Customer, Cart, Wishlist
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.contrib.auth import logout
from django.db.models import Q


def home(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'app/index.html', locals())

def about(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'app/about.html', locals())

def contact(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'app/contact.html', locals())

class CategoryView(View):
    def get(self, request, val):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request, 'app/category.html', locals())

class CategoryTitle(View):
    def get(self, request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/category.html', locals())


class AllProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/all-products.html', locals())

class ProductDetail(View):
    def get(self, request, pk):
        user = request.user
        product = Product.objects.get(pk=pk)
        if user.is_authenticated:
            wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=request.user))
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/product-detail.html', locals())

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/customerregistration.html', locals())
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ثبت نام با موفقیت انجام شد')
        else:
            messages.warning(request, 'مقادیر ورودی نامعتبر است')
        return render(request, 'app/customerregistration.html', locals())

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/profile.html', locals())
    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            locality = form.cleaned_data['locality']
            zipcode = form.cleaned_data['zipcode']

            reg = Customer(user=user, name=name, mobile=mobile, state=state, city=city, locality=locality, zipcode=zipcode)
            reg.save()
            messages.success(request, 'اطلاعات با موفقیت ثبت شد.')
        else:
            messages.warning(request, 'مقادیر ورودی نامعتبر است.')
        return render(request, 'app/profile.html', locals())

def address(request):
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'app/address.html', locals())

class updateAddress(View):
    def get(self, request, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'app/updateAddress.html', locals())
    def post(self, request, pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.city = form.cleaned_data['city']
            add.locality = form.cleaned_data['locality']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, 'اطلاعات با موفقیت بروزرسانی شد.')
        else:
            messages.warning(request, 'مقادیر ورودی نامعتبر است.')
        return redirect('address')


def LogoutView(request):
    logout(request)
    return redirect('login')

def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user, product=product).save()
    return redirect('/cart')

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40000
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user=request.user))
        wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'app/addtocart.html', locals())

class checkout(View):
    def get(self, request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user=request.user))
            wishitem = len(Wishlist.objects.filter(user=request.user))
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        famount=0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            famount = famount + value
        totalamount = famount + 40000
        return render(request, 'app/checkout.html', locals())


def plus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        #print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()

        user= request.user
        cart= Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40000

        data={
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        #print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()

        user= request.user
        cart= Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40000

        data={
            'quantity': c.quantity,
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)

def remove_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        #print(prod_id)
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()

        user= request.user
        cart= Cart.objects.filter(user=user)
        amount=0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 40000

        data={
            'amount': amount,
            'totalamount': totalamount
        }
        return JsonResponse(data)

def plus_wishlist(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist(user=user, product=product).save()
        data={
            'message': 'به موارد دلخواه اضافه شد.'
        }
        return JsonResponse(data)

def minus_wishlist(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist.objects.filter(user=user, product=product).delete()
        data={
            'message': 'از موارد دلخواه حذف شد.'
        }
        return JsonResponse(data)

