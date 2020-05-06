from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

# Create your views here.
def time(request):
    context = {
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%H:%M %p", gmtime())
    }
    return render(request, "time.html", context)