from django.db import models


class Author(models.Model):
    name = models.CharField('ФИО', max_length=128)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Genre(models.Model):
    name = models.CharField('Название', max_length=32)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Publisher(models.Model):
    name = models.CharField('Название', max_length=32)

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'


class Book(models.Model):
    authors = models.ManyToManyField(Author)
    genres = models.ManyToManyField(Genre)
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Edition(models.Model):

    HARDCOVER = 1
    SOFTCOVER = 2
    AUDIO = 3

    FORMATS = (
        (HARDCOVER, 'Твердый переплет'),
        (SOFTCOVER, 'Мягкий переплет'),
        (AUDIO, 'Аудио книга'),
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        null=False,
    )
    format = models.PositiveSmallIntegerField(
        'Тип обложки',
        choices=FORMATS,
        default=1
    )
    page_count = models.PositiveIntegerField('Кол-во страниц')
    publication_date = models.DateField('Дата публикации')
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        null=False,
    )
    isbn = models.CharField('ISBN', max_length=10)
    isbn13 = models.CharField('ISBN13', max_length=13)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
