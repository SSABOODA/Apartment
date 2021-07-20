from django.urls import path, include
from rest_framework         import routers
from rest_framework.routers import DefaultRouter

from .views import PublicViewSet
# from .views import PublicListCreateView, PublicRetrieveUpdateDestroyView

# from api.admins import views

router = routers.DefaultRouter()
router.register(r'', PublicViewSet)

urlpatterns = [
    path('/',include(router.urls)),
    # path('/', PublicListCreateView.as_view()),
    # path('/<int:pk>', PublicRetrieveUpdateDestroyView.as_view()),
]

# localhost:8000/api/admins
# localhost:8000/api/publics


