from django.test import TestCase, Client
from katalog.models import CatalogItem
from django.urls import reverse, resolve
from katalog.views import show_catalog

class Testing(TestCase):
    def test_model(self):
        item = CatalogItem.objects.create(
            item_name = "Fitbit Versa 3 [FB511BKBK-FRCJK] - Black",
            item_price = 3699000,
            item_stock = 1,
            description = "SmartTrack yang secara otomatis merekam kegiatan berolahraga Anda",
            rating = 5,
            item_url = "https://www.tokopedia.com/fitbit-official/fitbit-versa-3-fb511bkbk-frcjk-black"
        )
        self.assertEqual(CatalogItem.objects.get(item_name = "Fitbit Versa 3 [FB511BKBK-FRCJK] - Black").item_name, \
            "Fitbit Versa 3 [FB511BKBK-FRCJK] - Black")
        print("Is instance:", isinstance(item, CatalogItem))
        self.assertTrue(isinstance(item, CatalogItem))
    
    def test_url(self):
        url = reverse("katalog:show_catalog")
        print("Resolve:", resolve(url))
        self.assertEquals(resolve(url).func, show_catalog)
    
    def test_view(self):
        client = Client()
        response = client.get(reverse("katalog:show_catalog"))
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "katalog.html")