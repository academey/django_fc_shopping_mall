from django.views.generic import ListView, FormView, DetailView
from .models import Product
from .forms import RegisterForm
from order.forms import OrderForm
from django.utils.decorators import method_decorator
from fcuser.decorators import admin_required


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'


@method_decorator(admin_required, name='dispatch')
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        product = Product(
            name=form.data.get('name'),
            price=form.data.get('price'),
            description=form.data.get('description'),
            stock=form.data.get('stock')
        )
        product.save()
        return super().form_valid(form)



class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    # 어떤 쿼리에서 찾을지 알려줘야만 한다. 만약 특정 조건이 필요하다면
    # 아래 쿼리에서 all(필터) 를 넣어줘야 한다.
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context
