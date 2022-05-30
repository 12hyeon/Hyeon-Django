from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # /polls 시험지 리스트 페이지
    path('', views.index, name='index'),
    # /polls/1 시험 보기 detail -> test
    path('<int:exam_id>/', views.detail, name='detail'),
     # /polls/1/score/ 시험 체점
    path('<int:exam_id>/score/', views.score, name='score'),
    # /polls/1/result 결과
    path('<int:exam_id>/results/', views.results, name='results'),
    
]