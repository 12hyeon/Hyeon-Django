from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from .models import Question, Choice, Exam
stu_num = 0
q_num = 0
def index(request):
    latest_exam_list = Exam.objects.order_by('-pub_date')[:5]
    context = {'latest_exam_list': latest_exam_list}
    return render(request, 'polls/index.html', context)


def detail(request, exam_id):
    try:
        exam = Exam.objects.get(pk=exam_id)
        q_list = Question.objects.filter(exam_id=exam.id)
        context = {'exam': exam, 'q_list': q_list}
        global stu_num, q_num # 학번 담을 변수
        stu_num = 3220
        q_num = 0 # 문제 번호의 시작
    except Exam.DoesNotExist:
        raise Http404("Exam does not exist")
    return render(request, 'polls/detail.html', context)


def store(request, exam_id): # 기존에 학생마다 각 문제에 대한 답안지를 만듬
    exam = Exam.objects.get(pk=exam_id)
    q_list =  Question.objects.filter(exam_id=exam.id)
    quest = q_list[q_num]
    solution = quest.filter(num=1) # 해당 문제의 정답

    # 학번 저장 
    if (q_num == 0 and request.POST['choice'][0:4] == "3220"):
        stu_num = int(request.POST['choice'])
        # 학생의 답안지 또한 1번부터 순차적으로 만들 때
    
    # 학생의 답안을
    s = Choice.objects.filter(num = stu_num).filter(question = quest)
    # 해당 학생에게 해당 답안지가 주어진 경우만 저장 가능
    if len(s) == 1:
        if s.question == quest:
            s.choice_text = request.POST['choice']
    
    if request.POST['choice'].strip() == solution.strip() :
        s.correct = 'O'
    else:
        s.correct = 'X'
    s.save()
    q_num += 1
    

def score(request, exam_id): # 학생마다 각자의 맞는지 여부 출력
    exam = Exam.objects.get(pk=exam_id)
    stu_answer = Choice.objects.filter(num = stu_num)
    s_score = 0
    s_total = 0
    for s in stu_answer:
        if s.correct == 'O':
            score += 1
        s_total += 1
    context = {'exam': exam, 'stu_num': stu_num, 'answer': stu_answer, 'score': s_score, 'total': s_total}
    return render(request, 'polls/score.html', context)


def results(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)
    s = Choice.objects.filter() # 1개 시험지마다 학생 수
    context = {'exam': exam, 's':s}
    return render(request, 'polls/results.html', context)


