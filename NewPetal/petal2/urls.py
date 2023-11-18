from django.urls import path, include
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('base/', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('user_login/', views.user_login, name='user_login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('details/', views.details, name='details'),
    path('payment/', views.payment, name='payment'),
    path('invoice/', views.invoice, name='invoice'),

    path('create_invoice/', views.create_invoice, name='create_invoice'),
    path('cart/', views.cart, name='cart'),
    path('cart/<int:product_id>/', views.cart, name='cart'),
    path('remove_from_cart/<int:cart_item_id>/',
         views.remove_from_cart, name='remove_from_cart'),

    path('categorybag/', views.categorybag, name='categorybag'),
    path('categorybag/<str:category_name>/',
         views.categorybag, name='categorybag_by_category'),
    path('products/<int:product_id>/', views.details, name='product_detail'),


]
