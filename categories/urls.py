from django.urls import path

from categories.views import (
    CategoriesView,
)
urlpatterns = [
    path('', CategoriesView.as_view()),
]