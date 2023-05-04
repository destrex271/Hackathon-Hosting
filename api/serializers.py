from rest_framework import serializers

from users.models import CustomUser
from .models import Hackathon, Participant, Submission


class HackathonSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Hackathon
        fields = '__all__'


class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Submission
        fields = '__all__'


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = '__all__'
