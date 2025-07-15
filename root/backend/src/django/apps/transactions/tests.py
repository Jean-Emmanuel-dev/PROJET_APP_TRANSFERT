from rest_framework.test import APITestCase
from apps.transactions.models import Transaction
from apps.users.models import User
from django.urls import reverse

class TransactionViewSetTest(APITestCase):
    def setUp(self):
        # Création d'un utilisateur de test
        self.user = User.objects.create_user(email='tx@example.com', password='pass')
        # Authentification automatique du client de test avec cet utilisateur
        self.client.force_authenticate(user=self.user)

    def test_create_credit_transaction(self):
        # Récupère l'URL de la liste/création des transactions via le nom de route
        url = reverse('transaction-list')
        # Prépare les données pour une transaction de crédit
        data = {
            'wallet': self.user.wallet.id,
            'amount': 100,
            'tx_type': 'credit',
            'description': 'Recharge test'
        }
        # Effectue une requête POST pour créer la transaction
        response = self.client.post(url, data)
        # Vérifie que la réponse HTTP est 201 (création réussie)
        self.assertEqual(response.status_code, 201)
        # Rafraîchit le wallet depuis la base de données
        self.user.wallet.refresh_from_db()
        # Vérifie que le solde du wallet a bien été mis à jour
        self.assertEqual(float(self.user.wallet.balance), 100.00)
