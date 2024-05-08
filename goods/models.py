from django.db import models
from django.urls import reverse

# Create your models here.
class Catagories(models.Model):
    name = models.CharField(max_length=50 , unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200 , unique=True , blank=True , null=True , verbose_name='URL')
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Катигории'
    
    
    def __str__(seft):
        return seft.name    
        
        
class Products(models.Model):
    name = models.CharField(max_length=50 , unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200 , unique=True , blank=True , null=True , verbose_name='URL')
    image = models.ImageField(upload_to='goods_image', blank=True , null=True,verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.DecimalField(default=0.00, max_digits=7 , decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4 , decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0 , verbose_name='Количиство')
    category = models.ForeignKey(to=Catagories, on_delete=models.CASCADE, verbose_name='Категория')
    
    class Meta:
         db_table = 'product'
         verbose_name = 'Продукт'
         verbose_name_plural = 'Продукты'
         ordering = ("id",)
         
    def __str__(seft):
        return f'{seft.name} Количиство '
    
    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})
    
        
    def display_id(self):
        return f'{self.id:05}'
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        
        return self.price    
               
         
    
                