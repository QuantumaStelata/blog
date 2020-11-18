from django.conf.urls import url

from . import views


#app_name = 'blog'
urlpatterns = [
    url(r'article/(\d+)/leave_comment', views.leave_comment, name = 'leave_comment'),
    url(r'article/(\d+)', views.article, name = 'article'),
    url(r'', views.main, name = 'main'),
]