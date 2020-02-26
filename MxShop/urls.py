"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from MxShop.settings import MEDIA_ROOT
from django.views.static import serve
# from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

# from goods.views import GoodsListView
from goods.views import GoodsListViewSet, CategoryViewSet, BannerViewSet, HotwordsViewSet, IndexCategoryViewset
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from users.views import UserViewset
from trade.views import ShoppingCartViewset, OrderViewset
router = DefaultRouter()

router.register(r'goods', GoodsListViewSet, basename="goods")
router.register(r'categorys', CategoryViewSet, basename="categorys")
router.register(r'userfavs', UserFavViewset, basename="userfavs")
router.register(r'users', UserViewset, basename="users")
router.register(r'messages', LeavingMessageViewset, basename="messages")
router.register(r'address', AddressViewset, basename="address")
router.register(r'shopcarts', ShoppingCartViewset, basename="shopcarts")
router.register(r'orders', OrderViewset, basename="orders")
router.register(r'banners', BannerViewSet, basename="banners")
router.register(r'hotsearchs', HotwordsViewSet, basename="hotsearchs")
router.register(r'indexgoods', IndexCategoryViewset, basename="indexgoods")
#customise register
# goods_list = GoodsListViewSet.as_view({
#     'get':'list',
#     'post': 'create'
# })

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^', include(router.urls)),
    #product list
    # url(r'goods/$', GoodsListView.as_view(), name="goods-list"),
    url(r'^login/', obtain_jwt_token),
    # url(r'docs/', include_docs_urls(title="MxShop"))
    path('openapi', get_schema_view(
        title="MxShop",
        description="API for MxShop"
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
