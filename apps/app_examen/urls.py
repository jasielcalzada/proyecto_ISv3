from django.conf.urls import url
from .views import *
from django.contrib.auth.views import login, logout_then_login

urlpatterns = [
	url(r'^$',login,{'template_name':'app_examen/index.html'}, name='login'),
	url(r'^$',index_view,name='index_view'),
	url(r'^registro_maestro/$',registro_maestro.as_view(),name='registro_maestro'),
	url(r'^registro_materia/$',registro_materia.as_view(),name='registro_materia'),
	url(r'^listado_materias/$',listado_materias,name='listado_materias.html'),
	url(r'^detalle_materia/(?P<slug>[-\w]+)/$',detalle_materia.as_view(),name='detalle_materia'),
	url(r'^logout/$', logout_then_login, name='logout'),
]