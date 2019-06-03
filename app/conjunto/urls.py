from django.conf.urls import url, include
from app.conjunto.views import index_conjunto, conjunto_view, ConjuntoList, \
ConjuntoCreate, ConjuntoUpdate, ConjuntoDelete

#dentro de urlpatterns listar todas las urls de la app
urlpatterns = [
    url(r'^$', index_conjunto, name='index_conjunto'),
    url(r'^crear$', ConjuntoCreate.as_view(), name='crear_conjunto'),
    url(r'^listar$', ConjuntoList.as_view(), name='listar_conjunto'),
    url(r'^editar/(?P<pk>\d+)/$', ConjuntoUpdate.as_view(), name='editar_conjunto'),
    url(r'^eliminar/(?P<pk>\d+)/$', ConjuntoDelete.as_view(), name='eliminar_conjunto'),
  
   
]