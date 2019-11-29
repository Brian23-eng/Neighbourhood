from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$', views.home, name='home'),
    url(r'^all-hoods/',views.hoods, name='hood'),
    url(r'^new-hood/', views.create_hood, name='new-hood'),
    url(r'^single-hood/', views.single_hood, name = 'single-hood')
]