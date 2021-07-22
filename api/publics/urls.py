from django.urls import include, path

from .views import PublicListCreateView

# router = routers.DefaultRouter()
# router.register(r'', PublicViewSet)

urlpatterns = [
    path('/', PublicListCreateView.as_view()),
]


