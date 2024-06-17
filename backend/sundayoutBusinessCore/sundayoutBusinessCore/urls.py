from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),
    re_path('create_business', views.create_business),
    re_path('get_businesses', views.get_businesses)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)