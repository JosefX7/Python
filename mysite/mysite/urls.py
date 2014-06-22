from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from lucy import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^lucy/', include('lucy.urls')),
    url(r'^admin/', include(admin.site.urls)),
   

    url(r'^sample_graph/', views.graph, name = "graph")
)
