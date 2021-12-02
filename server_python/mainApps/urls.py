from django.urls import path

from .views import InstrustionView, PersonView

urlpatterns = [
    path('', InstrustionView.as_view(), name='main'),
    path('person/<int:pk>/', PersonView.as_view(), name='person')
]