from django.conf.urls import url, include
from app.torre.views import index_torre, torre_view, TorreList, TorreCreate, TorreUpdate, TorreDelete

#dentro de urlpatterns listar todas las urls de la app
urlpatterns = [
    url(r'^$', index_torre, name='index_torre'),
    url(r'^crear$', TorreCreate.as_view(), name='crear_torre'),
    url(r'^listar$', TorreList.as_view(), name='listar_torre'),
    url(r'^editar/(?P<pk>\d+)/$', TorreUpdate.as_view(), name='editar_torre'),
    url(r'^eliminar/(?P<pk>\d+)/$', TorreDelete.as_view(), name='eliminar_torre'),

   
]