from re import I
from django.urls import path, include
from rest_framework         import routers
from rest_framework.routers import DefaultRouter

from .views import AdminViewSet
# from .views import AdminListCreateView, AdminRetrieveUpdateDestroyView

# from .views import AdminList
from .views import AdminViewSet

from api.admins import views

router = routers.DefaultRouter()
router.register(r'', views.AdminViewSet)

urlpatterns = [
    path('/',include(router.urls)),
    # path('/', AdminListCreateView.as_view()),
    # path('/<int:pk>', AdminRetrieveUpdateDestroyView.as_view()),
    # path("/", AdminList.as_view())
]

# localhost:8000/api/admins
# localhost:8000/api/publics