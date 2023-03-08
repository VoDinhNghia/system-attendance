from rest_framework import serializers

class CollectionImageForm(serializers.Serializer):
    profileId = serializers.CharField()