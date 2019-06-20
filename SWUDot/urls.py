from django.urls import path
from .views import *

# photo 앱에 관련된 뷰들의 URL 설정
urlpatterns = [

    path('user/', UserListAPI.as_view()),
    path('user/<int:pk>', UserDetailAPI.as_view()),
    path('storeinfo/', StoreInfoListAPI.as_view()),
    path('storeinfo/<int:pk>', StoreInfoDetailAPI.as_view()),
    path('review/', ReviewListAPI.as_view()),
    path('review/<int:pk>', ReviewDetailAPI.as_view()),
    path('schoolinfo/', SchoolInfoListAPI.as_view()),
    path('schoolinfo/<int:pk>', SchoolInfoDetailAPI.as_view()),


]