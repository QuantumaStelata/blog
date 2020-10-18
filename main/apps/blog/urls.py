from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'my_blog', views.my_blog, name = 'my_blog'),
    url(r'about_me', views.about_me, name = 'about_me'),
    url(r'', views.main, name = 'main'),
    
]