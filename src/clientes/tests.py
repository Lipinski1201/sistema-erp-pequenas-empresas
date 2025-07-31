from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Cliente

class ClienteAPITests(APITestCase):
    def setUp(self):
        self.url = reverse("cliente-list")
        Cliente.objects.create(nome="Teste", email="t@x.com")

    def test_list_clients(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
