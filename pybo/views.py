from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):

    question_list = Question.objects.order_by('-create_date') #질문목록 데이터 + 작성일시 순으로 결과 정렬
    context = {'question_list' : question_list}

    return render(request, 'pybo/question_list.html', context)
    #render : 조회된 질문목록 데이터를 pybo/question_list.html 파일에 적용하여
    #HTML로 변환해주는 함수


# Create your views here.


