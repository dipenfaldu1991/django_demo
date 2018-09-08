from rest_framework import serializers
from student.models import student
from rest_framework.renderers import JSONRenderer


class user(serializers.HyperlinkedModelSerializer):
    class Mata:
        model=student
        field=(__all__)