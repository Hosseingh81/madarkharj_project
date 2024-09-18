from django.urls import path
from . import views
app_name='madarkharj'

urlpatterns = [
    path("<str:username>/",views.main_user_page_view.as_view(),name="mainpage"),
]
