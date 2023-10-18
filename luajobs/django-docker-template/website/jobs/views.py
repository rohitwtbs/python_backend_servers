from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .forms import JobForm
# Create your views here.


def index(request):
    # print(request)
    return HttpResponse('this is the first job opening')




def showForm(request):

    if request.method == 'POST':
        form = JobForm(request.POST)

        if form.is_valid():

            return HttpResponseRedirect("/thanks/")
    else:
        form = JobForm()
    pass

    return render(request, "job_input.html", {"form": form})


