from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User


class Category(MPTTModel):
    name = models.CharField("Назва", max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name = "Категорії"


class FilterAdvert(models.Model):
    name = models.CharField("Назва", max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фільтр"
        verbose_name_plural = "Фільтри"


class DateAdvert(models.Model):
    name = models.CharField("Назва", max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Термін"
        verbose_name_plural = "Терміни"
        ordering = ["id"]


class Advert(models.Model):
    user = models.ForeignKey(User, verbose_name="Користувач", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Категорія", on_delete=models.CASCADE)
    filters = models.ForeignKey(FilterAdvert, verbose_name="Фільтр", on_delete=models.CASCADE)
    date = models.ForeignKey(DateAdvert, verbose_name="Термін", on_delete=models.CASCADE)
    subject = models.CharField("Teма", max_length=200)
    description = models.TextField("Оголошення", max_length=1000)
    images = models.ForeignKey('gallery.Gallery', verbose_name="Зображення", blank=True, null=True, on_delete=models.SET_NULL)
    file = models.FileField("Файл", upload_to="petsCallboard_files/", blank=True, null=True)
    created = models.DateTimeField("Дата створення", auto_now_add=True)
    moderation = models.BooleanField("Модерація", default=False)
    price = models.DecimalField("Винагорода", max_digits=8, decimal_places=2)
    slug = models.SlugField("url", max_length=200, unique=True)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("advert-detail", kwargs={"category": self.category.slug, "slug": self.slug})

    class Meta:
        verbose_name = "Оголошення"
        verbose_name_plural = "Оголошення"


