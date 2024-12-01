from django.urls import path, include
from django.contrib import admin
from .views import Add_to_reestrView, register_detail, IndexView, ReestrListView
from . import views


app_name = "reestr_list"

urlpatterns = [
    path("admin", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    # path("reestr/", reestr_list, name="reestr_list"),
    path("reestr/", views.ReestrListView.as_view(), name="reestr_list"),
    path("reestr/add/", Add_to_reestrView.as_view(), name="add_to_register"),
    path("reestr/<slug:id_numb>/", register_detail, name="register_detail"),
]
