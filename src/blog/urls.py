from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    url(r'^article/(?P<slug>.+)$', 'blog.views.read', {}, 'read'),
    url(r'^categorie/(?P<nom>.+)$', 'blog.views.categorie'),
    url(r'^recherche$', 'blog.views.search'),
    url(r'^contact$', 'blog.views.contact'),
    url(r'^(?P<page>.+)$', 'blog.views.home'),
    url(r'^$', 'blog.views.home'),
    ) + static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
