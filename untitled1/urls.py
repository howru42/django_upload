"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import patterns as patterns
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from sampleapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^upload_html/', TemplateView.as_view(template_name="upload.html"), name="Upload Html"),
    url(r'^upload/', views.upload, name="Upload"),
]
urlpatterns += static(settings.PROFILE_PICS_URL, document_root=settings.PROFILE_PICS_ROOT)
urlpatterns += static(settings.GALLERY_PICS_URL, document_root=settings.GALLERY_PICS_ROOT)
