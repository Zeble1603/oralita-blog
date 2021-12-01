from django.contrib.sitemaps import Sitemap
from blog.models import Articulo, Tag

class ArticuloSiteMap(Sitemap):
    
    def items(self):
        return Articulo.objects.all()

class TagSiteMap(Sitemap):
    
    def items(self):
        return Tag.objects.all()

