from django.urls import path, include

from .views import PublicCostListView, PublicCostDetailView

urlpatterns = [

    path('/', PublicCostListView.as_view()),
    path('/<int:pk>/', PublicCostDetailView.as_view()),
    
]

