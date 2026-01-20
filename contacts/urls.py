from django.urls import path

from . import views

urlpatterns = [
   # path('', views.index, name='contacts'),
   path('', views.ListContactView.as_view(), name='contacts'),
   path('creer-contact/', views.CreateContacView.as_view(), name='store'),
   path('edite-contact/<int:pk>', views.UpdateContactView.as_view(), name='edite'),
   path('show-contact/<int:pk>', views.DetailContactView.as_view(), name='show'),
   path('delete-contact/<int:pk>/', views.DeleteContactView.as_view(), name='delete')
]
