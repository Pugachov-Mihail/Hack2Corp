from django.urls import path
from .views import InstructionsViews, PersonSerializer


urlpatterns = [
    path('instruction/', InstructionsViews.as_view()),
    path('user_list/', InstructionsViews.as_view())
]