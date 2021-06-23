from django.shortcuts import render
from rest_framework.response import Response

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status

from .models import Study
from .serializers import StudySerializer


class StudyList(APIView):
    def post(self, request, format=None):
        serializer = StudySerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()      
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
