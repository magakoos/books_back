import datetime

from django.core.management import BaseCommand

from books import models


class Command(BaseCommand):
    """Создание данных для тестов."""

    def handle(self, *args, **options):
        """Создание данных."""

        genre = models.Genre.objects.create(
            name='Science Fiction'
        )
        author = models.Author.objects.create(
            name='Lisa A. Nichols'
        )
        publisher = models.Publisher.objects.create(
            name='Atria/Emily Bestler Books/Alloy Entertainment'
        )
        book = models.Book.objects.create(
            title='Vessel',
            description='Book1',
        )
        edition = models.Edition.objects.create(
            book=book,
            format=models.Edition.HARDCOVER,
            page_count=304,
            isbn='1501168770',
            isbn13='9781501168772',
            publication_date=datetime.date(2019, 5, 19),
            publisher=publisher,
        )
        book.genres.add(genre)
        book.authors.add(author)

        genre2 = models.Genre.objects.create(
            name='Fantasy'
        )
        author = models.Author.objects.create(
            name='Jess Rothenberg'
        )
        publisher = models.Publisher.objects.create(
            name='Henry Holt & Company'
        )
        book = models.Book.objects.create(
            title='The Kingdom',
            description='Book2',
        )
        edition = models.Edition.objects.create(
            book=book,
            format=models.Edition.HARDCOVER,
            page_count=352,
            isbn='1250293855',
            isbn13='9781250293855',
            publication_date=datetime.date(2019, 5, 28),
            publisher=publisher,
        )
        book.genres.add(genre, genre2)
        book.authors.add(author)

        genre = models.Genre.objects.create(
            name='Graphic novels'
        )
        author1 = models.Author.objects.create(
            name='Kateri Akiwenzie-Damm'
        )
        author2 = models.Author.objects.create(
            name='Chelsea Vowel'
        )
        author3 = models.Author.objects.create(
            name='Katherena Vermette'
        )
        author4 = models.Author.objects.create(
            name='Jen Storm'
        )
        author5 = models.Author.objects.create(
            name='Niigaanwewidam James Sinclair'
        )
        author6 = models.Author.objects.create(
            name='David Alexander Robertson'
        )
        publisher = models.Publisher.objects.create(
            name='HighWater Press'
        )
        book = models.Book.objects.create(
            title='This Place: 150 Years Retold',
            description='Book3',
        )
        edition = models.Edition.objects.create(
            book=book,
            format=models.Edition.SOFTCOVER,
            page_count=296,
            isbn='1553797582',
            isbn13='9781553797586',
            publication_date=datetime.date(2019, 5, 30),
            publisher=publisher,
        )
        book.genres.add(genre)
        book.authors.add(author1, author2, author3, author4, author5, author6)