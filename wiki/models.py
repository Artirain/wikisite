from unicodedata import category
from django.db import models
from django.urls import reverse

# Create your models here.


#таблица
class Wiki(models.Model):
    title = models.CharField(max_length = 150, verbose_name='Наименование')  #CharField - строковое поле, для строк малого и большого размера
    #TextField - для больших объемов текста. Синтаксис CharField(max_length = )
    content = models.TextField(blank = True, verbose_name='Контент') #blank = True - необязательное заполнение
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации') #создаем дату и время единожды
    updated_at = models.DateTimeField(auto_now = True, verbose_name='Обновлено') #при сохранении записи будут заполняться автоматически
    photo = models.ImageField(upload_to = 'photos/%Y%m%d/', verbose_name='Фото', blank=True) # ImageField хранит только  фото, путь #FileField хранит любой файл
    #upload_to - загружаем в photos/ и разбиваем по дате их загрузки
    is_published = models.BooleanField(default = True, verbose_name='Опубликовано да/нет') #Поле истина/ложь
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория') #ForeignKey настраивает связь с главной сущностью.
    #Первый параметр указывает, с какой моделью будет создаваться связь - в данном случае это модель Company. 
    # Второй параметр - on_delete задает опцию удаления объекта текущей модели при удалении связанного объекта главной модели. 
    #null - true, по умолчарию false, но мы не хотим заполнять

    def get_absolute_url(self): 
        return reverse('view_wiki', kwargs={'pk':self.pk}) 

    def __str__(self):  #функция для того, чтобы получить str
        return self.title #вводим любое значение с таблицы, чтобы получить в формате str

    class Meta:  #с помощью этого класса теперь новости будут показываться в обратном порядке
        verbose_name = 'Новость'  #verbose_name атрибут - название в ед.ч
        verbose_name_plural = 'Новости' #во множественном числе
        ordering = ['-created_at'] #атрибут ordering - сортирует по created_at

class Category(models.Model):

    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории') #db_index - индексирует поле, делает более быстрым для поиска

    def get_absolute_url(self): #при названии метода так, джанго исп. этот метод по умолчанию(дает смотреть в админке сайт)
        return reverse('category', kwargs={'category_id':self.pk}) #1-ый параметр - название маршрута, 2-ой - необходимый параметр для построения маршрута


    def __str__(self): #получает стринг, ранее было : ... object(1)
        return self.title

    class Meta:  #с помощью этого класса теперь новости будут показываться в обратном порядке
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']