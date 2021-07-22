from rest_framework.response import Response
from api.publics.models      import Public
from api.publics.serializers import PublicSerializer

from rest_framework             import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated


# generics.
class PublicCostListView(generics.ListCreateAPIView):
    queryset = Public.objects.all()
    serializer_class = PublicSerializer

    permission_classes = [IsAdminUser]

class PublicCostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Public.objects.all()
    serializer_class = PublicSerializer
    
    permission_classes = [IsAuthenticated]
