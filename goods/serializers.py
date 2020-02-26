from rest_framework import serializers
from goods.models import Goods,IndexAd, GoodsCategory, GoodsImage, Banner, HotSearchWords, GoodsCategoryBrand
from django.db.models import Q
# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()

#     def create(self, validated_data):
#         return Goods.objects.create(**validated_data)
class CategorySerializer2(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class CategorySerializer1(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer1(many=True)
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GoodsImage
        fields =("image",)

class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = GoodsImageSerializer(many=True)
    class Meta:
        model = Goods
        fields = "__all__"

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

class HotSearchWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotSearchWords
        fields = "__all__"



class AdGoodsSerializer(serializers.ModelSerializer):
    images = GoodsImageSerializer(many=True)
    class Meta:
        model = Goods
        fields = ("id", "images")

class CategoryBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategoryBrand
        fields = "__all__"

class IndexCategorySerializer(serializers.ModelSerializer):
    brands = CategoryBrandSerializer(many=True)
    goods = serializers.SerializerMethodField()
    sub_cat = CategorySerializer2(many=True)
    ad_goods = serializers.SerializerMethodField()

    def get_goods(self, obj):
        all_goods = Goods.objects.filter(Q(category_id=obj.id)|Q(category__parent_category_id=obj.id)|Q(category__parent_category__parent_category_id=obj.id))
        goods_serializer = GoodsSerializer(all_goods, many=True, context={'request': self.context['request']})
        return goods_serializer.data
    
    def get_ad_goods(self, obj):
        goods_json = {}
        ad_goods = IndexAd.objects.filter(category_id = obj.id)
        if ad_goods:
            good_ins = ad_goods[0].goods
            goods_json = AdGoodsSerializer(good_ins, many=False, context={'request': self.context['request']}).data
        return goods_json

    class Meta:
        model = GoodsCategory
        fields = "__all__"