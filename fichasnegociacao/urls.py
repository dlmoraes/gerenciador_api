from django.urls import path

from .api.viewsets import FichaListApiView
#from .views import HomeView, FichasSearch, Fichas

urlpatterns = [
    path('', FichaListApiView.as_view(), name='fichas_list'),
#    path('', HomeView.as_view(), name='home'),
#    path('gerarfichas/', FichasSearch.as_view(), name='gerar_ficha'),
#    path('fichasdenegociacao/', Fichas.as_view(), name='fichas'),
]