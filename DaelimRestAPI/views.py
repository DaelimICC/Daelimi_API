from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Answer
from .serializers import AnswerSerializer

# Test API
@api_view(['GET'])
def TestAPI(request):
    return Response("Ready to Work!")