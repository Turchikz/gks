from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from .views import Add_to_reestrView, register_detail, IndexView, ReestrListView
from . import views


app_name = "reestr_list"

urlpatterns = [
    path("admin", admin.site.urls),
    path("", IndexView.as_view(), name="index"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("reestr/", ReestrListView.as_view(), name="reestr_list"),
    path("reestr/add/", Add_to_reestrView.as_view(), name="add_to_register"),
    path("reestr/<slug:id_numb>/", register_detail, name="register_detail"),
    # path("login/", views.LoginView.as_view(), name="login"),
    # path("logout/", views.LogoutView.as_view(), name="logout"),
    # path("password_change/", views.PasswordChangeView.as_view(), name="password_change"),
    # path("password_change/done/", views.PasswordChangeDoneView.as_view(), name="password_change_done",),
    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # path("password_reset/done/", views.PasswordResetDoneView.as_view(), name="password_reset_done",),
    # path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm",),
    # path("reset/done/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete",),
]
