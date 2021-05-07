"""yusufrefay_com_2020 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from blogs.views import DetailView,BlogsView,CategoryView,ContactView,PortfolioView,AboutView,ContactView,ResumeView
from django.conf import settings
from django.conf.urls.static import static
# from blogs import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include('blogs.urls')),
    path ('blogs', BlogsView, name='blogs'),
    path('blogs/<slug:slug>/', DetailView, name='detail'),
    path('category/<slug:slug>/', CategoryView, name='category'),
    path ('contact-me', ContactView, name='contact-me'),
    path ('about-me', AboutView, name='about-me'),
    path ('portfolio', PortfolioView, name='portfolio'),
    path ('resume', ResumeView, name='resume'),
]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)