from django.urls import path, include
from .views import InstructionsViews, CreatePerson


urlpatterns = [
    path('instruction/', InstructionsViews.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('register/', CreatePerson.as_view())
]