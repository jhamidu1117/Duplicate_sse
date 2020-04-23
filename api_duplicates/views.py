from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers import TRGidSerializer
from .models import TRGid
# Create your views here.


class TRGidViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TRGid.objects.all()
    serializer_class = TRGidSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TRGsView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        trgs = TRGid.objects.all()
        serializer = TRGidSerializer(trgs, many=True)
        content = {'message': 'Hello, World!'}
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = TRGidSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
