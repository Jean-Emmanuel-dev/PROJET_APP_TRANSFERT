from django.db import models
from django.conf import settings

class Notification(models.Model):
    # Lien vers l'utilisateur concerné par la notification
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,      # Suppression des notifications si l'utilisateur est supprimé
        related_name='notifications'   # Accès via user.notifications
    )
    # Titre de la notification
    title = models.CharField(max_length=100)
    # Message détaillé de la notification
    message = models.TextField()
    # Statut de lecture de la notification
    is_read = models.BooleanField(default=False)
    # Date de création de la notification
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # Trie les notifications par date décroissante

    def mark_as_read(self):
        # Marque la notification comme lue
        self.is_read = True
        self.save(update_fields=['is_read'])
