from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    # URL Address Of Name
    slug = models.SlugField()

    #For Ordering Categories
    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name

    #Returns The URL Of The Category
    def get_absolute_url(self) -> str:
        return f'/{self.slug}/'
