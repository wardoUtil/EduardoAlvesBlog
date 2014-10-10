from django.conf.urls import patterns, include, url
from Entrepreneur.views import *
from django.conf.urls.static import static
from Entrepreneur_Project import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^post/(?P<post_url>\S+)', render_post, name='view_post'),
    url(r'^create_comment', create_comment, name='create_comment'),
    url(r'^', render_homepage, name='index')


)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
