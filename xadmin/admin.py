from django.contrib import admin

from django.contrib.admin import AdminSite
# Register your models here.
from goods.models import GoodsCategory, Goods


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
    fields = ('name',  'category', 'goods_num', 'market_price', 'shop_price')
    list_display = ('name',  'category', 'goods_num', 'market_price', 'shop_price')
    list_editable = ['goods_num', 'market_price', 'shop_price']
admin.site.register(Goods, GoodsAdmin)
