from django.urls import path
from .views import reestr_list, Add_to_reestrView, IndexView


app_name = "reestr_list"

urlpatterns = [
    path("/", IndexView.as_view(), name="index"),
    path("reestr/", reestr_list, name="reestr_list"),
    path("reestr/add/", Add_to_reestrView.as_view(), name="add_to_register"),
]
