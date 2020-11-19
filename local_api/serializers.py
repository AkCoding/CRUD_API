from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()


#for create/post
    def create(self, validated_data):
        return Student.objects.create(**validated_data)


# for update/patch
    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance



    # Field level Validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('seat Full')
        return value




