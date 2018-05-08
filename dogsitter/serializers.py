from rest_framework import serializers

from .models import UserProfile, UserStatus, Feedback


class UserProfileSerializer(serializers.ModelSerializer):

    #user_status = serializers.StringRelatedField(many=True)

    class Meta:
        fields = (
            'firstName',
            'lastName',
            'email_id',
            'address',
            'password',
            'role'
        )
        model = UserProfile


class FeedbackSerializer(serializers.ModelSerializer):


    class Meta:
        fields = (
                    'appointment_id',
                    'firstName',
                    'lastName',
                    'email_id',
                    'review'
        )
        model = Feedback


class UserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'status',
            'updated_time',
            'is_active',
            'user_id',
        )
        model = UserStatus
