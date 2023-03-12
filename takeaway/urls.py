from django.urls import path
from takeaway import views

app_name = "takeaway"

urlpatterns = [
    path("", views.index, name="index"),
    path("account/<username>/", views.AccountView.as_view(), name="account"),
]