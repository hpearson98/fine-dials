from django.shortcuts import render


def view_basket(request):
    """
    This view renders the shopping basket page
    """
    return render(request, 'basket/basket.html')
