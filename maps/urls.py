"""maps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

from .models import ObjectSpot, ObjectPoint
#from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^data.geojson$', GeoJSONLayerView.as_view(model=ObjectSpot, properties=('title', 'description', 'type', 'picture_url')), name='data'),
    url(r'^spots.geojson$', GeoJSONLayerView.as_view(model=ObjectSpot, properties=('title', 'description', 'type', 'picture_url')), name='spots'),
    url(r'^points.geojson$', GeoJSONLayerView.as_view(model=ObjectPoint, properties=('title', 'description', 'type', 'picture_url')), name='points'),
    #url(r'^location/(?P<pk>[0-9]+)/$', views.location, name='location'),
] + static(settings.MEDIA_URL, document_root=settings.IMAGE_DIR)
#] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

