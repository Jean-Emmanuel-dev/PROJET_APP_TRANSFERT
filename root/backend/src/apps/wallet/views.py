from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Wallet
from .serializers import WalletSerializer
from core.permissions import IsOwner


class WalletViewSet(viewsets.ModelViewSet):
    """
    Gérer les portefeuilles : liste, détails, création, mise à jour, suppression
    """
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get_queryset(self):
    # Ne renvoie que le portefeuille de l'utilisateur connecté
        return Wallet.objects.filter(user=self.request.user)


