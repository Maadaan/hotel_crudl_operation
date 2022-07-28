from rest_framework import serializers
from .models import Hotel


class HotelSerializers(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    email = serializers.EmailField()
    phone_no = serializers.CharField()

    def create(self, validated_data):
        return Hotel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_no = validated_data.get('phone_no', instance.phone_no)
        instance.save()
        return instance
