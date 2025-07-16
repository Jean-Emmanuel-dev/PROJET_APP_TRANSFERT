from django.db import models
from wallet.models import Wallet

class Transaction(models.Model):
    TX_TYPES = (('credit', 'Crédit'), ('debit', 'Débit'))

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    tx_type = models.CharField(max_length=10, choices=TX_TYPES)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.tx_type == 'credit':
            self.wallet.deposit(self.amount)
        else:
            self.wallet.withdraw(self.amount)
        super().save(*args, **kwargs)
