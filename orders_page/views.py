from django.http import Http404
from django.shortcuts import render, redirect
from .models import Order
from django.views import View
from .forms import OrderForm

def orders(request):
    order_list = Order.objects.order_by("order_number")
    context = {
        "order_list": order_list,
    }
    return render(request, 'orders_page/orders.html', context)

def detail(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        raise Http404("Order does not exist!")
    return render(request, "orders_page/detail.html", {"order": order})


class NewOrder(View):
    def get(self, request):
        order_form = OrderForm()
        return render(request, "orders_page/neworder.html", {"order_form": order_form})

    def post(self, request):
        order_form = OrderForm(request.POST, request.FILES)
        if order_form.is_valid():
            order_form.save()
            return redirect("orders_page:new_order")
