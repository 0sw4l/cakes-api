from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.api.app.serializers import ClienteSerializer
from apps.app.models import Cliente
from apps.utils.shortcuts import get_object_or_none


class ClienteView(mixins.CreateModelMixin,
                  generics.GenericAPIView):
    serializer_class = ClienteSerializer

    def post(self, request, *args, **kwargs):
        client = get_object_or_none(Cliente, cedula=request.data['cedula'])
        if client:
            return Response({
                'id': client.id
            })
        return self.create(request, *args, **kwargs)


