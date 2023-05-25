# from . import views



from . import views
from django.urls import path


urlpatterns = [
    path('create/', views.create_view,name="create"),
    path('list/', views.list_view,name="list"),
    path('delete/<id>/', views.delete_view,name="delete"),
    path('update/<id>/', views.update_view,name="update"),
    path('success/', views.success_view,name="create"),


]