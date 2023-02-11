from django.urls import path, re_path
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('account', views.account, name="account"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('contact', views.contact, name="contact"),
    path('myaccount', views.myaccount, name="myaccount"),
    path('shop', views.shop, name="shop"),
    path('wishlist', views.wishlist, name="wishlist"),
    path('sandbox', views.sandbox, name="sandbox"),
    path('catalog', views.catalog, name="catalog"),
    re_path(r'^$', views.listing, name='listing'),
    re_path(r'^(?P<subsubcategory_slug>[-\w]+)/$', views.listing, name='listing_subsubcategory'),

]