from rest_framework import serializers
from .models import Little

class LittleSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Little
		fields = ('id', 'name', 'alias')