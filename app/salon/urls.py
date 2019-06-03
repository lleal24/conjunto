from django.conf.urls import url, include
from app.salon.views import index_salon, salon_view, SalonList, SalonCreate, SalonUpdate, SalonDelete

#dentro de urlpatterns listar todas las urls de la app
urlpatterns = [
    url(r'^$', index_salon, name='index_salon'),
    url(r'^crear$', SalonCreate.as_view(), name='crear_salon'),
    url(r'^listar$', SalonList.as_view(), name='listar_salon'),
    url(r'^editar/(?P<pk>\d+)/$', SalonUpdate.as_view(), name='editar_salon'),
    url(r'^eliminar/(?P<pk>\d+)/$', SalonDelete.as_view(), name='eliminar_salon'),

   
]