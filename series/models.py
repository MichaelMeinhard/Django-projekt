from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='Genre',
                            help_text='Enter a series genre')
    description = models.TextField(blank=True,
                                   null=True)

    class Meta:
        verbose_name = "Seriál"
        ordering = ['name']

    def __str__(self):
        return self.name
