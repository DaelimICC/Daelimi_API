from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from issue.models import Issue

def upload_Issue(request):
    """
    이슈 내용 저장 및 내용 및 제목 없을시 예외처리
    """
    if request.method == 'GET':
        return render(request, 'issue.html')
    elif request.method == 'POST':
        subject = request.POST.get('issueTitle',None)
        content = request.POST.get('issueContents',None)
        issue = Issue(
            subject = subject,
            content = content
        )
        issue.save()
        return render(request,'issue.html')




