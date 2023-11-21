from django.db import models

class FilmModel(models.Model):
    GENRE = (
        ('Horror', 'Horror'),
        ('Dramma', 'Dramma')
    )
    title = models.CharField(max_length=100, verbose_name='Укажите название фильма')
    country = models.CharField(max_length=100, verbose_name='Укажите название страны')
    image = models.ImageField(max_length=100, upload_to='films/')
    genre = models.CharField(max_length=100, choices=GENRE)
    director = models.CharField(max_length=100, verbose_name='Укажите директора')
    description = models.TextField(verbose_name='Укажите описание', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}-{self.country}'

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Afisha(models.Model):
    film_title = models.CharField(max_length=100)
    time_watch = models.TimeField()
    area = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.film_title


class Slider(models.Model):
    slider = models.URLField()

    def __str__(self):
        return self.slider