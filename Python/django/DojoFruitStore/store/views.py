from django.shortcuts import render, HttpResponse, redirect
import datetime

# Create your views here.
def storefront(request):
    return render(request, "store.html")

def submit(request):
    print("Test", request.POST)
    request.session['raspberry'] = request.POST['raspberry']
    request.session['strawberry'] = request.POST['strawberry']
    request.session['apple'] = request.POST['apple']
    request.session['name'] = request.POST['name']
    request.session['id'] = request.POST['id']

    totalItems = int(request.POST['raspberry']) + int(request.POST['strawberry']) + int(request.POST['apple'])
    request.session['numItems'] = totalItems
    date = datetime.datetime.now()
    request.session['date'] = date.strftime("%B %d %Y %I:%M:%S %p")
    return redirect("/checkout")

def checkout(request):
    print(f"Charging {request.session['name']} for {request.session['numItems']} fruits")
    return render(request, "checkout.html")