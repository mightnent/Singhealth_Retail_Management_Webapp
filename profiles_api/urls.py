from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('profile',views.UserProfileViewSet) #no need basename cuz will auto infer from queryset
router.register('feed',views.UserProfileFeedViewSet)

urlpatterns = [
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]