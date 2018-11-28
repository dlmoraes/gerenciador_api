# coding = utf-8

from django.urls import path

from .api.viewsets import DiarioViewSet, DiarioRetrieveUpdateAPIView

urlpatterns = [
    path('', DiarioViewSet.as_view(), name='diario_list_create'),
    path('<int:id>/', DiarioRetrieveUpdateAPIView.as_view(), name='diario_update'),
]