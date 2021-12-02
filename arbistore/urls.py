from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from arbistore.views import Categories, CategoryProductFetch, ProductFetch, ProductList, RegisterView, \
    TokenObtainPairView, TokenVerifyView, SubCategoryProductFetch

urlpatterns = [
                  path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('verify/', TokenVerifyView.as_view(), name='verify'),
                  path('products/', ProductList.as_view(), name='products'),
                  path('categories/', Categories.as_view(), name='categories'),
                  path('register/', RegisterView.as_view(), name='register'),
                  path('category/<int:pk>/', CategoryProductFetch.as_view(), name='category_products_fetch'),
                  path('subcategory/<int:pk>/', SubCategoryProductFetch.as_view(), name='sub_category_products_fetch'),
                  path('product_view/<int:pk>/', ProductFetch.as_view(), name='product_fetch'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('api-auth/', include('rest_framework.urls')),
              ]
