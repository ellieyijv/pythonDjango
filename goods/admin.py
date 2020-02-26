from django.contrib import admin
from django import forms

from django.contrib.admin import AdminSite
# Register your models here.
from .models import GoodsCategory, IndexAd, Goods, Banner, HotSearchWords, GoodsCategoryBrand



class GoodsCategoryAdmin(admin.ModelAdmin):
    actions_on_top=False
    actions_on_bottom=True
    
    def get_queryset(self, request):
        query = super(GoodsCategoryAdmin, self).get_queryset(request)
        filtered_query = query.filter(category_type= 1)
        return filtered_query
admin.site.register(GoodsCategory, GoodsCategoryAdmin)

class GoodsAdmin(admin.ModelAdmin):
    actions_on_top=False
    actions_on_bottom=True
    fields = ('name',  'category', 'goods_num', 'market_price', 'shop_price', 'sold_num', 'is_hot', 'is_new')
    list_display = ('name',  'category', 'goods_num', 'market_price', 'shop_price', 'sold_num', 'is_new')
    list_editable = ['goods_num', 'market_price', 'shop_price', 'sold_num', 'is_new']
admin.site.register(Goods, GoodsAdmin)

class BannerAdmin(admin.ModelAdmin):
    actions_on_top=False
    actions_on_bottom=True
    fields = ('goods', 'image', 'index')
    list_display = ('goods', 'image', 'index')
admin.site.register(Banner, BannerAdmin)

class HotSearchWordsAdmin(admin.ModelAdmin):   
    actions_on_top=False
    actions_on_bottom=True
    fields = ('keywords', 'index')
    list_display = ('keywords', 'index')
admin.site.register(HotSearchWords, HotSearchWordsAdmin)

class GoodsBrandForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GoodsBrandForm, self).__init__(*args, **kwargs)
        self.instance.category= "aa"
    
    # def get_category(self):
    #     self.instance.category = GoodsCategory.objects.filter(category_type=1) 
        

class GoodsBrandAdmin(admin.ModelAdmin):
    add_form = GoodsBrandForm
    fields=('category', 'image', 'name', 'desc')
    list_display=('category', 'image', 'name', 'desc')
   
admin.site.register(GoodsCategoryBrand, GoodsBrandAdmin)

class IndexAdAdmin(admin.ModelAdmin):
    list_display = ("category", "goods")
admin.site.register(IndexAd, IndexAdAdmin)