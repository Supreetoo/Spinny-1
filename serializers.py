from rest_framework import serializers
from .models import Box

class BoxSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Box
        fields = ('id', 'length', 'width', 'height', 'created_by', 'created_at', 'last_updated', 'area', 'volume')


class BoxListSerializer(serializers.ModelSerializer):
    length = serializers.SerializerMethodField()
    width = serializers.SerializerMethodField()
    height = serializers.SerializerMethodField()
    area = serializers.SerializerMethodField()
    volume = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()
    last_updated = serializers.SerializerMethodField()

    class Meta:
        model = Box
        fields = ('id', 'length', 'width', 'height', 'area', 'volume', 'created_by', 'last_updated')

    def get_length(self, obj):
        return obj.length
    
    def get_width(self, obj):
        return obj.width
    
    def get_height(self, obj):
        return obj.height

    def get_area(self, obj):
        return obj.length * obj.width * obj.height

    def get_volume(self, obj):
        return obj.length * obj.width * obj.height

    def get_created_by(self, obj):
        user = obj.creator
        return user.username if user else None

    def get_last_updated(self, obj):
        return obj.updated_at if obj.updated_at else None
