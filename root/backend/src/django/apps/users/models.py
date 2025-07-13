from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

# Gestionnaire personnalisé pour le modèle User
class UserManager(BaseUserManager):
    # Méthode pour créer un utilisateur standard
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L’email est requis")  # Vérifie que l'email est fourni
        email = self.normalize_email(email)  # Normalise l'email (ex: minuscule)
        user = self.model(email=email, **extra_fields)  # Crée une instance User
        user.set_password(password)  # Hash le mot de passe
        user.save(using=self._db)  # Sauvegarde dans la base de données
        return user

    # Méthode pour créer un superutilisateur (admin)
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)  # Doit avoir les droits staff
        extra_fields.setdefault('is_superuser', True)  # Doit être superuser
        return self.create_user(email, password, **extra_fields)

# Modèle utilisateur personnalisé
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)  # Email unique pour chaque utilisateur
    username = models.CharField(max_length=30, blank=True)  # Nom d'utilisateur optionnel
    phone_number = models.CharField(max_length=15, unique=True)  # Numéro de téléphone unique
    is_verified = models.BooleanField(default=False)  # Statut de vérification
    is_staff = models.BooleanField(default=False)  # Peut accéder à l'admin Django
    date_joined = models.DateTimeField(auto_now_add=True)  # Date d'inscription

    objects = UserManager()  # Utilise le gestionnaire personnalisé

    USERNAME_FIELD = 'email'  # Champ utilisé pour l'authentification
    REQUIRED_FIELDS = []  # Champs requis lors de la création via createsuperuser

    class Meta:
        ordering = ['-date_joined']  # Trie les utilisateurs par date d'inscription décroissante

    def __str__(self):
        return self.email  # Représentation en chaîne de l'utilisateur
