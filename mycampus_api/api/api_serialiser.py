from rest_framework import serializers
from .models import Actu

class ActuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actu
        fields = '__all__'
        # ou explicitement : fields = ['id', 'titre', 'contenu', 'image']
