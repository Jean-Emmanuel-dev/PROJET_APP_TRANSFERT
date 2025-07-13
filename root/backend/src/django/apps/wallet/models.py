from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Wallet(models.Model):
    # Lien unique avec l'utilisateur (un wallet par utilisateur)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,  # Suppression du wallet si l'utilisateur est supprimé
        related_name='wallet'      # Permet d'accéder au wallet via user.wallet
    )
    # Solde du portefeuille, avec 2 décimales
    balance = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00
    )
    # Date de la dernière mise à jour du portefeuille
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Portefeuille"              # Nom dans l'admin Django
        verbose_name_plural = "Portefeuilles"      # Pluriel dans l'admin

    def __str__(self):
        # Affichage lisible du wallet dans l'admin ou le shell
        return f"Wallet of {self.user.email}"

    def deposit(self, amount):
        # Ajoute un montant au solde
        self.balance += amount
        self.save(update_fields=['balance'])  # Sauvegarde uniquement le champ balance
        return self.balance

    def withdraw(self, amount):
        # Retire un montant du solde si suffisant, sinon lève une erreur
        if amount > self.balance:
            raise ValueError("Solde insuffisant")
        self.balance -= amount
        self.save(update_fields=['balance'])
        return self.balance

# Signal : création automatique d'un wallet après la création d'un utilisateur
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)
