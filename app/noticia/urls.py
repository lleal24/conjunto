from django.conf.urls import url, include
from app.noticia.views import index_noticia, noticia_view, NoticiaList, NoticiaCreate, NoticiaUpdate, NoticiaDelete

#dentro de urlpatterns listar todas las urls de la app
urlpatterns = [
    url(r'^$', index_noticia, name='index_noticia'),
    url(r'^crear$', NoticiaCreate.as_view(), name='crear_noticia'),
    url(r'^listar$', NoticiaList.as_view(), name='listar_noticia'),
    url(r'^editar/(?P<pk>\d+)/$', NoticiaUpdate.as_view(), name='editar_noticia'),
    url(r'^eliminar/(?P<pk>\d+)/$', NoticiaDelete.as_view(), name='eliminar_noticia'),

   
]