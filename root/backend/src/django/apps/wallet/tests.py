from rest_framework.test import APITestCase
from apps.wallet.models import Wallet
from apps.users.models import User
from django.urls import reverse

class WalletViewSetTest(APITestCase):
    def setUp(self):
        # Création d'un utilisateur de test
        self.user = User.objects.create_user(email='wallet@example.com', password='pass')
        # Authentification automatique du client de test avec cet utilisateur
        self.client.force_authenticate(user=self.user)

    def test_wallet_created_on_user_creation(self):
        # Vérifie que le wallet est bien créé automatiquement lors de la création de l'utilisateur
        self.assertTrue(hasattr(self.user, 'wallet'))
        # Vérifie que le solde initial du wallet est bien à 0
        self.assertEqual(self.user.wallet.balance, 0)

    def test_wallet_detail(self):
        # Récupère l'URL du détail du wallet via le nom de route
        url = reverse('wallet-detail', args=[self.user.wallet.id])
        # Effectue une requête GET sur cette URL
        response = self.client.get(url)
        # Vérifie que la réponse HTTP est 200 (succès)
        self.assertEqual(response.status_code, 200)
        # Vérifie que le solde retourné est bien '0.00' (format string)
        self.assertEqual(response.data['balance'], '0.00')
