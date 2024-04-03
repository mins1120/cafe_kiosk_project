from django.shortcuts import render
from .models import Question, Choice

# 모든 음료 종류를 보여주는 뷰
def index(request):
    drink_list = Question.objects.all()
    context = {'drink_list': drink_list}
    return render(request, 'cafe_kiosk_app/index.html', context)

# 세부 음료 종류를 보여주는 뷰
def detail(request, question_id):
    drink = Question.objects.get(pk=question_id)
    choices = drink.choices.all()
    context = {'drink': drink, 'choices': choices}
    return render(request, 'cafe_kiosk_app/detail.html', context)
