from django.test import TestCase
from gallery.models import *
from datetime import date

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='surrealism')

    def test_str_method(self):
        category = Category.objects.get(id=1)
        expected_object_name = 'surrealism'
        self.assertEquals(str(category), expected_object_name)

    def test_name_content(self):
        category = Category.objects.get(id=1)
        expected_name = 'surrealism'
        self.assertEquals(category.name, expected_name)

class ImageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='surrealism')
        cls.image = Image.objects.create(
            title='The Persistence of Memory',
            image='path/to/image.jpg',  
            created_date=date.today(),
            age_limit=18
        )
        cls.image.categories.add(cls.category)

    def test_str_method(self):
        image = Image.objects.get(id=1)
        expected_object_name = 'The Persistence of Memory'
        self.assertEquals(str(image), expected_object_name)

    def test_title_content(self):
        image = Image.objects.get(id=1)
        expected_title = 'The Persistence of Memory'
        self.assertEquals(image.title, expected_title)

    def test_image_content(self):
        image = Image.objects.get(id=1)
        expected_image_path = 'path/to/image.jpg'
        self.assertEquals(image.image, expected_image_path)

    def test_created_date_content(self):
        image = Image.objects.get(id=1)
        expected_date = date.today()
        self.assertEquals(image.created_date, expected_date)

    def test_age_limit_content(self):
        image = Image.objects.get(id=1)
        expected_age_limit = 18
        self.assertEquals(image.age_limit, expected_age_limit)

    def test_categories(self):
        image = Image.objects.get(id=1)
        self.assertIn(self.category, image.categories.all())
