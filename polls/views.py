from django.db.models import F
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

from .forms import TestForm


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "polls/index.html", context)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "polls/detail.html", {"question": question})

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    
# testing a form
# def show_test_form(request):
#     return render(request, "polls/test_form.html")

def test_form(request):
    print("request = ", request)
    
    if request.htmx:
        print("HTMX TRUE request = ", request)

    if request.method == "POST":
        print("request.POST = ", request.POST)

        test_form = TestForm(request.POST)
        # print("test form = ", test_form.cleaned_data) # prints whole html of <form> tag
        # prints <input type="email" name="email" value="d@c.com" maxlength="100" required id="id_email">
        # print("test form email = ", test_form["email"]) 
        
        if test_form.is_valid():
            # return HttpResponseRedirect("/thanks/")
            print("test form = ", test_form.cleaned_data) 
            return HttpResponse("Thanks!")
    
    else:
        test_form = TestForm()
        print("empty test form")
        # print("empty test form data = ", test_form) # prints whole <form> tag!
    
    return render(request, "polls/test_form.html", {"test_form": test_form})

    #return HttpResponse("You're looking at the results of the test form.")