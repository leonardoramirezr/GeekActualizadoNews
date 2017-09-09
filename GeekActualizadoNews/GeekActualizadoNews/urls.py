from django.conf.urls import include, url
from django.contrib import admin
from News.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'GeekActualizadoNews.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', include('News.urls')),
    #url(r'^json/', include('News.urls')),
    url(r'^$', News),
    url(r'^json/', Newsjson),
]
