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
        question_serializer = QuestionSerializer(data=request.POST)
        # print(question_serializer.data['message'])
        if question_serializer.is_valid():
            question_serializer.save()

            print(question_serializer.data['message'])


            response_data = {
                'answer': question_serializer.data['message']
            }


            # return HttpResponse(question_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(response_data)
        else:
            return HttpResponse(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
