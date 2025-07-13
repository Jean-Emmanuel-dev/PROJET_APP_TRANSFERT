from django.db import models
from django.conf import settings
from decimal import Decimal

class Transaction(models.Model):
    # Types de transaction possibles
    CREDIT = 'credit'
    DEBIT = 'debit'
    TYPE_CHOICES = [
        (CREDIT, 'Credit'),  # Crédit (ajout d'argent)
        (DEBIT, 'Debit'),    # Débit (retrait d'argent)
    ]

    # Référence au portefeuille concerné
    wallet = models.ForeignKey(
        'wallet.Wallet',
        on_delete=models.CASCADE,      # Suppression des transactions si le wallet est supprimé
        related_name='transactions'    # Accès via wallet.transactions
    )
    # Montant de la transaction
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    # Type de transaction (crédit ou débit)
    tx_type = models.CharField(max_length=6, choices=TYPE_CHOICES)
    # Date de création de la transaction
    created_at = models.DateTimeField(auto_now_add=True)
    # Description optionnelle de la transaction
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']  # Trie les transactions par date décroissante
        indexes = [
            models.Index(fields=['wallet', 'created_at']),  # Index pour optimiser les requêtes
        ]

    def save(self, *args, **kwargs):
        # Mise à jour automatique du wallet lors de la sauvegarde d'une transaction
        super().save(*args, **kwargs)
        if self.tx_type == self.CREDIT:
            self.wallet.deposit(self.amount)   # Ajoute le montant au wallet
        else:
            self.wallet.withdraw(self.amount)  # Retire le montant du wallet

    def __str__(self):
        # Affichage lisible de la transaction
        return f"{self.tx_type.title()} {self.amount} on {self.created_at}"
