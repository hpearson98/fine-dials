from django.shortcuts import render


def index(request):
    """
    This view renders the index page
    """
    return render(request, 'home/index.html')
