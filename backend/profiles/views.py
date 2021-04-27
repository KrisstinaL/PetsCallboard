from rest_framework import generics
from rest_framework import permissions

from .models import Profile
from .serializers import ProfileSer, ProfileUpdateSer, AvatarUpdateSer


class ProfileDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSer


class ProfileUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSer


class AvatarProfileUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = AvatarUpdateSer

