from django import forms
from .models import Order
from product.models import Product
from fcuser.models import Fcuser

class OrderForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    # 여기서 fcuser와 를 받을 필요가 없다. 세션에 들고 있는 값이 있을 것이므로 그걸 쓰면 되니까!
    # 대신, product 는 HiddenInput 으로 받아줘야 한다.
    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요'
        },
        label='수량'
    )
    product = forms.IntegerField(
        error_messages={
            'required': '상품을 입 력해주세요'
        },
        label='상품', widget=forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        fcuser_email = self.request.session.get('user')

        if quantity and product and fcuser_email:
            order = Order(
                quantity=quantity,
                product=Product.objects.get(pk=product),
                fcuser=Fcuser.objects.get(email=fcuser_email)
            )
            order.save()
        else:
            self.product = product
            self.add_error('quantity', '값이 없습니다')
            self.add_error('product', '값이 없습니다')
        # name = cleaned_data.get('name')
        # price = cleaned_data.get('price')
        # description = cleaned_data.get('description')
        # stock = cleaned_data.get('stock')
        #
        # if name and price and description and stock:
        #     product = Product(
        #         name=name,
        #         price=price,
        #         description=description,
        #         stock=stock
        #     )
        #     product.save()
