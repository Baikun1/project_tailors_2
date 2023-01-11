from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    # return HttpResponse("This is Home page & Iam baikuntah behara")
    return render(request, 'home.html')
def index(request):
    # return HttpResponse("This is Home page & Iam baikuntah behara")
    return render(request, 'index.html')
def about(request):
    # return HttpResponse("This is about page")
    return render(request, 'about.html')
def blog(request):
    # return HttpResponse("This is blog page")
    return render(request, 'blog.html')
def contact(request):
    # return HttpResponse("This is contact page")
    return render(request, 'contact.html')