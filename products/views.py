from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Watch, Brand
from .forms import ProductForm


def all_watches(request):
    """
    This view shows all watches including sorting and search queries
    """
    watches = Watch.objects.all()
    query = None
    brands = None
    sort = None
    direction = None

    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'model':
            sortkey = 'lower_model'
            watches = watches.annotate(lower_model=Lower('model'))

        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
            
            watches = watches.order_by(sortkey)
    if 'brand' in request.GET:
        brands = request.GET['brand'].split(',')
        watches = watches.filter(brand__name__in=brands)
        brands = Brand.objects.filter(name__in=brands)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'watches': watches,
        'search_term': query,
        'current_brands': brands,
        'current_sorting': current_sorting,
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

@login_required
def add_watch(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_watch'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'watches/add_watch.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_watch(request, watch_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    watch = get_object_or_404(Watch, pk=watch_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=watch)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('watch_detail', args=[watch.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=watch)
        messages.info(request, f'You are editing {watch.brand} {watch.model}')

    template = 'watches/edit_watch.html'
    context = {
        'form': form,
        'watch': watch,
    }

    return render(request, template, context)

@login_required
def delete_watch(request, watch_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    watch = get_object_or_404(Watch, pk=watch_id)
    watch.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('watches'))