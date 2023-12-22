from django.contrib.auth.models import User
from rest_framework import serializers

class RegistractionSeriallizer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only': True}
        }
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'P1 and P2 should be the same!'}) 
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists!'}) 
        
        # 입력된 email과 username이 같은 User에 대해서 password 저장.
        account = User(email=self.validated_data['email'], username=self.validated_data['username'], password=password)
        account.set_password(password)      
        account.save()
        
        return account  