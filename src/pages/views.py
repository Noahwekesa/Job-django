from django.shortcuts import render

# Create your views here.
def home_page(request):

    context = {'key': 'value'} 
    return render(request, "index.html", context)