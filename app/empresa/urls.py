from django.conf.urls import url, include
from app.empresa.views import index_empresa, empresa_view, EmpresaList, \
EmpresaCreate, EmpresaUpdate, EmpresaDelete

#dentro de urlpatterns listar todas las urls de la app
urlpatterns = [
    url(r'^$', index_empresa, name='index_empresa'),
    url(r'^crear$', EmpresaCreate.as_view(), name='crear_empresa'),
    url(r'^listar$', EmpresaList.as_view(), name='listar_empresa'),
    url(r'^editar/(?P<pk>\d+)/$', EmpresaUpdate.as_view(), name='editar_empresa'),
    url(r'^eliminar/(?P<pk>\d+)/$', EmpresaDelete.as_view(), name='eliminar_empresa'),

]