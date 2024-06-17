# configure all the urls.
from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView # this is the view we wrote inside the views.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # prebuilt views to obtain and refresh tokens

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/register/", CreateUserView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("api-auth/", include("rest_framework.urls")),# prebuilt urls from Django
    path("api/", include("api.urls")), # this is the urls.py file we created inside the api folder. We are linking the api urls into the main urls
]
