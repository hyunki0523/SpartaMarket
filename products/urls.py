from django.urls import path
from . import views


app_name = 'post'

urlpatterns = [
    path("",views.post_list, name="list"),
    path("<int:pk>/",views.post_detail, name="detail"),
    path("create/",views.create, name="create"),
    path("update/<int:pk>",views.update, name="update"),
    path("delete/<int:pk>",views.delete, name="delete"),
    path("<int:pk>/comments/", views.comment_create, name="comment_create"),
    path("<int:pk>/comments/<int:comment_pk>/delete/",views.comment_delete,name="comment_delete"),
    path("<int:pk>/check/", views.check, name="check"),
]