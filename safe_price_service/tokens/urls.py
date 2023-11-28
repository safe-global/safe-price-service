from django.urls import path

from . import views

app_name = "tokens"

urlpatterns = [
    path(
        "<int:chain_id>/tokens/<str:address>/prices/usd/",
        views.TokenPriceView.as_view(),
        name="price-usd",
    ),
]
