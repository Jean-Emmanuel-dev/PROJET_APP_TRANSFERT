from rest_framework.test import APITestCase
from django.urls import reverse
from apps.users.models import User

class UserViewSetTest(APITestCase):
    def setUp(self):
        # Création d'un utilisateur de test
        self.user = User.objects.create_user(
            email='test@example.com',
            password='securepass',
            phone_number='0101010101'
        )
        # Authentification automatique du client de test avec cet utilisateur
        self.client.force_authenticate(user=self.user)

    def test_user_list(self):
        # Récupère l'URL de la liste des utilisateurs via le nom de route
        url = reverse('user-list')  # dépend du nom dans le router
        # Effectue une requête GET sur cette URL
        response = self.client.get(url)
        # Vérifie que la réponse HTTP est 200 (succès)
        self.assertEqual(response.status_code, 200)
        # Vérifie que le champ 'email' est présent dans la première entrée retournée
        self.assertIn('email', response.data[0])
