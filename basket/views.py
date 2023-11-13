from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Watch


def view_basket(request):
    """
    This view renders the shopping basket page
    """
    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    watch = get_object_or_404(Watch, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f"Updated {watch.brand} {watch.model} quantity in your basket.")
    else:
        basket[item_id] = quantity
        messages.success(request, f"Added {watch.brand} {watch.model} to your basket.") 

    request.session['basket'] = basket
    return redirect(redirect_url)

def adjust_basket(request, item_id):
    """ Adjust the quantity of the specified product to the shopping basket """
    watch = get_object_or_404(Watch, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f"Updated {watch.brand} {watch.model} quantity in your basket.")
        
    else:
        basket.pop(item_id)
        messages.success(request, f"Removed {watch.brand} {watch.model} from your basket.")

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))

def remove_from_basket(request, item_id):
    """ Remove the specified product from the shopping basket """
    watch = get_object_or_404(Watch, pk=item_id)
    
    try:
        basket = request.session.get('basket', {})
        basket.pop(item_id)
        messages.success(request, f"Removed {watch.brand} {watch.model} from your basket.")

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing {watch.brand} {watch.model} from your basket.")
        return HttpResponse(status=500)