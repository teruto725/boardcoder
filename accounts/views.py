from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView
from .models import CustomUser
from .forms import CustomUserSignUpForm, CustomUserChangeForm


class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserSignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")# dont use reverse as a sucess url

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            #messages.success(self.request, "OK,upload:"+obj.name)
            return HttpResponseRedirect(reverse("accounts:login"))
        else:
            raise Http404("Question does not exist")

class UserDetailView(DetailView):
    model = CustomUser
    template_name = "accounts/detail.html"

    # override
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.request.user.is_authenticated:
            messages.error(self.request,"please login")
            return HttpResponseRedirect(reverse('accounts:login'))
        elif self.object.pk == self.request.user.pk:
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            messages.error(self.request, "permission denied")
            return HttpResponseRedirect(reverse('home:home'))


class UserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = "accounts/update.html"

    def get_success_url(self):
        return reverse_lazy('accounts:detail', kwargs={'pk': self.object.pk})


