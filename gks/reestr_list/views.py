from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, View
from .forms import Add_to_registerForm, Add_to_registerFormSet
from .models import Register



class IndexView(TemplateView):
    template_name = 'index.html'


class ReestrListView(ListView):
    queryset = Register.objects.all()
    context_object_name = 'reestr_list'
    paginate_by = 3
    template_name = 'reestr_list/list.html'


class Add_to_reestrView(CreateView):
    model =  Register
    success_url = '/reestr/'
    form_class = Add_to_registerForm
    template_name = 'reestr_list/add_to_register.html'


    def get_context_data(self, **kwargs):
        context = super(Add_to_reestrView, self).get_context_data(**kwargs)
        context['formset'] = Add_to_registerFormSet(queryset=Register.objects.none())
        return context

    def form_valid(self, formset):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.save()
        return self.render_to_response({'formset': formset})   
        
    def post(self, request, *args, **kwargs):
        formset = Add_to_registerFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                jc = form.save(commit=True)
                jc.id_numb = str(jc.date)
                jc.id_numb = str((Register.objects.filter(date__contains=str(jc.date.year)).count()) + 0) + '-' + \
                             jc.id_numb[2] + jc.id_numb[3]
                jc.save()
            formset.save()

        return self.render_to_response({'formset': formset})
   

def register_detail(request, id_numb):
    try:
        register = Register.objects.get(id_numb=id_numb)
    except Register.DoesNotExist:
        raise Http404("нет детальной информации")
    
    return render(request, 'reestr_list/list_detail.html', {'register':register})