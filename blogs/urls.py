from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.index,{'blogname': ''}, name='home'),
    # path('<str:blogname>', views.index, name='index'),
]