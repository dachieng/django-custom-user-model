from django.urls.conf import include
from authentication.views import APIAuthUser, LoginViewSet, UserVieset, LoginSerializer
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', APIAuthUser.as_view(), name="auth"),
    path('users/', UserVieset.as_view(), name="users"),
    path('login/', LoginViewSet.as_view(), name="login"),

]
