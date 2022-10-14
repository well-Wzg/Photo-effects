from django.urls import path
from main_app import views

app_name = "main_app"
urlpatterns = [
    path('', views.IndexView.as_view(),name="index"),
    path('edit/<str:id>/', views.EditView.as_view(),name="edit"),
]