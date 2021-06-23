from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'



class OfficeSerializer(serializers.ModelSerializer):
    get_full_title = serializers.ReadOnlyField()
    get_count_rooms = serializers.ReadOnlyField()
    type = serializers.CharField(source='get_type_display')
    rooms = RoomSerializer(many=True)

    places_count = serializers.SerializerMethodField()


    def get_places_count(self, obj):
        count = 0
        for room in obj.rooms.all():
            count += room.places.count()
        return count

    class Meta:
        model = Office
        fields = '__all__'
