from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform

class StreamPlatformSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField() # def get_len_name이 호출됨.
    
    class Meta:
        model = WatchList
        fields = "__all__"
    
    # def get_len_name(self, object): # get_<vaiable_name>
    #     return len(object.name)
            
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Title and Description should be different!")
    #     else:
    #         return data
            
    # def validate_name(self, value): 
    #     if len(value) <2:
    #         raise serializers.ValidationError('Name is too short!')
    #     else:
    #         return value