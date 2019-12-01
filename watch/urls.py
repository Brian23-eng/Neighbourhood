from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$', views.home, name='home'),
    url(r'^all-hoods/',views.hoods, name='hood'),
    url(r'^new-hood/', views.create_hood, name='new-hood'),
    
    url(r'^profile/(?P<username>[\w.@+-]+)/$',views.profile,name='profile'),
    url(r'^profile/(?P<username>\w+)/edit', views.edit_profile, name='edit-profile'),
    url(r'^join_hood/(?P<id>)',views.join_hood, name='join-hood'),
    url(r'^leave_hood/(?P<id>)', views.leave_hood, name='leave-hood'),
    url(r'^single_hood/(?P<hood_id>\d+)', views.single_hood, name = 'single-hood'),
    url(r'^(?P<hood_id>\d+)/new-post', views.create_post, name='post'),
    url(r'^(?P<hood_id>\d+)/members', views.hood_members, name='members'),
    url(r'^search/', views.search_business, name='search'),
    
]