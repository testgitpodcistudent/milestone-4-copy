from django.shortcuts import redirect, render, reverse, HttpResponse


# Create your views here.
def view_cart(request):
    """ return cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ add 1 of the specified product to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ adjust quantity of specified product in cart to a specified amount from cart.html """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] = quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(reverse("view_cart"))


def remove(request, item_id):
    """ remove all of specified item from the cart """
    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)