
from mywebapp.forms import CertificatesForm, ProjectForm
from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import (
    TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View)
from mywebapp.models import Certificates, Projects
from django.utils import timezone
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
# Create your views here.


class Aboutpage(TemplateView):
    template_name = 'about.html'


def contact(request):
    if request.method == 'POST':
        full_name = request.POST.get('full-name')
        fromemail = request.POST.get('email')
        user_message = request.POST.get('user-message')
        send_mail(
            'Feedback by ' + full_name,
            user_message,
            fromemail,
            ['sumithgs2000@gmail.com']
        )
        return render(request, 'contactme.html', {'msg': full_name})
    else:
        return render(request, 'contactme.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('projects_list'))


def user_login(request):
    if request.method == 'POST':
        username1 = request.POST.get('username')
        password2 = request.POST.get('password')
        user = authenticate(username=username1, password=password2)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('projects_list'))
            else:
                return HttpResponse('Account not active')
        else:
            print('someone tried to login and failed')
            print('Username:{} and password {}'.format(username1, password2))
            return HttpResponse('Invalid login details supplied!')
    else:
        return render(request, 'registrations/login.html', {})


class ProjectsListView(ListView):
    model = Projects

    def get_queryset(self):
        return Projects.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')


class ProjectsDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'projects_detail'
    model = Projects


class ProjectsUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'mywebapp/projects_detail.html'
    form_class = ProjectForm
    model = Projects


class ProjectsDeleteView(LoginRequiredMixin, DeleteView):
    model = Projects
    template_name = 'mywebapp/confirmdelete.html'
    success_url = reverse_lazy('projects_list')


class ProjectsCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'mywebapp/projects_detail.html'
    form_class = ProjectForm
    model = Projects


class CertificatesListView(ListView):
    model = Certificates
    context_object_name = 'certificates_list'

    def get_queryset(self):
        return Certificates.objects.all()


class CertificatesDetailView(DetailView):
    context_object_name = 'certificates_detail'
    template_name = 'mywebapp/certificates_detail.html'
    model = Certificates


class CertificatesUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'mywebapp/certificates_detail'
    form_class = CertificatesForm
    model = Certificates


class CertificatesCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'mywebapp/certificates_detail'
    form_class = CertificatesForm
    model = Certificates


class CertificatesDeleteView(LoginRequiredMixin, DeleteView):
    model = Certificates
    template_name = 'mywebapp/confirmdeletecertificate.html'
    success_url = reverse_lazy('certificates_list')
