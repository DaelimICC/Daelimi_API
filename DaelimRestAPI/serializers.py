from rest_framework import serializers
from .models import Question


# Request Serializer
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('message', 'isFilter')

