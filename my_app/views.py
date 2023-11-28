from django.shortcuts import render
from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     ListCreateAPIView, CreateAPIView,
                                     UpdateAPIView,DestroyAPIView)

from my_app.models import *
from my_app.serializers import *


class GYMListView(ListAPIView):
    queryset = GYM.objects.all()
    serializer_class = GYMSerializer

class GYMCreateAPIView(CreateAPIView):
    queryset = GYM.objects.all()
    serializer_class = GYMSerializer

class GYMUpdateAPIView(UpdateAPIView):
    queryset = GYM.objects.all()
    serializer_class = GYMSerializer
    lookup_field = 'id'

class GYMRetrieveAPIView(RetrieveAPIView):
    queryset = GYM.objects.all()
    serializer_class = GYMSerializer
    lookup_field = 'id'

class GYMDestroyAPIView(DestroyAPIView):
    queryset = GYM.objects.all()
    serializer_class = GYMSerializer
    lookup_field = 'id'
