from django.shortcuts import render, HttpResponse
from .forms import QuestionForm
from .models import Question


def question_form_view(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form-succes.html')

        else:
            return HttpResponse("Form is invalid")
    form = {'form': QuestionForm}
    return render(request, 'question-form.html', form)


def question_list_view(request):
    question = Question.objects.all()
    ctx = {'questions': question}
    return render(request, 'question-list.html', ctx)
