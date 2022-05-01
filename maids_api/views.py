from rest_framework import viewsets,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.serializers import *
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission,AllowAny,DjangoModelPermissionsOrAnonReadOnly,IsAuthenticated
from rest_framework import filters
from rest_framework import permissions
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .permissions import IsOwnerOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.tokens import RefreshToken


# user registration view
class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            new_user = reg_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



# class ProfileUserWritePermission(BasePermission):
#         message = 'Editing posts is restricted to the owner only.'

#         def has_object_permission(self, request, view, obj):
#             if request.method in SAFE_METHODS:
#                 return True
            
#             return obj.author == request.user


class ProfileList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Profile.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ProfileSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

   
class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class CommentList(generics.ListCreateAPIView):
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ProfileListDetailFilter(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=location']  #exact match search
    # ['^slug'] starts-with search functionality
    # ['@']  full text search works best with postgresql
    # ['$']  regex search


class AdminProfileView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class EditProfile(generics.RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class DeleteProfile(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# dashboard summary view
class ProfileSummary(APIView):
    def get(self, request):
        profiles = Profile.total_profiles()
        return Response({
            'profiles': profiles,
        })




