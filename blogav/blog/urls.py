from django.conf.urls import url

from blogav.blog import views


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
