from django.shortcuts import render, get_object_or_404
from .models import Category, Subcategory, Subsubcategory, Brand, Product,  Product_image

def catalog(request):
    category = None
    categories = Category.objects.all().order_by("id")
    subcategory = None
    subcategories = Subcategory.objects.all().order_by("id")
    subsubcategory =  None
    subsubcategories = Subsubcategory.objects.all().order_by("id")
    brand = None
    brands = Brand.objects.all()
    products = Product.objects.all()
    return render(request,
                  "main/catalog.html",
                  {'category': category,
                   'categories': categories,
                   'subcategory': subcategory,
                   'subcategories': subcategories,
                   'subsubcategory': subsubcategory,
                   'subsubcategories': subsubcategories,
                   'brand': brand,
                   'brands': brands,
                   'products': products
                  })

def listing(request, subsubcategory_slug=None):
    subsubcategory = None
    subsubcategories = Subsubcategory.objects.all()
    product = None
    products = Product.objects.all()
    image = None
    images = Product_image.objects.all()
    brand = None
    brands = Brand.objects.all()
    if subsubcategory_slug:
        subsubcategory = get_object_or_404(Subsubcategory, slug=subsubcategory_slug)
        products = products.filter(subsubcategory=subsubcategory)
        images = images.filter(product=product)
    return render(request,
                  "main/listing.html",
                  {'subsubcategory': subsubcategory,
                   'image': image,
                   'brand': brand,
                   'brands': brands,
                   'images': images,
                   'subsubcategories': subsubcategories,
                   'product': product,
                   'products': products})

def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def account(request):
    return render(request, "main/account.html")

def cart(request):
    return render(request, "main/cart.html")

def checkout(request):
    return render(request, "main/checkout.html")

def contact(request):
    return render(request, "main/contact.html")

def myaccount(request):
    return render(request, "main/my-account.html")

def  productdetails(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug)
    return render(request,
                  "main/product-details.html",
                  {'product': product})


def wishlist(request):
    return render(request, "main/wishlist.html")

def shop(request):
    return render(request, "main/shop.html")

def sandbox(request):
    return render(request, "main/sandbox.html")
