from rest_framework import routers
from .views import NoteViewSet, create_auth, get_user_by_token
from django.urls import path


router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)
urlpatterns = [
    path('register/', create_auth),
    path('whoami/', get_user_by_token),
]
urlpatterns += router.urls

