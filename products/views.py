from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
from .models import Watch


def all_watches(request):
    """
    This view shows all watches including sorting and search queries
    """
    watches = Watch.objects.all()
    context = {
        'watches': watches,
    }
    return render(request, 'watches/watches.html', context)


def watch_detail(request, watch_id):
    """
    This view shows the details of the selected watch
    """
    watch = get_object_or_404(Watch, pk=watch_id)
    context = {
        'watch': watch,
    }
    return render(request, 'watches/watch_detail.html', context)
