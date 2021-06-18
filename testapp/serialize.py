from rest_framework import serializers
from testapp.models import details


class detailserialize(serializers.ModelSerializer):
	class Meta:
		model=details
		fields="__all__"