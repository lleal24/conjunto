from django.conf.urls import url, include
from app.propietario.views import index_propietario, propietario_view, PropietarioList, \
PropietarioCreate, PropietarioUpdate, PropietarioDelete

#dentro de urlpatterns listar todas las urls de la app
urlpatterns = [
    url(r'^$', index_propietario, name='index_propietario'),
    url(r'^crear$', PropietarioCreate.as_view(), name='crear_propietario'),
    url(r'^listar$', PropietarioList.as_view(), name='listar_propietario'),
    url(r'^editar/(?P<pk>\d+)/$', PropietarioUpdate.as_view(), name='editar_propietario'),
    url(r'^eliminar/(?P<pk>\d+)/$', PropietarioDelete.as_view(), name='eliminar_propietario'),
  
   
]