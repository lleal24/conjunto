from django.conf.urls import url, include
from app.empleado.views import index_empleado, empleado_view, EmpleadoList, \
EmpleadoCreate, EmpleadoUpdate, EmpleadoDelete

#dentro de urlpatterns listar todas las urls de la app
urlpatterns = [
    url(r'^$', index_empleado, name='index_empleado'),
    url(r'^crear$', EmpleadoCreate.as_view(), name='crear_empleado'),
    url(r'^listar$', EmpleadoList.as_view(), name='listar_empleado'),
    url(r'^editar/(?P<pk>\d+)/$', EmpleadoUpdate.as_view(), name='editar_empleado'),
    url(r'^eliminar/(?P<pk>\d+)/$', EmpleadoDelete.as_view(), name='eliminar_empleado'),

]