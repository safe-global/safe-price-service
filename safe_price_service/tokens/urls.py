from django.urls import path

from . import views

app_name = "tokens"

urlpatterns = [
    path("about/", views.AboutView.as_view(), name="about"),
    path(
        "<int:chain_id>/tokens/<str:address>/prices/usd/",
        views.TokenPriceView.as_view(),
        name="price-usd",
    ),
]
