from rest_framework          import status

## APIView
# from rest_framework.views    import APIView

# concrete View = genericAPIView + mixin class ##
# from rest_framework.generics import GenericAPIView
# from rest_framework          import mixins
# from rest_framework          import generics 

## viewset
from rest_framework          import viewsets

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Public

from api.publics.serializers import PublicSerializer

class PublicViewSet(viewsets.ModelViewSet):
    queryset         = Public.objects.all()
    serializer_class = PublicSerializer
    permission_classes = [IsAuthenticated]

# class PublicListCreateView(mixins.CreateModelMixin, 
#                             mixins.ListModelMixin,
#                             GenericAPIView):

#     queryset = Public.objects.all()
#     serializer_class = PublicSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class PublicRetrieveUpdateDestroyView(mixins.RetrieveModelMixin,
#                                         mixins.DestroyModelMixin,
#                                         mixins.UpdateModelMixin,
#                                         GenericAPIView):
#     queryset = Public.objects.all()
#     serializer_class = PublicSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
