from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True, null=True , verbose_name='Аватар')
    
    
    class Meta:
        db_table = 'user'
        verbose_name = 'Пользувателя'
        verbose_name_plural = 'Пользователи'
    
    
    def __str__(seft):
        return seft.username
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    