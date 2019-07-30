from django.test import TestCase

from catalog.models import Author, Language, BookInstance, Book, Genre
# Create your tests here.


class YourTestClass(TestCase):
    """."""

    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods."""
        Author.objects.create(first_name='Big', last_name='Ann')
        Language.objects.create(name='English')
        Genre.objects.create(name='Science Fiction')
        Book.objects.create(title='FooBar Strikes Again', summary='Really good book', isbn='0000000000000')
        # x = BookInstance.objects.create(imprint='orange', status='o')
        pass

    def test_book_instance_repr_method(self):
        """Test imprint field label in book instance model."""
        book = Book.objects.get(id=1)
        x = BookInstance.objects.create(imprint='orange', status='o', book=book)
        expected_object = f'{x.id} ({x.book.title})'
        self.assertEquals(expected_object, f'{x.id} (FooBar Strikes Again)')

    def test_book_instance_imprint_label(self):
        """Test imprint field label in book instance model."""
        x = BookInstance.objects.create(imprint='orange', status='o')
        field_label = x._meta.get_field('imprint').verbose_name
        self.assertEquals(field_label, 'imprint')

    def test_book_instance_imprint_label_output_repr(self):
        """Test imprint field label in book instance model."""
        x = BookInstance.objects.create(imprint='orange', status='o')
        expected_object = f'{x.imprint}'
        self.assertEquals(expected_object, 'orange')

    def test_book_instance_imprint_label_max_length(self):
        """Test imprint field label max lengthin book instance model."""
        x = BookInstance.objects.create(imprint='orange', status='o')
        field_label = x._meta.get_field('imprint').max_length
        self.assertEquals(field_label, 200)

    def test_book_instance_status_label(self):
        """Test status field label in book instance model."""
        x = BookInstance.objects.create(imprint='orange', status='o')
        field_label = x._meta.get_field('status').verbose_name
        self.assertEquals(field_label, 'status')

    def test_book_instance_status_label_output_repr(self):
        """Test status field label in book instance model."""
        x = BookInstance.objects.create(imprint='orange', status='o')
        expected_object = f'{x.status}'
        self.assertEquals(expected_object, 'o')

    def test_book_instance_status_label_max_length(self):
        """Test imprint field label max lengthin book instance model."""
        x = BookInstance.objects.create(imprint='orange', status='o')
        field_label = x._meta.get_field('status').max_length
        self.assertEquals(field_label, 1)

    def test_get_absolute_url_book(self):
        """Test get absolute url for book model object."""
        book = Book.objects.get(id=1)
        self.assertEquals(book.get_absolute_url(), '/catalog/book/1')

    def test_display_genre_book(self):
        """Test for display genre method on book model object."""
        book = Book.objects.get(id=1)
        self.assertEquals(book.display_genre(), '')

    def test_title_label_book(self):
        """Test the title lable in book model object."""
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_label_representation_method(self):
        """Test the string representation method in book object model."""
        book = Book.objects.get(id=1)
        expected_object = f'{book.title}'
        self.assertEquals(expected_object, str(book))

    def test_title_max_length(self):
        """Test the max length of the title field in book object."""
        book = Book.objects.get(id=1)
        expected_length = book._meta.get_field('title').max_length
        self.assertEquals(expected_length, 200)

    def test_label_summary_field_book(self):
        """Test the summary field in book object."""
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('summary').verbose_name
        self.assertEquals(field_label, 'summary')

    def test_label_summary_representation_book(self):
        """Test the summary field representation from setup."""
        book = Book.objects.get(id=1)
        expected_repr = f'{book.summary}'
        self.assertEquals(expected_repr, 'Really good book')

    def test_summary_max_length(self):
        """Test the max length of the summary field in book object."""
        book = Book.objects.get(id=1)
        expected_length = book._meta.get_field('summary').max_length
        self.assertEquals(expected_length, 1000)

    def test_label_isbn_field_book(self):
        """Test the isbn field in book object."""
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEquals(field_label, 'ISBN')

    def test_label_summary_representation_book(self):
        """Test the isbn field representation from setup."""
        book = Book.objects.get(id=1)
        expected_repr = f'{book.isbn}'
        self.assertEquals(expected_repr, '0000000000000')

    def test_isbn_max_length(self):
        """Test the max length of the isbn field in book object."""
        book = Book.objects.get(id=1)
        expected_length = book._meta.get_field('isbn').max_length
        self.assertEquals(expected_length, 13)


    def test_name_label_genre(self):
        """Test the name label of genre object."""
        genre = Genre.objects.get(id=1)
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_label_string_representation_genre(self):
        """Test string represenation of genre object model."""
        genre = Genre.objects.get(id=1)
        expected_object = f'{genre.name}'
        self.assertEquals(expected_object, 'Science Fiction')

    def test_string_repr_method_for_genre(self):
        """Test string repr method for genre object model."""
        genre = Genre.objects.get(id=1)
        expected_object = genre.name.__str__()
        self.assertEquals(expected_object, 'Science Fiction')

    def test_genre_max_length(self):
        """Test max length value for genre object."""
        genre = Genre.objects.get(id=1)
        expected_length = genre._meta.get_field('name').max_length
        self.assertEquals(expected_length, 200)

    def test_name_label(self):
        """Test Language object name."""
        language = Language.objects.get(id=1)
        field_label = language._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_label_string_representation(self):
        """Test Language object string representation from setUp object."""
        language = Language.objects.get(id=1)
        expected_object_name = f'{language.name}'
        self.assertEquals(expected_object_name, str(language))

    def test_name_max_length(self):
        """Test Language object max length field."""
        language = Language.objects.get(id=1)
        field_label_max_length = language._meta.get_field('name').max_length
        self.assertEquals(field_label_max_length, 50)

    def test_first_name_label(self):
        """."""
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        """."""
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_date_of_death_label(self):
        """."""
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'Died')

    def test_date_of_birth_label(self):
        """."""
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_first_name_max_length(self):
        """."""
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').max_length
        self.assertEquals(field_label, 100)

    def test_last_name_max_length(self):
        """."""
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').max_length
        self.assertEquals(field_label, 100)

    def test_object_name_is_last_name_comma_first_name(self):
        """."""
        author = Author.objects.get(id=1)
        expected_object_name = f'{author.last_name}, {author.first_name}'
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        """."""
        author = Author.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(), '/catalog/author/1')
