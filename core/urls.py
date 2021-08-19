from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.add),
    path('shows/create', views.create),
    path('shows/<int:show_id>',views.show),
    path('<int:show_id>/edit', views.edit),
    path('shows/<int:show_id>/update', views.update),
    path('shows/<int:show_id>/destroy', views.delete),
]
