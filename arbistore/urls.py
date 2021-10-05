from django.urls import include, path
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.conf import settings

from arbistore.views import Categories, ProductFetch, ProductList, RegisterView

urlpatterns = [
                  path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('verify/', TokenVerifyView.as_view(), name='verify'),
                  path('products/', ProductList.as_view(), name='products'),
                  path('categories/', Categories.as_view(), name='categories'),
                  path('register/', RegisterView.as_view(), name='register'),
                  path('product_view/<int:pk>/', ProductFetch.as_view(), name='product_fetch'),
                  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('api-auth/', include('rest_framework.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
