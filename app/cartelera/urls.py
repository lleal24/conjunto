from django.conf.urls import url, include
from app.cartelera.views import index_cartelera, cartelera_view, CarteleraList, CarteleraCreate, CarteleraUpdate, CarteleraDelete

#dentro de urlpatterns listar todas las urls de la app
urlpatterns = [
    url(r'^$', index_cartelera, name='index_cartelera'),
    url(r'^crear$', CarteleraCreate.as_view(), name='crear_cartelera'),
    url(r'^listar$', CarteleraList.as_view(), name='listar_cartelera'),
    url(r'^editar/(?P<pk>\d+)/$', CarteleraUpdate.as_view(), name='editar_cartelera'),
    url(r'^eliminar/(?P<pk>\d+)/$', CarteleraDelete.as_view(), name='eliminar_cartelera'),

   
]