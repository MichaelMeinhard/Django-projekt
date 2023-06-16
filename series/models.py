from django.db import models


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='Genre',
                            help_text='Enter a series genre')
    description = models.TextField(verbose_name='description',
                                   help_text='Enter description',
                                   blank=True,
                                   null=True)

    class Meta:
        verbose_name = "Genre"
        ordering = ['name']

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=50,
                            unique=True,
                            verbose_name='Name',
                            help_text='Enter name')
    description = models.TextField(verbose_name='description',
                                   help_text='Enter description',
                                   blank=True,
                                   null=True)
    length = models.IntegerField(help_text='Enter length of this series in hours',
                                 verbose_name='length in hours',
                                 blank=True,
                                 null=True)
    season = models.IntegerField(verbose_name='Number of seasons',
                                 help_text='Enter number of seasons',
                                 blank=True,
                                 null=True,
                                 default=0)
    episodes = models.IntegerField(verbose_name='Number of episodes',
                                   help_text='Enter number of episodes',
                                   blank=True,
                                   null=True,
                                   default=0)
    genres = models.ManyToManyField('Genre',
                                    verbose_name='Genres of series')
    directors = models.ManyToManyField('Director',
                                       verbose_name='Directors')
    foto = models.ImageField(verbose_name='Photo',
                             help_text='Select picture',
                             blank=True,
                             null=True)

    class Meta:
        verbose_name = 'Series'
        ordering = ['name']
        verbose_name_plural = 'Seriess'

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=50,
                            unique=False,
                            verbose_name='First name',
                            help_text='Enter first name')
    sname = models.CharField(max_length=50,
                             unique=False,
                             verbose_name='Second name',
                             help_text='Enter second name')
    bio = models.TextField(max_length=2000,
                           verbose_name='Bio',
                           help_text='Enter bio',
                           blank=True,
                           null=True)
    birth = models.DateField(verbose_name='Date of birth',
                             help_text='Enter date of birth',
                             null=True,
                             blank=True)
    foto = models.ImageField(verbose_name='Photo',
                             help_text='Select picture',
                             blank=True,
                             null=True)

    class Meta:
        verbose_name = "Director"
        ordering = ['name']

    def __str__(self):
        return self.name + ' ' + self.sname
