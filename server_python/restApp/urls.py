from django.urls import path, include
from .views import InstructionsViews, CreatePerson, SingleArticleView


urlpatterns = [
    path('instruction/', InstructionsViews.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('instruction/<int:pk>', SingleArticleView.as_view()),
    path('register/', CreatePerson.as_view())
]