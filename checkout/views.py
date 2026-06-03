from django.contrib import messages
from django.shortcuts import redirect, render, reverse
from .forms import OrderForm


# Create your views here.
def checkout(request):
    bag = request.session.get("bag", {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse("products"))

    order_form = OrderForm()
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": "pk_test_51TdyJ3KOk1eNwg7UUq1G0N5BTr0OaQcl4bHh8PVPg8PreurMWDVLyay7OD2aQknOok91xAs07MndJ5KfcXX73jtb00DMlF94zJ",
        "client_secret": "test_client_secret",
    }

    return render(request, template, context)
