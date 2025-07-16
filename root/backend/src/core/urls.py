from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import des vues API
from users.views import UserViewSet
from wallet.views import WalletViewSet
from transactions.views import TransactionViewSet
from notifications.views import NotificationViewSet

# JWT views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Initialisation du routeur
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'wallets', WalletViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Swagger pour les tests
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
  openapi.Info(
    title="API FinTech",
    default_version='v1',
    description="Documentation interactive de l'API",
  ),
  public=True,
  authentication_classes=(JWTAuthentication,),
  permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]


# Ajout de la vue pour obtenir les informations de l'utilisateur connecté
from users.views import MeView

urlpatterns += [
    path('api/me/', MeView.as_view(), name='me'),
]

