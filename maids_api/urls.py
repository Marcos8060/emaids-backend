from django.urls import path
# from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/',CustomUserCreate.as_view(),name='create_user'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),name='blacklist'),
    path('profiles/',ProfileList.as_view()),
    path('profiles/<int:pk>/',ProfileDetail.as_view()),
    path('comments/',CommentList.as_view()),
    path('comments/<int:pk>/',CommentDetail.as_view()),
    path('profiles/search/',ProfileListDetailFilter.as_view()),
    path('admin/profiles/',AdminProfileView.as_view()),
    path('admin/delete/<int:pk>',DeleteProfile.as_view()),
    path('edit/<int:pk>/',EditProfile.as_view()),
    path('summary/',ProfileSummary.as_view()),

    
    # JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

