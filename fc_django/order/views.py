from django.views.generic.edit import FormView
from .forms import OrderForm
from django.shortcuts import redirect


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
