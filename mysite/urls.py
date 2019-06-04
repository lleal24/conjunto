"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'apartamento'
app_name = 'torre'
app_name = 'conjunto'
app_name = 'propietario'
app_name = 'empresa'
app_name = 'evento'
app_name = 'noticia'
app_name = 'usuario'


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^conjunto/', include(('app.conjunto.urls', 'conjunto'), namespace='conjunto')),
    url(r'^torre/', include(('app.torre.urls', 'torre'), namespace='torre')),
    url(r'^apartamento/', include(('app.apartamento.urls', 'apartamento'), namespace='apartamento')),
    url(r'^propietario/', include(('app.propietario.urls', 'propietario'), namespace='propietario')),
    url(r'^salon/', include(('app.salon.urls', 'salon'), namespace='salon')),
    url(r'^empresa/', include(('app.empresa.urls', 'empresa'), namespace='empresa')),
    url(r'^empleado/', include(('app.empleado.urls', 'empleado'), namespace='empleado')),
    url(r'^evento/', include(('app.evento.urls', 'evento'), namespace='evento')),
    url(r'^noticia/', include(('app.noticia.urls', 'noticia'), namespace='noticia')),
    url(r'^cartelera/', include(('app.cartelera.urls', 'cartelera'), namespace='cartelera')),
    url(r'^usuario/', include(('app.usuario.urls', 'usuario'), namespace='usuario')),
    url(r'^home/', TemplateView.as_view(template_name='home.html'),name='home'),
    url('', LoginView.as_view(template_name='index.html'),name='login'),
    url(r'^logout', LogoutView.as_view, name='logout'),
    
    
    #url(r'^mascota/', include(('app.mascota.urls', 'mascota'), namespace='mascota')),  

]