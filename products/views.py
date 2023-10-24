from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Watch


def all_watches(request):
    """
    This view shows all products including sorting and search queries
    """
    watches = Watch.objects.all()
    context = {
        'watches': watches,
    }
    return render(request, 'watches/watches.html', context)
