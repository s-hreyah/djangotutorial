from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.template import loader

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    queryset=Question.objects.order_by('-pub_date')

# def index(request):
#     # latest_question_list = Question.objects.order_by("-pub_date")
#     # output=",".join( question.question_text for question in latest_question_list)
#     # return HttpResponse(output)
#     latest_question_list=Question.objects.order_by("-pub_date")
#     # print(latest_question_list)
#     # template=loader.get_template("polls/index.html")
#     # context={"latest_question_list":latest_question_list}
#     # return HttpResponse(template.render(context,request))
#     return render(request,'polls/index.html',{"latest_question_list":latest_question_list})



class DetailView(generic.DetailView):
    model= Question
    template_name = 'polls/detail.html'


# def detail(request, question_id):
    # output=f"you are looking at question : {question_id}"
    # return HttpResponse(output)

    #     try:
    #         question = Question.objects.get(pk=question_id)
    #     except Question.DoesNotExist:
    #         raise Http404("Question does not exist")
    #     return render(request, "polls/detail.html", {"question": question})
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, "polls/detail.html", {"question": question})


class ResultsView(generic.DetailView):
    model= Question
    template_name = 'polls/results.html'


# def results(request,question_id):
#     # output=f"you are looking at Result  : {question_id}"
#     # return HttpResponse(output)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question":question})

def vote(request,question_id) :

    question = get_object_or_404(Question, pk=question_id)
    choice_id =request.POST.get("choice")
    selected_choice = question.choice_set.get(pk=choice_id)
    selected_choice.votes=F("votes") +1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))