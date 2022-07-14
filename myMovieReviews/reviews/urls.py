from django.urls import path
from . import views

app_name = "reviews"
urlpatterns = [
    path('review', views.review_list, name='review_list'),
    path('create', views.review_create, name='review_create'),
    path('review/<int:id>', views.review_detail, name="review_detail"),
    path('review/<int:id>/update', views.review_update, name="review_update"),
]
