from petal2 import views
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import signupForm, InvoiceForm
from .models import SliderItem, Product, SpecialProduct, Category, CartItem, Customer, Invoice
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect

# Create your views here.


def base(request):
    return render(request, 'petal2/base.html')


def invoice(request):
    return render(request, 'petal2/invoice.html')


def cart(request, product_id=None):
    if product_id is not None:

        product = get_object_or_404(Product, pk=product_id)

        if request.user.is_authenticated:
            price = product.price
            cart_item, created = CartItem.objects.get_or_create(
                user=request.user, product=product, price=price)

            if not created:
                cart_item.quantity += 1
                cart_item.save()
            cart_url = reverse('cart')
            return redirect('cart')

    if request.user.is_authenticated:

        cart_items = CartItem.objects.filter(user=request.user)
    else:
        cart_items = []

    for cart_item in cart_items:
        cart_item.subtotal = cart_item.product.price * cart_item.quantity
        cart_item.save()

    subtotal = calculate_subtotal(cart_items)

    total = calculate_total(subtotal)

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'total': total
    }

    return render(request, 'petal2/cart.html', context)


def calculate_subtotal(cart_items):
    subtotal = 0
    for item in cart_items:
        subtotal += item.product.price * item.quantity
    return subtotal


def calculate_total(subtotal):
    return subtotal


def remove_from_cart(request, cart_item_id):
    if request.user.is_authenticated:
        # Get the cart item for the current user based on cart_item_id
        cart_item = get_object_or_404(
            CartItem, id=cart_item_id, user=request.user)

        # Remove the cart item
        cart_item.delete()

    # Redirect back to the cart page or any other appropriate page
    return redirect('cart')


def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = Invoice(
                customer=request.user,
                invoice_date=form.cleaned_data['invoice_date'],
                due_date=form.cleaned_data['due_date'],
                total_amount=form.cleaned_data['total_amount'],
                # Populate other fields from the form
            )
            invoice.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'petal2/create_invoice.html', {'form': form})


@login_required
def payment(request):
    # Get the logged-in user and their associated Customer profile (if it exists)
    user = request.user
    try:
        customer = user.customer
    except Customer.DoesNotExist:
        customer = None

    # Replace the following lines with actual data retrieval as needed
    product = Product.objects.get(id=1)
    cart_items = CartItem.objects.filter(user=request.user)
    subtotal = calculate_subtotal(cart_items)
    total = calculate_total(subtotal)
    vat = 6
    totalvat = total + vat
    customer_address = request.GET.get('customer_address')
    product_price = request.GET.get('product_price')
    customer = request.user,

    context = {
        'product': product,
        'customer': customer,
        'cart_items': cart_items,
        'subtotal': subtotal,
        'total': total,
        'customer_address': customer_address,
        'product_price': product_price,
        'customer': customer,
        'totalvat': totalvat,
        'vat': vat

    }

    return render(request, 'petal2/payment.html', context)


def details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'petal2/details.html', {'product': product})


def categorybag(request, category_name=None):
    Categories = Category.objects.all()

    if category_name:
        category = get_object_or_404(Category, name=category_name)
        products = Product.objects.filter(Category=category)
        SpecialProducts = SpecialProduct.objects.filter(Category=category)

    else:
        products = Product.objects.order_by('price')
        SpecialProducts = SpecialProduct.objects.all()

    return render(request, 'petal2/categorybag.html', {'products': products, 'Categories': Categories, 'SpecialProducts': SpecialProducts})


def home(request):
    slider_items = SliderItem.objects.all()
    return render(request, 'petal2/home.html', {'slider_items': slider_items})


@csrf_protect
def signup(request):
    if request.method == "POST":
        new_form = signupForm(request.POST)
        if new_form.is_valid():
            user = new_form.save()

            customer, created = Customer.objects.get_or_create(user=user)
            if created:
                customer.first_name = new_form.cleaned_data['first_name']
                customer.last_name = new_form.cleaned_data['last_name']
                customer.save()

            login(request, user)

            return redirect('/user_login/')

    else:
        new_form = signupForm()
    return render(request, 'petal2/signup.html', {'form': new_form})


def create_customers_for_existing_users():
    users = User.objects.all()
    for user in users:
        customer, created = Customer.objects.get_or_create(user=user)


@csrf_protect
def user_login(request):
    if request.method == "POST":
        new_form = AuthenticationForm(request=request, data=request.POST)
        if new_form.is_valid():
            username = new_form.cleaned_data['username']
            password = new_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
    else:
        new_form = AuthenticationForm()
    return render(request, 'petal2/login.html', {'form': new_form})


def user_profile(request, category_name=None):
    slider_items = SliderItem.objects.all()
    Categories = Category.objects.all()

    return render(request, 'petal2/profile.html', {'name': request.user, 'slider_items': slider_items, 'Categories': Categories})


def user_logout(request):
    logout(request)
    return HttpResponse('/login/')
