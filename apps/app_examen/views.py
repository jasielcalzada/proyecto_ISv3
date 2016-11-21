from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.views.generic import FormView, CreateView, ListView,DetailView,UpdateView,DeleteView
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from .models import maestro, materia
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.contrib.auth.models import User

# Create your views here.
def index_view(request):
	return render(request,'app_examen/index.html')

class registro_maestro(FormView):
	template_name = 'app_examen/registro_maestro.html'
	form_class = UserForm
	success_url = reverse_lazy('index_view')

	def form_valid(self,form):
		user = form.save()
		p = maestro()
		p.user_perfil = user
		p.n_empleado = form.cleaned_data['n_empleado']
		p.nombre = form.cleaned_data['nombre']
		p.correo = form.cleaned_data['correo']
		p.save()
		return super(registro_maestro,self).form_valid(form)


class registro_materia(CreateView):
	template_name = 'app_examen/registro_materia.html'
	model = materia
	fields = ['serie','nombre','maestro_a']
	success_url = reverse_lazy('indn_empleado n_empleado ex_view')

	def post(self, request, *args, **kwargs):
		flag = False
		p = materia()
		query = materia.objects.filter(serie = request.POST['serie'])
		if query:
			if query.count == 1:
				flag = False
		else:
			a = request.POST['maestro_a']
			user = maestro.objects.get(n_empleado=a)
			print user
			p.serie = request.POST['serie']
			p.nombre = request.POST['nombre']
			p.maestro_a = user
			p.save()

		return render(request,'app_examen/registro_materia.html',{'flag':flag})


def listado_materias(request):
	
	current_user = request.user.profile.n_empleado
	materias = materia.objects.filter(maestro_a = current_user)
	ctx = {'materias':materias,}
	return render(request,'app_examen/listado_materias.html',ctx)

class detalle_materia(DetailView):
    template_name = 'app_examen/detalle_materia.html'
    slug_field = 'serie'
    model = materia