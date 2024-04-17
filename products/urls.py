from django.urls import path
from . import views


app_name = 'post'

urlpatterns = [
    path("",views.post_list, name="list"),
    path("<int:post_id>/",views.post_detail, name="detail"),
    path("create/",views.create, name="create"),
    path("update/<int:post_id>/",views.update, name="update"),
    path("<int:post_id>/delete/",views.delete, name="delete"),

]