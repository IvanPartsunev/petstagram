from django.db import models
from django.utils.text import slugify


class Pet(models.Model):
    MAX_NAME_LENGTH = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        blank=False,
        null=False,
    )

    pet_photo = models.URLField(
        blank=False,
        null=False,
    )

    birth_date = models.DateField(
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=False,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.pk}")
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
