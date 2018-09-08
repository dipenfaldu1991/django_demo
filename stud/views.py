from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import user
from rest_framework import authentication,permissions


