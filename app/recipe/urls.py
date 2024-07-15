"""
Url mappings for the recipe app.
"""

from django.urls import (
    path, include
)

from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register('recepies', viewset=views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]
