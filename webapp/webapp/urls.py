from django.conf.urls import patterns, include, url
from views import HomeView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'webapp.views.home', name='home'),
    url(r'^$', HomeView.as_view()),
    url(r'^create_license/', 'webapp.views.create_license', name='create_license'),
    url(r'^admin/', include(admin.site.urls)),
)
