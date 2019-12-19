from django.views.generic.edit import FormView
from .forms import OrderForm

class OrderCreate(FormView):
    form_class = OrderForm
    success_url = '/product/'
