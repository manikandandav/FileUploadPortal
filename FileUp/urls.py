from django.conf.urls import patterns, include, url
from FileUp.views import login, home, register, logout

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url ( r'^$',login),
    url ( r'^login/$',login),
    url ( r'^home/$', home),
    url ( r'^register/$', register),
    url ( r'^logout/$', logout),
    # url(r'^admin/', include(admin.site.urls)),
)
