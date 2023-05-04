from django.shortcuts import render
from rest_framework.exceptions import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import CustomUser

from .models import Hackathon, Participant, Submission

from .serializers import HackathonSerialzier, ParticipantSerializer, SubmissionSerializer


class HackathonView(APIView):
    def post(self, request):
        print(str(request.data))
        data = request.data
        serializer = HackathonSerialzier(data=data)
        usr_id = request.data['user_id']
        usr = CustomUser.objects.filter(id=usr_id).first()
        if usr == None:
            return Response({"error" : "User does not exist"}, status = status.HTTP_404_NOT_FOUND)
        if not usr.is_organizer:
            return Response({"error" : "User is not registered as an organizer"})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        dataset = Hackathon.objects.all()
        print(dataset)
        data = HackathonSerialzier(dataset, many=True)
        print(data.data)
        return Response(data.data, status = status.HTTP_200_OK)


class GetUserHackathons(APIView):
    def get(self, request):
        user_id = request.GET['user_id']
        dataset = Participant.objects.filter(user = user_id)
        hcthons = []
        i = 0
        flg = False
        for ptp in dataset:
            i += 1
            hcthons.append(ptp.hackathon)
        if i > 0:
            flg = True
        data = HackathonSerialzier(hcthons, many=flg)
        return Response(data.data, status = status.HTTP_200_OK)



class RegisterHackathon(APIView):
    def post(self, request):
        data = request.data
        usr = CustomUser.objects.filter(id = data['user']).first()
        if usr.is_organizer:
            return Response({"error" : "Organizers are not allowed to register!"}, status = status.HTTP_400_BAD_REQUEST)
        serializer = ParticipantSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class SubmissionView(APIView):
    def post(self, request):
        data = request.data
        serializer = SubmissionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        params = request.GET;
        submission = None
        sub_id = None
        usr_id = None
        try:
            sub_id = params['sub_id']
        except:
            pass
        try:
            usr_id = params['usr_id']
        except:
            pass
        flg = False
        if sub_id != None:
            submission = Submission.objects.filter(id = sub_id).first()
        else:
            print(usr_id)
            submission = Submission.objects.filter(participant__user__id = usr_id)
            flg = True
        if submission == None:
            return Response({"error" : "Submission not found!"}, status = status.HTTP_404_NOT_FOUND)
        data = SubmissionSerializer(submission, many=flg)
        return Response(data.data, status = status.HTTP_200_OK)
