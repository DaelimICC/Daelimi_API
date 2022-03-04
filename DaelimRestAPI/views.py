from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import HttpResponse
from .models import Question
from .serializers import QuestionSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import re

from .Location_Filter import Location
from .Facility import Facility


# Post Implement
class IndexView(APIView):
    global loc, fac
    loc = Location()
    fac = Facility()

    @method_decorator(csrf_exempt)
    def post(self, request):
        tempdata = JSONParser().parse(request)
        question_serializer = QuestionSerializer(data=tempdata)
        if question_serializer.is_valid():
            requestData = question_serializer.data

            if requestData['isFilter'] == 1:
                kor_reg = re.compile(r'[ㄱ-ㅣ가-힣]+')

                tempQuestion = requestData['message'].split()
                locationWord = tempQuestion[0][0:len(tempQuestion[0]) - 1]

                # True : 주요 시설물 답변, False : 강의실 코드 답변
                if kor_reg.match(locationWord):
                    if fac.checkVailed(locationWord):
                        answerData = locationWord + '는 ' + fac.FindLocation(locationWord) + '에 있습니다!'
                    else:
                        answerData = '거기는 어디인가요...? 잘 모르겠어요ㅠㅠ'
                else:
                    if loc.classroomfinder(locationWord) != "찾을 수 없는 강의실 코드":
                        answerData = str(tempQuestion[0]) + ' ' + loc.classroomfinder(locationWord) + '에 있습니다!'
                    else:
                        answerData = str(tempQuestion[0]) + ' 어디에 있는지 저도 모르겠네요... 올바른 강의실 코드인가요?'
            # isFilter == 0
            elif requestData['isFilter'] == 0:
                answerData = '아직 구현이 되지 않았습니다! 조금만 더 기다려주세요 :D'
            elif requestData['isFilter'] == 404:
                answerData = 'isOK'
            else:
                answerData = 'Exception'
            # Answer Json (Dictionary)
            response_data = {
                'answer': answerData
            }

            return JsonResponse(response_data)

        else:
            return HttpResponse(question_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
