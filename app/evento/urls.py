from django.conf.urls import url, include
from app.evento.views import index_evento, evento_view, EventoList, EventoCreate, EventoUpdate, EventoDelete

#dentro de urlpatterns listar todas las urls de la app
urlpatterns = [
    url(r'^$', index_evento, name='index_evento'),
    url(r'^crear$', EventoCreate.as_view(), name='crear_evento'),
    url(r'^listar$', EventoList.as_view(), name='listar_evento'),
    url(r'^editar/(?P<pk>\d+)/$', EventoUpdate.as_view(), name='editar_evento'),
    url(r'^eliminar/(?P<pk>\d+)/$', EventoDelete.as_view(), name='eliminar_evento'),

   
]