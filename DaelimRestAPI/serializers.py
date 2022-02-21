from rest_framework import serializers
from .models import Answer


# Test Serializer
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer')
