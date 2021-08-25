from django.urls.conf import include
from authentication.views import LoginViewSet, UserVieset, LoginSerializer
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserVieset.as_view(), name="users"),
    path('login/', LoginViewSet.as_view(), name="login"),

]
