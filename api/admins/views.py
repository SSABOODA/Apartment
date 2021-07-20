from rest_framework          import status

# APIView
# from rest_framework.views    import APIView

# concrete View = genericAPIView + mixin class ##
# from rest_framework.generics import GenericAPIView
# from rest_framework          import mixins
# from rest_framework          import generics 

## viewset
from rest_framework          import viewsets

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Admin
from api.admins.serializers import AdminSerializer

from rest_framework.permissions import IsAuthenticated

# ViewSet
class AdminViewSet(viewsets.ModelViewSet):
    queryset         = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated]

# Mixin + Generic
# class AdminListCreateView(mixins.CreateModelMixin, 
#                             mixins.ListModelMixin,
#                             GenericAPIView):

#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
    
#     queryset = Admin.objects.all()
#     serializer_class = AdminSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class AdminRetrieveUpdateDestroyView(mixins.RetrieveModelMixin,
#                                         mixins.DestroyModelMixin,
#                                         mixins.UpdateModelMixin,
#                                         GenericAPIView):

#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     queryset = Admin.objects.all()
#     serializer_class = AdminSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):

#         return self.partial_update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
