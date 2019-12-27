from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import OrderForm
from django.shortcuts import redirect
from .models import Order

class OrderCreate(FormView):
    form_class = OrderForm
    success_url = '/product/'

    def form_invalid(self, form):
        return redirect('/product/' + str(form.product))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })

        return kw


class OrderList(ListView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(fcuser__email=self.request.session.get('user'))
        return queryset
