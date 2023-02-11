from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering =  ["id"]
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    category = models.ForeignKey(Category,related_name="subcategories", on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering =  ["id"]
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.name

class Subsubcategory(models.Model):
    subcategory = models.ForeignKey(Subcategory, related_name='subsubcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ["id"]
        verbose_name = 'Subsubcategory'
        verbose_name_plural = 'Subsubcategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                        args=[self.slug])


class Brand(models.Model):
    name = models.CharField(max_length=200, db_index=True, null=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, null=True, default='')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name

class Product(models.Model):
    subsubcategory = models.ForeignKey(Subsubcategory, related_name='products', on_delete=models.CASCADE)
    rating = models.IntegerField(db_index=True, unique=True, null=True)
    brand = models.ForeignKey(Brand, related_name='products_brand', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ["id"]
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_last_image(self):
        try:
            last_image = self.product_image.image
        except AttributeError:
            last_image = self.image


class Product_image(models.Model):
    product = models.ForeignKey(Product, related_name='g', on_delete=models.CASCADE)
    rating = models.IntegerField(db_index=True, null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    size = models.BooleanField(default=True)

    class Meta:
        ordering = ["id"]
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return f'{self.product.name} image'




