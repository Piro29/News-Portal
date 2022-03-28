from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sources', views.sources, name='sources'),
    path('singlepost', views.singlepost, name='singlepost'),
    path('business', views.business, name='business'),
    path('entertainment', views.entertainment, name='entertainment'),
    path('health', views.health, name='health'),
    path('sports', views.sports, name='sports'),
    path('technology', views.technology, name='technology'),
    path('general', views.general, name='general'),
    path('science', views.science, name='science'),
    path('search', views.search, name='search'),
    path('addnews', views.addnews, name='addnews'),
    path('postednews', views.postednews, name='postednews'),
]
