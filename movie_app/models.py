from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator,MaxValueValidator


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(70)],
        null=True,
        blank=True
    )
    user_photo = models.ImageField(upload_to='user_images', null=True, blank=True)

    StatusChoices = (
        ('pro', 'pro'),
        ('simple', 'simple'),
    )
    status = models.CharField(max_length=120, choices=StatusChoices, default='simple')
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.category_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category}, {self.genre_name}'


class Country(models.Model):
    country_name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.country_name


class Director(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    director_photo = models.ImageField(upload_to='director_images')
    bio = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return self.full_name


class Actor(models.Model):
    full_name = models.CharField(max_length=100)
    actor_photo = models.ImageField(upload_to='actor_images', null=True, blank=True)

    def __str__(self):
        return self.full_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    slogan = models.CharField(max_length=100, null=True, blank=True)
    year = models.DateField()

    country = models.ManyToManyField(Country)
    director = models.ManyToManyField(Director)
    genre = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)

    MovieTypeChoices = (
        ('360', '360'),
        ('480', '480'),
        ('720', '720'),
        ('1080p', '1080p'),
        ('1080p Ultra', '1080p Ultra'),
    )
    movie_type = models.CharField(max_length=20, choices=MovieTypeChoices)
    movie_time = models.PositiveSmallIntegerField()
    movie_poster = models.ImageField(upload_to='movie_images')
    trailer = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.movie_name


class MovieVideo(models.Model):
    video_name = models.CharField(max_length=50)
    video = models.FileField(upload_to='movie_videos')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie} - {self.video_name}'
