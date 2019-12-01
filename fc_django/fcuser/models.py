from django.db import models


class Fcuser(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='등록 날짜')

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '유저'
        verbose_name_plural = '유저들'
