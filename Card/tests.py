from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Language, Module, Card

# To run tests:
# python manage.py test Card


class ModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')

        self.language = Language.objects.create(language_name='English', language_api='http://example.com/api')

        self.module = Module.objects.create(
            language_1=self.language,
            language_2=self.language,
            name='Test Module',
            description='Test Module Description',
            visibility=True,
            color='g',
            author=self.user
        )

        self.card = Card.objects.create(
            module=self.module,
            word_1='Word1',
            word_2='Word2',
            definition_1='Definition 1',
            definition_2='Definition 2'
        )

    def test_create_language(self):
        new_language = Language.objects.create(language_name='Spanish', language_api='http://example.com/api/es/')
        self.assertEqual(new_language.language_name, 'Spanish')
        self.assertEqual(new_language.language_api, 'http://example.com/api/es/')

    def test_create_module(self):
        new_module = Module.objects.create(
            language_1=self.language,
            language_2=self.language,
            name='New Module',
            description='New Module Description',
            visibility=True,
            color='b',
            author=self.user
        )
        self.assertEqual(new_module.name, 'New Module')
        self.assertEqual(new_module.color, 'b')
        self.assertEqual(new_module.author, self.user)

    def test_create_card(self):
        new_card = Card.objects.create(
            module=self.module,
            word_1='New Word 1',
            word_2='New Word 2',
            definition_1='New Definition 1',
            definition_2='New Definition 2'
        )
        self.assertEqual(new_card.word_1, 'New Word 1')
        self.assertEqual(new_card.definition_2, 'New Definition 2')

    def test_update_module(self):
        self.module.name = 'Updated Module'
        self.module.save()
        updated_module = Module.objects.get(pk=self.module.pk)
        self.assertEqual(updated_module.name, 'Updated Module')

    def test_delete_card(self):
        card_count_before = Card.objects.count()
        self.card.delete()
        card_count_after = Card.objects.count()
        self.assertEqual(card_count_after, card_count_before - 1)
