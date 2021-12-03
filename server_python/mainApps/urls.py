from django.urls import path, include

from .views import PersonOfficeView, PersonView, RegistratoinPerson

urlpatterns = [
    path('', PersonOfficeView.as_view(), name='main'),
    path('<int:pk>/', PersonView.as_view(), name='person'),
    path('registration/', RegistratoinPerson.as_view())
]

urlpatterns += [
    path('accoutns/', include('django.contrib.auth.urls'))
]