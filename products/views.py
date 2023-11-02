from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.contrib import messages

from .models import Watch


def all_watches(request):
    """
    This view shows all watches including sorting and search queries
    """
    watches = Watch.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse('watches'))

            queries = Q(
                brand__name__icontains=query
            ) | Q(
                description__icontains=query
            )

            watches = watches.filter(queries)

    context = {
        'watches': watches,
        'search_term': query,
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
