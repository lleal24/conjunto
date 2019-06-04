from django.conf.urls import url, include
from app.usuario.views import RegistroUsuario
from django.contrib.auth.decorators import permission_required
from app.usuario.views import UsuarioList, UsuarioUpdate, UsuarioDelete



urlpatterns = [
    
    url(r'^registrar$', (RegistroUsuario.as_view()), name='registrar'),
    url(r'^listar$', UsuarioList.as_view(), name='listar_usuario'),
    url(r'^editar/(?P<pk>\d+)/$', UsuarioUpdate.as_view(), name='editar_usuario'),
    url(r'^eliminar/(?P<pk>\d+)/$', UsuarioDelete.as_view(), name='eliminar_usuario'),
    
]