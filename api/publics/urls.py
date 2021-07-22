from django.urls import include, path

from .views import PublicListCreateView

urlpatterns = [
    path('/', PublicListCreateView.as_view()),
]


