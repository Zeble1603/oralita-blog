from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Articulo, Tag


class ArticuloSiteMap(Sitemap):
    
    def items(self):
        return Articulo.objects.all()


class TagSiteMap(Sitemap):
    
    def items(self):
        return Tag.objects.all()


class StaticViewSiteMap(Sitemap):

    i18n=True
    changefreq='monthly'

    def items(self):
        return ['index:home','index:quienes-somos','index:donde','index:primera_visita','index:contact']

    def location(self,item):
        return reverse(item)    
