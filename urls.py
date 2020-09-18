from django.conf.urls import url
from .views import*

urlpatterns=[
    url (r'^$', home, name="index"),
    url (r'^CrearCiudad/', crearCiudad, name="crear_ciudad"),
    url (r'^ListarCiudad/', listarCiudad, name="Listar_ciudad"),
    url (r'^EditarCiudad/(?P<id>\d+)/$', editarCiudad, name = "editar_ciudad"),
    url (r'^EliminarCiudad/(?P<id>\d+)/$', eliminarCiudad, name = "eliminar_ciudad"),
    url (r'^CrearPersona/', crearPersona, name="crear_persona"),
    url (r'^ListarPersona/', listarPersona, name="Listar_persona"),
    url (r'^EditarPersona/(?P<id>\d+)/$', editarPersona, name = "editar_persona"),
    url (r'^EliminarPersona/(?P<id>\d+)/$', eliminarPersona, name = "eliminar_persona"),
    url (r'^CrearDocumento/', crearDocumento, name = "crear_documento"),
    url (r'^ListarDocumento/', listarDocumento, name = "listar_documento"),
    url (r'^EliminarDocumento/(?P<id>\d+)/$', eliminarDocumento, name = "eliminar_documento"),
    url (r'^EditarDocumento/(?P<id>\d+)/$', editarDocumento, name = "editar_documento"),
]