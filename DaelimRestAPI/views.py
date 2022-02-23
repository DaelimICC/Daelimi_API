from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import HttpResponse
from .models import Answer, Question
from .serializers import AnswerSerializer, QuestionSerializer
from django.http import JsonResponse


# Test API
# @api_view(['GET'])
# def TestAPI(request):
#     return Response("Ready to Work!")

# Post Implement
class IndexView(View):
    def post(self, request):
        return HttpResponse('Response Clear')
