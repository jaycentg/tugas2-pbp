from django.shortcuts import render
from katalog.models import CatalogItem

data_catalog_item = CatalogItem.objects.all()
context = {
    'list_item': data_catalog_item,
    'nama': 'Jaycent Gunawan Ongris',
    'npm': '2106750231'
}

def show_catalog(request):
    return render(request, "katalog.html", context)