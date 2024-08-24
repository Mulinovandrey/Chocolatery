from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name = 'Название')
    price = models.IntegerField(blank=True, verbose_name = 'Цена') #blank=True - обозначает поле необязательное к заполнению
    price_with_sale = models.FloatField(blank=True, verbose_name = 'Цена со скидкой')
    content = models.TextField(blank=True, verbose_name = 'Описание')
    is_available = models.BooleanField(default=True, verbose_name = 'Наличие')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name = 'Фото', blank=True) # сохранение по дате при загрузке %Y/%m/%d/
    weight = models.IntegerField(blank=True, verbose_name = 'Масса')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')


    def get_absolute_url(self):
        return reverse('view_product', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title']



class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
