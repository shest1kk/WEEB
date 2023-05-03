from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Car
from .serializers import CarSerializers


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializers

@action(detail=False)
def send_report(self, request):
    send_report()
    return Response(status=status.HTTP_200_OK)
