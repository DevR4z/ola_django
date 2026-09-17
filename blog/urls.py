from django.urls import path
from blog import views as blog_views

urlpatterns = [
    path('exemplo/', blog_views.exemplo),
    path('', blog_views.blog),
]
