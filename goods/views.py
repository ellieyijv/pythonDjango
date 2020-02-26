
# Create your views here.
from goods.serializers import GoodsSerializer, CategorySerializer, BannerSerializer, HotSearchWordsSerializer, IndexCategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import  DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Goods, GoodsCategory, Banner, HotSearchWords
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .filters import GoodsFilter

# class GoodsListView(APIView):
#     """
#     Goods List
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)

#     def post(self, request, format=None):
#         serializer = GoodsSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##########################################################################
# class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
#     """
#     Goods List
#     """
#     queryset = Goods.objects.all()[:10]
#     serializer_class = GoodsSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


class GoodsPagination(PageNumberPagination):
    ###default size
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

# class GoodsListView(generics.ListAPIView):
#     """
#     Goods List
#     """
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsPagination


class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    throttle_classes = (UserRateThrottle, AnonRateThrottle)
    # filters is from rest_framework, not from django's
    filter_backends=(DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    #^start with, =exactly same
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'add_time')
    # filter_fields = ('name', 'shop_price')
    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get("price_min", 0)
    #     if price_min:
    #         queryset = queryset.filter(shop_price__gt=int(price_min))
    #     return queryset
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
        
##retrieveModelMixin is for 
class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(category_type = 1)
    serializer_class = CategorySerializer


class BannerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Banner.objects.all().order_by("index")
    serializer_class = BannerSerializer

class HotwordsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = HotSearchWords.objects.all()
    serializer_class = HotSearchWordsSerializer


class IndexCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    # in queryset filter name__in=["",]
    queryset = GoodsCategory.objects.filter(is_tab = True, name__in=["生鲜食品", "酒水饮料"] )
    serializer_class = IndexCategorySerializer