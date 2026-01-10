from django.urls import path

from . import views
urlpatterns = [
   path('', views.index, name='contacts'),
   path('creer-contact/', views.store, name='store'),
   path('edite-contact/<int:id>', views.edite, name='edite'),
   path('show-contact/<int:id>', views.show, name='show'),
   path('delete-contact/<int:id>/', views.delete, name='delete')
]
