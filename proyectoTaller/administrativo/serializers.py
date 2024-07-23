from django.contrib.auth.models import User, Group
from administrativo.models import Departamento, Edificio

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EdificioSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Edificio
        fields = '__all__'


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    departamento_str = serializers.StringRelatedField(source="departamento", read_only=True)
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Departamento
        # fields = ['id', 'telefono', 'tipo']
        fields = '__all__'
