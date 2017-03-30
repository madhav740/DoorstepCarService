from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
#allah hu
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Automobiles.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'homepage.views.home', name='homepage'),
    )
