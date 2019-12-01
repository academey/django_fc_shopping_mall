from django.db import models


class Order(models.Model):
    fcuser = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='사용자')  # 클래스 안의 모델을 지칭
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='제품')  # 클래스 안의 모델을 지칭
    quantity = models.IntegerField(verbose_name='수')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록 날짜')

    class Meta:
        db_table = 'fastcampus_order'
        verbose_name = '주문'
        verbose_name_plural = '주문들'
