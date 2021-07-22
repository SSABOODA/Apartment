from api.publics.serializers import CheckCostSerializer, PublicSerializer

from rest_framework          import mixins
from rest_framework          import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Public

# mixin + GenericView
class PublicListCreateView(mixins.ListModelMixin, GenericAPIView):

    queryset = Public.objects.all()
    serializer_class = CheckCostSerializer
    
    def post(self, request, *args, **kwargs):
        try:
            household_number = request.data['household_number']
            password         = request.data['password']

            publics = Public.objects.get(household_number=household_number, password=password)

            serializers = PublicSerializer(publics)

            return Response(serializers.data, status=status.HTTP_200_OK)
        except Public.DoesNotExist:
            return Response({'MESSAGE' : '입력하신 정보와 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

