from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Produto

class ProdutoAPITest(APITestCase):
    def setUp(self):
        self.url = reverse("produto-list")
        Produto.objects.create(nome="Teste", preco="9.99")

    def test_list_produtos(self):
        res = self.client.get(self.url)
        self.assertEqual(res.status_code, 200)
        self.assertGreaterEqual(len(res.data), 1)
