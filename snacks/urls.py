from django.urls import path
from .views import SnackListView,SnackListDetail

urlpatterns = [
    path('',SnackListView.as_view(),name = 'list_view'),
    path('<int:pk>/',SnackListDetail.as_view(),name = 'list_detail')
    ]