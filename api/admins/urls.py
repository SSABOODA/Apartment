from django.urls import path, include
# from rest_framework         import routers
# from rest_framework.routers import DefaultRouter

# router = routers.DefaultRouter()
# router.register(r'', views.AdminViewSet)

from .views import PublicCostListView, PublicCostDetailView

urlpatterns = [
    # path('/',include(router.urls)),
    path('/', PublicCostListView.as_view()),
    path('/<int:pk>/', PublicCostDetailView.as_view()),
    
]

# localhost:8000/api/admins
# localhost:8000/api/publics