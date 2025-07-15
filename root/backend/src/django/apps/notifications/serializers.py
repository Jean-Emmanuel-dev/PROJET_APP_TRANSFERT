from rest_framework import serializers
from .models import Notification

# Sérialiseur pour le modèle Notification
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification  # Modèle associé au sérialiseur
        # Champs à inclure dans la représentation JSON
        fields = ['id', 'title', 'message', 'is_read', 'created_at']
