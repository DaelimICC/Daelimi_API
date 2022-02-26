from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import HttpResponse
from .models import Question
from .serializers import QuestionSerializer
from django.http import JsonResponse

from .Location_Filter import Location


# Post Implement
class IndexView(View):
    global loc
    loc = Location()

    def post(self, request):
        question_serializer = QuestionSerializer(data=request.POST)
        if question_serializer.is_valid():
            requestData = question_serializer.data

            if requestData['isFilter'] == 1:
                tempQuestion = requestData['message'].split()
                locationWord = tempQuestion[0][0:len(tempQuestion[0])-1]
                answerData = str(tempQuestion[0]) + ' ' + loc.classroomfinder(locationWord) + '에 있습니다!'
            # Answer Json (Dictionary)
            response_data = {
                'answer': answerData
            }

            return JsonResponse(response_data)
        else:
            return HttpResponse(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
