from rest_framework import serializers
from watchlist_app.models import Movie



class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"
        
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Description should be different!")
        else:
            return data
            
    def validate_name(self, value): 
        if len(value) <2:
            raise serializers.ValidationError('Name is too short!')
        else:
            return value