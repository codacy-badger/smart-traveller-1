from rest_framework import serializers

from accounts.models import CustomUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    A Serializer for the user model with all required field.
    """
    class Meta:
        """
        Exposes required model fields.
        """
        model = CustomUser
        fields = ('url', 'mobile','username', 'email', 'first_name', 'last_name', 'created_at', 'updated_at', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data.pop('password'))
        user.save()

        return user

    def update(self, instance, validated_data):
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.save()

        return instance
