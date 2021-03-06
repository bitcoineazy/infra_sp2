from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='categories')
router.register(r'titles', views.TitleViewSet, basename='titles')
router.register(r'genres', views.GenreViewSet, basename='genres')

urlpatterns = [
    path('v1/', include(router.urls)),
]
