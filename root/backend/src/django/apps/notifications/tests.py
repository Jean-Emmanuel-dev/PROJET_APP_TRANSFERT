from rest_framework.test import APITestCase
from apps.notifications.models import Notification
from apps.users.models import User
from django.urls import reverse

# Test du ViewSet des notifications
class NotificationViewSetTest(APITestCase):
    def setUp(self):
        # Création d'un utilisateur de test
        self.user = User.objects.create_user(email='notif@example.com', password='pass')
        # Authentification automatique du client de test avec cet utilisateur
        self.client.force_authenticate(user=self.user)
        # Création d'une notification associée à cet utilisateur
        self.notification = Notification.objects.create(
            user=self.user,
            title='Test',
            message='Ceci est une notification'
        )

    def test_notification_list(self):
        # Récupère l'URL de la liste des notifications via le nom de route
        url = reverse('notification-list')
        # Effectue une requête GET sur cette URL
        response = self.client.get(url)
        # Vérifie que la réponse HTTP est 200 (succès)
        self.assertEqual(response.status_code, 200)
        # Vérifie qu'il y a bien une notification retournée
        self.assertEqual(len(response.data), 1)
