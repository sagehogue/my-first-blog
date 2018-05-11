from django.shortcuts import render

# Create your views here.
def home(request):
    context_dict = {
        'name': 'Sage',
        'fruit': ['apple', 'banana', 'orange', 'kiwi', 'lychee']
    }
    return render(request, 'aBlog/home.html', context_dict)