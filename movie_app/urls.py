from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserProfileListAPIView,UserProfileAPIView, CategoryListAPIView, CategoryDetailAPIView,
    GenreListAPIView, GenreDetailAPIView, CountryListAPIView, CountryDetailAPIView,
    DirectorListAPIView,DirectorDetailAPIView,ActorListAPIView,ActorDetailAPIView, MovieListAPIView, MovieDetailAPIView,
    MovieVideoViewSet, MovieFrameViewset,RatingCreateViewAPIView, ReviewCreateViewAPIView,
    ReviewLikeViewSet, FavoriteViewSet, FavouriteItemViewSet, HistoryViewSet,RegisterView,LoginView,LogoutView
)

router = DefaultRouter()
router.register(r'movie-videos', MovieVideoViewSet)
router.register(r'movie-frames', MovieFrameViewset)
router.register(r'review-likes', ReviewLikeViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'favorite-items', FavouriteItemViewSet)
router.register(r'history', HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('genre/', GenreListAPIView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetailAPIView.as_view(), name='genre_detail'),
    path('movie/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('director/',DirectorListAPIView.as_view(), name='director_list'),
    path('director/<int:pk>/', DirectorDetailAPIView.as_view(), name='country_detail'),
    path('actor/',ActorListAPIView.as_view(), name='actor_list'),
    path('actor/<int:pk>/',ActorDetailAPIView.as_view(), name='actor_detail'),
    path('user/',UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/',UserProfileAPIView.as_view(), name='user_detail'),
    path('rating/', RatingCreateViewAPIView.as_view(), name='ratings'),
    path('review/', ReviewCreateViewAPIView.as_view(), name='reviews'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
