from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

class Advert(models.Model):
    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
    
    name = models.CharField(max_length=100, verbose_name='название')
    pub_date = models.DateField(auto_now_add=True, verbose_name='дата публикации')
    author = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name='автор', blank = True, null=True)
    text = models.TextField(verbose_name='описание')
    price = models.IntegerField(verbose_name='стоимость')
    photo = models.ImageField(upload_to='images', verbose_name='изображение')


    def __str__(self):
        return f'{self.name}'
