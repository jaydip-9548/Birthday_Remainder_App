
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('API.urls')),
    path('',include('API_SignIn_Up.urls')),
    # path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    # path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'),
    # path('refreshtoken',TokenRefreshView.as_view(),name='token_refresh'),
    # path('',TemplateView.as_view(template_name='index.html')),
    
]
