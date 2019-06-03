from django.conf.urls import url, include
from app.apartamento.views import index_apartamento, apartamento_view, ApartamentoList, \
ApartamentoCreate, ApartamentoUpdate, ApartamentoDelete

#dentro de urlpatterns listar todas las urls de la app
urlpatterns = [
    url(r'^$', index_apartamento, name='index_apartamento'),
    url(r'^crear$', ApartamentoCreate.as_view(), name='crear_apartamento'),
    url(r'^listar$', ApartamentoList.as_view(), name='listar_apartamento'),
    url(r'^editar/(?P<pk>\d+)/$', ApartamentoUpdate.as_view(), name='editar_apartamento'),
    url(r'^eliminar/(?P<pk>\d+)/$', ApartamentoDelete.as_view(), name='eliminar_apartamento'),

]