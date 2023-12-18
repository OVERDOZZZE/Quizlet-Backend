from django.db import models
from User.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class Language(models.Model):
    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    language_name = models.CharField(
        max_length=255,
        verbose_name='Language name'
    )
    language_api = models.CharField(
        max_length=355,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.language_name


class Module(models.Model):
    COLORS = [
        ('r', 'red'),
        ('g', 'green'),
        ('b', 'blue'),
        ('g', 'gray')
    ]

    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    language_1 = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        verbose_name='Language 1',
        related_name='module_language_1'
    )
    language_2 = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        verbose_name='Language 2',
        related_name='module_language_2'
    )
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Name'
    )
    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Creation date'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Module description'
    )
    visibility = models.BooleanField(
        verbose_name='Module visibility',
        help_text='Click to hide your module from other users'
    )
    color = models.CharField(
        choices=COLORS,
        max_length=255,
        verbose_name='Module color',
        default='g'
    )
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'

    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        verbose_name='Card module'
    )
    word_1 = models.CharField(
        max_length=255,
        verbose_name='Word 1'
    )
    word_2 = models.CharField(
        max_length=255,
        verbose_name='Word 2'
    )
    definition_1 = models.TextField(
        blank=True,
        null=True,
        verbose_name='Card 1 Definition'
    )
    definition_2 = models.TextField(
        blank=True,
        null=True,
        verbose_name='Card 2 Definition'
    )
    image = models.ImageField(
        upload_to='images/card_images/',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.word_1} - {self.word_2}'


# @receiver(post_save, sender=Module)
# def set_author_on_creation(sender, instance, created, **kwargs):
#     if created:
#         user = CustomUser.objects.get(username='ваше_имя_пользователя')
#         instance.author = user
#         instance.save()
