from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator,MaxValueValidator

StatusChoices = (
    ('pro', 'pro'),
    ('simple', 'simple'),
)

class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(10), MaxValueValidator(70)],
        null=True,
        blank=True
    )
    user_photo = models.ImageField(upload_to='user_images', null=True, blank=True)


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
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='genre')

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
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.full_name


class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    slogan = models.CharField(max_length=100, null=True, blank=True)
    year = models.DateField()

    country = models.ManyToManyField(Country,related_name='country_movies')
    director = models.ManyToManyField(Director,related_name='director_movies')
    genre = models.ManyToManyField(Genre,related_name='genres_movies' )
    actors = models.ManyToManyField(Actor,related_name='movies')

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
    movie_status = models.CharField(max_length=30,choices=StatusChoices,default='simple')

    def __str__(self):
        return self.movie_name



class MovieVideo(models.Model):
    video_name = models.CharField(max_length=50)
    video = models.FileField(upload_to='movie_videos')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie} - {self.video_name}'



    def ger_avg_rating(self):
        all_ratings = self.ratings.all()
        if all_ratings.exists():
            [i.stars for i in all_ratings]
        return 0



class MovieFrame(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='movie_frames')

    def __str__(self):
        return f'{self.movie}{self.image}'


class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1, 11)]
    )

    def __str__(self):
        return f'{self.user},{self.movie},{self.stars}'



class Review(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user},{self.comment}'


class ReviewLike(models.Model):
    review = models.ForeignKey(Review,on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    like = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.user},{self.like}'



class Favorite(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'



class FavouriteItem(models.Model):
    favorite = models.ForeignKey(Favorite,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.favorite},{self.movie}'



class History(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    watched_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user},{self.movie},{self.watched_date}'



