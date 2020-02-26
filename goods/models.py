from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.

class GoodsCategory(models.Model):
    """
    Goods Category
    """

    CATEGORY_TYPE =  (
        (1, "First Category"),
        (2, "Second Category"),
        (3, "Third Category"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="Category Name", help_text="Category Name")
    code = models.CharField(default="", max_length=30, verbose_name="Category Code", help_text="Category Code")
    desc = models.TextField(default="", verbose_name="Category Description", help_text="Category Description")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="Category Type", help_text="Category Type")
    parent_category= models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Parent Category", help_text="Parent Category", related_name="sub_cat")
    
    is_tab = models.BooleanField(default=False, verbose_name="isNav", help_text="Is Navigated")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add Time")

    class Meta:
        verbose_name = "Goods Category"  
        verbose_name_plural = verbose_name 
        
    def __str__(self):
        return self.name

         
class GoodsCategoryBrand(models.Model):
    """
    Brand Name
    """
    category = models.ForeignKey(GoodsCategory, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Category", related_name="brands")
    name= models.CharField(default="", max_length=30, verbose_name="Brand Name", help_text="Brand Name")
    desc = models.TextField(default="", max_length=200, verbose_name="Brand Description", help_text="Brand Description")
    image = models.ImageField(upload_to="brand/images", max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add Time")

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = verbose_name
        db_table = "goods_goodsbrand"
        
    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    Product
    """
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name="Category")
    goods_sn = models.CharField(max_length=50, default="", verbose_name="Goods Serial Name")
    name = models.CharField(max_length=100, verbose_name="Goods Name")
    click_num = models.IntegerField(default=0, verbose_name="Click Number")
    sold_num = models.IntegerField(default=0, verbose_name="Goods Sold Number")
    fav_num = models.IntegerField(default=0, verbose_name="Favourite Number")
    goods_num = models.IntegerField(default=0, verbose_name="Goods In Stock")
    market_price = models.FloatField(default=0, verbose_name="Maket Price")
    shop_price = models.FloatField(default=0, verbose_name="Current Price")
    goods_brief = models.TextField(max_length=500, verbose_name="Goods Brif Description")
    # goods_desc = models.TextField(verbose_name="Goods Details",  default='')
    goods_desc = UEditorField(verbose_name="content", imagePath="goods/images/", width=1000, height=300,
                              filePath="goods/files/", default='')
    ship_free = models.BooleanField(default=True, verbose_name="Is Ship Free")
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="Cover Image")
    is_new = models.BooleanField(default=False, verbose_name="Is Latest")
    is_hot = models.BooleanField(default=False, verbose_name="Is Hot")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add Time")

    class Meta:
        verbose_name = 'Goods'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class IndexAd(models.Model):
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name="Category")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="Goods Image", related_name="goods")

    class Meta:
        verbose_name = 'HomePage Category Advertisement'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name

class GoodsImage(models.Model):
    """
    Goods Images
    """

    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="Goods Image", related_name="images")
    image = models.ImageField(upload_to="goods/images/")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add Time")

    class Meta:
        verbose_name = "Product Images"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.goods.name

class Banner(models.Model):
    """
    Hero Banner Image
    """
    goods =  models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name = "Goods")
    image = models.ImageField(upload_to="banner", verbose_name="banner Image")
    index = models.IntegerField(default=0, verbose_name="Order of Image")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add Time")
    
    class Meta:
        verbose_name = "Banner Images"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.goods.name


class HotSearchWords(models.Model):
    """
    Hot Search keywords
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="Hot Keywords")
    index = models.IntegerField(default=0, verbose_name="Order Of Keywords")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="Add Time")

    class Meta:
        verbose_name = 'Hot Search Keywords'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords

