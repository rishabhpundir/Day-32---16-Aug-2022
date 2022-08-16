from django.urls import path
from apiapp import views

urlpatterns = [
    path('list/', views.movie_list),
    path('list/<int:movie_id>', views.movie_details),
]
