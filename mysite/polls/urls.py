from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path('', views.landing, name='landing'),
    path("index/", views.index, name='index'),
    path("games/", views.games, name="games"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]